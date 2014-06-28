import sys
inf = float('inf')

f = [open(sys.argv[i]) for i in range(1, len(sys.argv))]
alltext = [i.read() for i in f]
line = [[float(j) for j in i.split()] for i in alltext]


def min_index(L):
	# L is a list, each of it's members is a list of 4 floats (cost, nodes, weight, time)
	min_i, min_c, min_w, min_t = 0, inf, inf, inf
	for i, x in enumerate(L):
		if x[0] < min_c:
			min_c = x[0]
			min_w = x[2]
			min_t = x[3]
			min_i = i
		elif x[0] == min_c:
			if x[2] < min_w:
				min_w = x[2] 
				min_t = x[3]
				min_i = i
			elif x[2] == min_w:
				if x[3] < min_t:
					min_t = x[3]
					min_i = i
	return min_i

# print(min_index(line))

def min_index2(L):
	min_i, min_c, min_t = 0, inf, inf
	for i, x in enumerate(L):
		if x[0] < min_c:
			min_c = x[0]
			min_t = x[3]
			min_i = i
		elif x[0] == min_c:
			if x[3] <= min_t:
				min_t = x[3]
				min_i = i
	return min_i

print(min_index2(line))

def min_index_of2(L):
	min_i, min_c, min_t = 0, inf, inf
	if L[0][0] == L[1][0] and L[0][3] == L[1][3]:
		return 3

	for i, x in enumerate(L):
		if x[0] < min_c:
			min_c = x[0]
			min_t = x[3]
			min_i = i
		elif x[0] == min_c:
			if x[3] <= min_t:
				min_t = x[3]
				min_i = i
	return min_i

