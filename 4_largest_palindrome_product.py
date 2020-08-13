#!/usr/bin/python3.7


from lib import timer





# after some thought I think bruteforcing the factors would be more efficient,
# but you know what? this code works and I'm happy with this lol.


@timer
def main(l):
	for i in range(10**(l*2)-1,9*10**(l*2-1),-1):
		s = str(i)
		if s==s[::-1]:
			for j in range(10**l-1,9*10**(l-1),-1):
				# further analysis shows that one of the factors must be a multiple of 11
				# after adding this i realised that it has absolutely no effect
				if i%11==0:
					if (i/j)%1==0:
						if 10**(l-1)-1 < (i/j) < 10**l-1:
							return i
	return 0
# ~40m







main(3)

