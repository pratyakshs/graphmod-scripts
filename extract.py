import sys, getopt, os, re
inputfile = sys.argv[1]

f = open(inputfile)
alltext = f.read()
lines = alltext.splitlines()

logE = 0.43429448190325182765112891
inf = 9999999999999999

marker1, marker2 = -1, -1

linenum = 0
pre_time = 0

for linenum, line in enumerate(lines):
	if 'Initialization complete' in line:
		pre_time = float(line.split()[-2])
	if 'Starting search' in line:
		marker1 = linenum + 1
	if 'Search done' in line:
		marker2 = linenum - 3

if marker2 == -1:
	marker2 = linenum

# print(marker2, marker1)

if marker1 == -1:
	if 'Solved during initialization' in alltext:
		for k, t in enumerate([10, 60, 600, 3600, 10800, 21600]):
			fo = open('extracted/'+sys.argv[2]+'-'+sys.argv[3]+'-i'+sys.argv[4]+'-'+sys.argv[5]+'-t'+str(t)+'.ext', 'w')
			print(str(inf)+' '+str(inf)+' '+str(inf)+' '+str(pre_time), file = fo)
			fo.close()

	else:
		for k, t in enumerate([10, 60, 600, 3600, 10800, 21600]):
			fo = open('extracted/'+sys.argv[2]+'-'+sys.argv[3]+'-i'+sys.argv[4]+'-'+sys.argv[5]+'-t'+str(t)+'.ext', 'w')
			print(str(inf)+' '+str(inf)+' '+str(inf)+' '+str(inf), file = fo)
			fo.close()

elif marker2 - marker1 < 0:
	for k, t in enumerate([10, 60, 600, 3600, 10800, 21600]):
		fo = open('extracted/'+sys.argv[2]+'-'+sys.argv[3]+'-i'+sys.argv[4]+'-'+sys.argv[5]+'-t'+str(t)+'.ext', 'w')
		print(str(inf)+' '+str(inf)+' '+str(inf)+' '+str(inf), file = fo)
		fo.close()
#	print('& Out of memory & No solution & & & & & \\\\')


else:
	rows = marker2 - marker1 + 1
	time = ['x'] * rows
	ornodes = ['x'] * rows
	andnodes = ['x'] * rows
	weight = ['x'] * rows
	cost = ['x'] * rows
	uw = ['x'] * rows

	for i in range(marker1, marker2 + 1):
		time[i - marker1] = float(re.findall('[0-9]+\.[0-9]*', re.findall('\[.*\]', lines[i])[0])[0]) + pre_time
		row = lines[i].split()
		for j, k in enumerate(row):
			if k == 'w' or k  == 'u':
				break
		uw[i - marker1] = row[j]
		weight[i - marker1] = float(row[j + 1])
		ornodes[i - marker1] = float(row[j + 2])
		andnodes[i - marker1] = float(row[j + 3])
		cost[i - marker1] = '{0:.4f}'.format(float(row[j + 4])*logE)
	j = 0
	cols = [0] * 6
	labels = ['Cost', 'Nodes', 'Weight', 'Time']
	for i, t in enumerate([10.0, 60.0, 600.0, 3600.0, 10800.0, 21600.0]):
		while j < rows:
			if uw[j] == 'u':
				j += 1 
				continue
			if time[j] > t:
				if j > 0: 
					j -= 1
				break
			j += 1
		if j < rows:
			cols[i] = [cost[j], ornodes[j] + andnodes[j], weight[j], time[j]]
	for i, c in enumerate(cols):
		if c == 0:
			cols[i] = [cost[rows-1], ornodes[rows-1]+andnodes[rows-1], weight[rows-1], time[rows-1]]

	for k, t in enumerate([10, 60, 600, 3600, 10800, 21600]):
		dat = ''
		for j in range(0, 4):
			dat += str(cols[k][j]) + ' '
		fo = open('extracted/'+sys.argv[2]+'-'+sys.argv[3]+'-i'+sys.argv[4]+'-'+sys.argv[5]+'-t'+str(t)+'.ext', 'w')
		# filename example: extracted/jglp-pedigree20-i18-araobf-t600.ext
		print(dat, file = fo)
		fo.close()
