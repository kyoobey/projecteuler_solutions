


from lib import timer
from math import sqrt, ceil
from itertools import combinations
from functools import reduce





################################################
####### doesn't work

# def prime_table(N):
# 	n = N*11
# 	P = [-1,1]
# 	primes = [True]*n
# 	l = []

# 	for p in range(3,n,2):
# 		if P[1] == N: break
# 		elif primes[p]:
# 			l.append(p)
# 			P = [p, P[1]+1]
# 			for _ in range(p*2, n, p): primes[_] = False
# 	return l


# @timer
# def main(n):
# 	n = 3
# 	Dn = 2
# 	cnt = 0
# 	primes = prime_table(100000)
# 	while cnt < n:
# 		n += 1
# 		n1 = n
# 		if n1%2==0: n1=n1/2
# 		Dn1 = 1
# 		for p in primes:
# 			if p*p > n1:
# 				Dn1 = 2*Dn1
# 				break
# 			exponent = 1
# 			while n1 % p == 0:
# 				exponent+=1
# 				n1 = n1/p
# 			if exponent > 1:
# 				Dn1 = Dn1*exponent
# 			if n1 == 1: break
# 		cnt = Dn*Dn1
# 		Dn=Dn1
# 	return n*(n-1)/2






################################################
def prime_factors(n):
	l=[]
	if n%2==0:
		while n%2==0:
			l.append(2)
			n//=2
	for i in range(3, ceil(sqrt(n))+1, 2):
		if n%i==0:
			while n%i==0:
				l.append(i)
				n/=i
	# return l if n<2 else n
	l.append(n)
	return l

def all_factors(n):
	f = prime_factors(n)
	l = []
	for i in range(1,len(f)+1):
		l += combinations(f, i)
	for _ in range(len(l)):
		i = l.pop()
		i = reduce(lambda a,b: a*b, i)
		if i not in l: l.insert(0,i)
	return [1]+sorted(l)

@timer
def main(n):
	i = 2
	t = 1
	while True:
		t+=i
		# print(t)
		if len(all_factors(t)) > n:
			return t
		i+=1

# ~15s




main(500)

