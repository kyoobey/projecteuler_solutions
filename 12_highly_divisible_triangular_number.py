


from lib import timer
from math import sqrt, ceil
from itertools import combinations
from functools import reduce



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

