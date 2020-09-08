#!/usr/bin/python3.7


from lib import timer


from math import sqrt
from math import ceil, floor






@timer
def main(N):
	n = N*11                        # i know, arbitary
	P = [-1,1]
	primes = [True]*n
	# primes = [False, True]*int(n//2+100)

	for p in range(3,n,2):
		if P[1] == N: break
		elif primes[p]:
			P = [p, P[1]+1]
			for _ in range(p*2, n, p): primes[_] = False
	return P[0]
	# return P, [_ for _ in range(2,len(primes)) if primes[_]][N+400]
	# return [_ for _ in range(2,len(primes)) if primes[_]][N-1]
# ~20m
#  ^
# ~30m





# primes = [2,3]
# @timer
# def main(n):
# 	i=5
# 	while len(primes) < n:
# 		for _ in primes[:ceil(sqrt(len(primes)))]:
# 			if i%_==0: break
# 		else: primes.append(i)
# 		i+=2
# 	return primes[-1]
# ~100m


# primes = [2]
# @timer
# def main(n):
# 	i=3
# 	while len(primes) < n:
# 		for _ in primes:
# 			if i%_==0: break
# 		else: primes.append(i)
# 		i+=2
# 	return primes[-1]
# ~3.7s



main(10001)



