#!/usr/bin/python3



from lib import timer





def chain_length(n):
	l = 0
	while True:
		if n==1: break
		if n%2==0: n/=2
		else: n=3*n+1
		l+=1
	return l+1


@timer
def main(n):
	table = [-1]*n
	i = 2
	m = -1
	cl = -1
	while i < n:
		if table[i]>-1:
			_cl = table[i]
		else:
			_cl = chain_length(i)
		if cl < _cl:
			m = i
			cl = _cl
		i+=1
	return m

# ~90s






######################################
# table = {}
# def chain_length(a):
# 	if a in table.keys():
# 		return table[a]
# 	l = 0
# 	n = a
# 	while True:
# 		if n==1: break
# 		if n%2==0: n/=2
# 		else: n=3*n+1
# 		l+=1
# 	table[a] = l+1
# 	return l+1


# @timer
# def main(n):
# 	i = 2
# 	m = -1
# 	cl = -1
# 	while i < n:
# 		_cl = chain_length(i)
# 		if cl < _cl:
# 			m = i
# 			cl = _cl
# 		i+=1
# 	return m

# ~90s



main(1_000_000)


