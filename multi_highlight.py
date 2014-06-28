import sys, math
from sol import SOL

inputfile = sys.argv[1]
problem_name = sys.argv[2]

f = open(inputfile)
alltext = f.read()
lines = alltext.splitlines()

numrows = 5

inf = 9999999999999
table = [[[inf]*4 for i in range(numrows)] for j in range(6)]
# 4 is number of attributes in a cell

a = 0

for line in lines:
	if 'Cost' in line or 'Search did not start' in line:
		l = line.split('\\\\')
		for i in range(0, 4):
			row = l[i].split('&')
			for j in range(0, 6):
				try:
					table[j][a][i] = math.fabs(float(row[j+2]))
# fabs because weight is sometimes printed -1. 
				except:
					table[j][a][i] = inf
		a += 1


hcells = [0]*6

# only using two shades of gray
def mymin(time_row):
	min_cost = [inf-10]*2
	for cells in time_row:
		if cells[0] < min_cost[0]:
			min_cost[0] = cells[0]
	
	for cells in time_row:
		if min_cost[0] < cells[0] < min_cost[1]:
			min_cost[1] = cells[0]
	
	min_indices = [[], []]
	for i, cells in enumerate(time_row):
		if cells[0] == min_cost[0]:
			min_indices[0].append(i)
		elif cells[0] == min_cost[1]:
			min_indices[1].append(i)
	return min_indices	


for t in range(0, 6): # 6, one for each time col
	hcells[t] = mymin(table[t])

# hcells[i] contains two lists hcells[i][0], hcells[i][1]. hcells[i][0] will be coloured darker than hcells[i][1]

inv_hcells = [[[] for i in range(numrows)] for j in range(2)]

for t in range(len(hcells)):
	for index in hcells[t][0]:
		inv_hcells[0][index].append(t)
	for index in hcells[t][1]:
		inv_hcells[1][index].append(t)


def replace(line2, i, grayval):
	c = 0
	nl = ''
	for x in line2.split():
		if x == '&':
			if (c-i-1) % 7 == 0:
				nl += ' & \cellcolor[gray]{' + str(grayval) + '} '
			else:
				nl += ' & '
			c += 1
		else:
			nl = nl + ' ' + x + ' '
	return nl
	
a = 0
for linum, line in enumerate(lines):
	if 'Cost' in line or 'Search did not start' in line:
		line_new = line
		for i in inv_hcells[0][a]:
			line_new = replace(line_new, i, 0.65)
		for i in inv_hcells[1][a]:
			line_new = replace(line_new, i, 0.85)
		a += 1
		print(line_new)
	else:
		print(line)

