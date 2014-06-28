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


# for i in range(0, 6):
# 	for j in range(0, numrows):
# 		table[i][j][4] = math.fabs(table[i][j][0] + SOL.get(problem_name))

hcells = [0]*6

def mymin(time_row):
	min_c = min_w = min_t = inf
	min_i = -1
	for i in range(len(time_row)):
# 0: cost, 1: nodes, 2: weight, 3: time
		if time_row[i][0] < min_c:
			min_c = time_row[i][0]
			min_w = time_row[i][2]
			min_t = time_row[i][3]
			min_i = i
		elif time_row[i][0] == min_c:
			if time_row[i][2] < min_w:
				min_w = time_row[i][2]
				min_t = time_row[i][3]
				min_i = i
			elif time_row[i][2] == min_w:
				if time_row[i][3] < min_t:
					min_t = time_row[i][3]
					min_i = i
	return min_i

for t in range(0, 6): # 6, one for each time col
	hcells[t] = mymin(table[t])

inv_hcells = [[], [], [], [], [], []]
for i in range(len(hcells)):
	inv_hcells[hcells[i]].append(i)

def replace(line2, i):
	c = 0
	nl = ''
	for x in line2.split():
		if x == '&':
			if (c-i-1) % 7 == 0:
				nl += ' & \cellcolor[gray]{0.8} '
			else:
				nl += ' & '
			c += 1
		else:
			nl = nl + ' ' + x + ' '
	return nl
	
a = 0
for linum, line in enumerate(lines):
	if 'Cost' in line:
		line_new = line
		for i in inv_hcells[a]:
			line_new = replace(line_new, i)
		a += 1
		print(line_new)
	else:
		print(line)

