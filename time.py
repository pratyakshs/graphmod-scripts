import os
import re

print(os.getcwd())

# os.chdir('..')
path = input('Enter the directory path which contains the output files: ')
os.chdir(path)

files = os.listdir('.')
problem = input('Enter the problem name: ') + '_'

mc = [i for i in files if problem in i]
print('Number of files matched:', len(mc))

temp = [open(i) for i in mc]
mcc = [i for i, f in zip(mc, temp) if 'Time elapsed' in f.read()]

for i in temp:
	i.close()

print('Number of files which contain \'Time elapsed\':', len(mcc))

temp = [open(i) for i in mcc]
mcf = [i for i, f in zip(mcc, temp) if 'fail' in f.read()]

print('Number of files which contain \'fail\':', len(mcf))

mccc = [i for i in mcc if i not in mcf]

time = float(input('Time lowerbound: '))

while time > 0:
	for i in mcc:
		if float(re.findall('[0-9]+\.[0-9]+', open(i).read().splitlines()[-4])[0]) >= time:
			print(i)
	time = float(input('Time lowerbound: '))


