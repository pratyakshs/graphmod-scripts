import sys
import math
logE = 1.0/math.log(10)

pv, ds, pd, iw = 0, 0, 0, 0

for i in range(1, len(sys.argv)):
	f = open('stdout/mbe/'+sys.argv[i]+'_i10-braobb-sqrt-den4-del0.1_64-withTies.out.txt')
	lines = f.read().splitlines()
	for line in lines:
		if 'Problem variables' in line:
			pv = line.split()[-1]
		if 'domain size' in line:
			ds = line.split()[-1]
		if 'Pseudotree depth' in line:
			pd = line.split()[-1]
		if 'Induced width' in line:
			iw = line.split()[-1]
	print('\"'+sys.argv[i]+'\"',':','','\"(n='+str(pv),'k='+str(ds),'w*='+str(iw),'h='+str(pd)+')\"', ',')
	f.close()	

print('\n\n')

i_list = [18, 14, 10, 8, 6, 4, 2]

for j in range(1, len(sys.argv)):
	flag = False
	for i in i_list:
		f = open('stdout/mbe/'+sys.argv[j]+'_i'+str(i)+'-braobb-sqrt-den4-del0.1_64-withTies.out.txt')
		lines = f.read().splitlines()
		for line in lines:
			if 'Solution:' in line:
				flag = True
				sol = line.split()[-1]
				print('\"'+sys.argv[j]+'\"',':', -logE*float(sol), ',')
		if flag:
			break

