#!/usr/bin/python3.7
from lib import timer





fib = [2,8]

@timer
def main(l):
	while fib[-1] < l:
		fib.append(4*fib[-1]+fib[-2])       # aparently i noticed the pattern long ago ...
	print(sum(fib[:-1]))
	return sum(fib[:-1])



main(4_000_000)



