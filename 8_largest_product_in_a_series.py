#!/usr/bin/python3.7




from lib import timer

from operator import mul
from functools import reduce
# from collections import deque

# Q = deque()




# prod = lambda x: reduce(mul, x, 1)


# @timer
# def main(a, l):
# 	s = prod([a[_] for _ in range(l)])
# 	last = a[:l]
# 	zero_idx = -1
# 	for _ in range(500):
# 		last.append(a.pop(0))
# 		print(last, s, zero_idx)

# 		if last[-1] == 0:
# 			while 0 in last:
# 				last, a = a[:l], a[l:]
# 			s = prod(last)
# 		# elif zero_idx > -1:
# 		# 	zero_idx -= 1


# 		# if zero_idx == 0:
# 		# 	last.pop(0)
# 		# 	s = 1
# 			# last[0] = 1
# 		# else:
# 		s = s // last.pop(0) * last[-1]








# @timer
# def main(a, l):
# 	s = prod(a[:l])

# 	i = 0

# 	nearest_zero_info = [False, 0]

# 	while i < len(a)-l:
# 		# if nearest_zero_info[0]: s=0

# 		s = 

# 		print(s, a[i:i+l], nearest_zero_info)
# 		# s = max(prod(a[i:i+l]), s)
# 		# print(a[i], prod(a[i:i+l]))

# 		if a[i+l] == 0:
# 			nearest_zero_info[0] = True
# 			nearest_zero_info[1] = l-1
# 		elif nearest_zero_info[1] > -1:
# 			nearest_zero_info[1] -= 1
# 			nearest_zero_info[0] = nearest_zero_info[1] > -1
# 			# print(nearest_zero_info[1] > -1)
# 		i+=1

# 	return s






# this is the solution
# vvvvvvvvvvvv

@timer
def main(a, l):
	m = -1

	i = 0
	while i < len(a)-l:
		if a[i+l-1] is not 0:
			_1, _2 = a[i], a[i+l]
			if _2 is not 0:
				rest = a[i+1:i+l]
				if 9 in rest:
					rp = reduce(mul, rest, 1) * (_1 if _1>_2 else _2)
					if m<rp:
						m = rp
		else:
			i+=l
		i+=1

	return m
# ~500µ












# @timer
# def main(a, l):
# 	m = -1
# 	for i in range(len(a)-l+1):
# 		_ = a[i:i+l]
# 		# if not 0 in _: m = max(m, reduce(mul, _, 1))
# 		# if (not 0 in _) and (9 in _): m = max(m, reduce(mul, _, 1))
# 		if (not 0 in _) and (_.count(9)>1): m = max(m, reduce(mul, _, 1))
# 	return m
# 1m >> 630µ > 580µ




arr = [int(_) for _ in """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace('\n','')]


main(arr, 13)

