#!/usr/bin/python3.7

from lib import timer
from math import sqrt, ceil




# cant get any faster for me =(


@timer
def main(n):
	l=-1
	if n%2==0:                     # so, separating 2 almost halves the runtime
		l=2
		while n%2==0: n//=2
	for i in range(3, ceil(sqrt(n))+1, 2):
		if n%i==0:
			l=i
			while n%i==0: n/=i
	return l if n<2 else n
# ~40m wtf?


# @timer
# def main(n):
# 	l=-1
# 	for i in range(2, ceil(sqrt(n))+1):
# 		if n%i==0:
# 			l=i
# 			while n%i==0: n/=i
# 	return int(max(n,l))
# ~80m




main(600851475143)
# main(101)

