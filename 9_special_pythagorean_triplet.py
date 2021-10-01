#!/usr/bin/python3


from lib import timer
from math import sqrt


# @timer
# def main(n):
# 	for c in range(n):
# 		for b in range(c):
# 			a = n-b-c
# 			if a**2 + b**2 == c**2:
# 				return a*b*c
# ~90m for input = 1000


# @timer
# def main(n):
# 	for a in range(3,(n-3)//3):
# 		for b in range(a+1,(n-1-a)//2):
# 			c = n-a-b
# 			if a**2 + b**2 == c**2:
# 				return a*b*c
# ~70m for input = 1000


@timer
def main(n):
	def _hcf(a, b): return a if b<1 else _hcf(b, a%b)
	s2 = n/2
	max_limit = int(sqrt(s2)-1)
	for m in range(2, 21):
		if s2%m==0:
			sm = s2/m
			while sm%2==0:
				sm = sm / 2
			if m%2==1: k=m+2
			else: k = m+1
			while k < 2*m and k<=sm:
				if sm%k==0 and _hcf(k,m)==1:
					d = s2 / (k*m)
					n = k-m
					a = d*(m*m-n*n)
					b = 2*d*m*n
					c = d*(m*m+n*n)
					return a*b*c
				k+=2
# ~30µ



main(1000)
