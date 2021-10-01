#!/usr/bin/python3


from lib import timer



@timer
def main(N):
	n = N*2                        # i know, arbitary
	P = [-1,1]
	primes = [True]*n
	s = 0

	for p in range(3,n,2):
		if p>N: return s+2
		if P[1] == N: break
		elif primes[p]:
			s+=p
			P = [p, P[1]+1]
			for _ in range(p*2, n, p): primes[_] = False
# 1.3s




main(2_000_000)

