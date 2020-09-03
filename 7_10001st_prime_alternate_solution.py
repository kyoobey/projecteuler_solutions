
# this doesn't work, shit!!!


# 2
# 3
# 5 = 2+3
# 7 = (5+3)-1, (5+3)+1 == 3*3
# 11 = (5+7)-1
# 13 = (5+7)+1
# 17 = (7+11)-1
# 19 = (7+11)+1
# 23 = (11+13)-1, (11+13)+1 == 5*5
# 29 = (13+17)-1
# 31 = (13+17)+1


from math import sqrt, ceil, floor



primes = [2,3,5]
i=2


# new_primes = []


def is_prime(n):


	for k in primes[:int(sqrt(n))+1]:
		if n%k==0:
			return False
	return True





# while len(primes) > max(i, j):
for _ in range(20):
	s = primes[i] + primes[i-1]

	if is_prime(s-2):
		primes.append(s-1)

	if is_prime(s-1):
		primes.append(s-1)

	if is_prime(s+1):
		primes.append(s+1)

	i+=1

	# print(i)

	# print(primes)


	if primes[-1] == 43:
		# primes = primes[:-1] + [47,53]
		primes.append(47)




print(primes)