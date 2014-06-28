import sys, getopt, os, re
inputfile = sys.argv[1]

f = open(inputfile)
alltext = f.read()
lines = alltext.splitlines()

logE = 0.43429448190325182765112891

# print('---------', inputfile, '------------')

#if 'Search done' in alltext:
#	print('Search done')
#	done = True
#else:
#	print('Search timed out')
#	done = False
#
#if 'failure' in alltext: 
#	print('Ran out of memory')
#	outofmemory = True
#elif 'success' in alltext:
#	print('Search successful')
#	outofmemory = False

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
		print('& Solved during initialization', end = '')
	else:
		print('& Search did not start', end = '')
	print('& & & & & & \\\\')
	for i in range(0, 4):
		print('& & & & & & & \\\\')
	print('\\hline')

elif marker2 - marker1 < 0:
	print('& Out of memory & No solution & & & & & \\\\')
	for i in range(0, 4):
		print('& & & & & & & \\\\')
	print('\\hline')


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
			if uw[j] == 'u' or weight[j] == -1:
				j += 1 
				continue
			if time[j] > t:
				if j > 0: 
					j -= 1
				break
			j += 1
		if j < rows:
			if time[j] < t:
				cols[i] = [cost[j], ornodes[j] + andnodes[j], weight[j], time[j]]
			else:
				cols[i] = [float('nan'), float('nan'), float('nan'), t]
	for i, c in enumerate(cols):
		if c == 0:
			cols[i] = [cost[rows-1], ornodes[rows-1]+andnodes[rows-1], weight[rows-1], time[rows-1]]
	for j in range(0, 4):
		print('&', labels[j], end = ' ')
		for k in range(0, 6):
			print('&', cols[k][j], end = ' ')
		print('\\\\')
	print('\\cline{2-8}')
	print('&  \\multicolumn{7}{|c|}{Preprocessing time:', pre_time,' seconds} \\\\')
	print('\\hline \\hline')

