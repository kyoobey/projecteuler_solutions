#!/usr/bin/python3.7



from lib import timer
from functools import reduce
from math import sqrt, ceil




# can be improved but i'm bored with this problem, so bye




# def factorise(n):
# 	l=[]
# 	while n%2==0:
# 		n//=2
# 		l.append(2)
# 	for i in range(3, ceil(sqrt(n))+1, 2):
# 		while n%i==0:
# 			n/=i
# 			l.append(i)
# 	# return l if n<2 else n
# 	return l if n<2 else l+[n]

@timer
def main(N):
	r = [2,3]
	p = 6
	for n in range(4,20):
		for i in r:
			if n%i==0: n//=i
		r.append(n)
		p*=n
	return p
# ~20µ






################################################
# approach 1 - best ~21µ




# @timer
# def main(n):
# 	def _hcf(a, b): return a if b<1 else _hcf(b, a%b)
# 	def _lcm(a, b): return (a*b)//_hcf(a, b)
# 	return reduce(lambda a,b : _lcm(a, b), range(2, n))
# ~25µ
# same code as below (line 45 - 53), but runs faster
# apperently calling functions in python takes ~5µ
# update:
########################
# @timer
# def main(n):
# 	def _hcf(a, b): return a if b<1 else _hcf(b, a%b)
# 	return reduce(lambda a,b : (a*b)//_hcf(a, b), range(2, n))
# ~22µ i've no idea how !! I should just use c++
########################
# 


# def lcm(*l):
# 	def _hcf(a, b): return a if b<1 else _hcf(b, a%b)
# 	def _lcm(a, b): return (a*b)//_hcf(a, b)
# 	return reduce(lambda a,b : _lcm(a, b), l)

# @timer
# def main(n):
# 	return lcm(*range(2, n))
# ~30µ


main(20)
