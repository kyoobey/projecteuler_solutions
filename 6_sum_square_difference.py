#!/usr/bin/python3.7

from lib import timer
from itertools import combinations








@timer
def main(n):
	s=0
	for i in range(1, n+1):
		s += i*((n-i+1)*(i+n)*0.5 - i)
	return s*2
# ~30µ
# using for loops is a little faster because of the i+=1 instruction
# instead of /2 use *0.5




# @timer
# def main(n):
# 	s=0
# 	i=1
# 	while i<=n:
# 		s += i*(((n-i+1)*(i+n)/2) - i)
# 		i+=1
# 	return s*2
# ~35µ
# used ap sum formula instead of sum and range




# @timer
# def main(n):
# 	s=0
# 	i=1
# 	while i<=n:
# 		s += i*sum(range(i+1, n+1))
# 		i+=1
# 	return s*2
# ~94µ huge improvement, but there's room for more, at the sum(range()) part










# @timer
# def main(n):
# 	s=0
# 	for a,b in combinations(range(1, n+1), 2):
# 		s+=a*b
# 	return s*2
# ~500µ, even trashier


# @timer
# def main(n):
# 	return 2*sum([a*b for a,b in combinations(range(1, n+1), 2)])
# ~500µ, trash code ...




main(100)
