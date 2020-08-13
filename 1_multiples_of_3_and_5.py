#!/usr/bin/python3.7



from lib import *



@timer
def main(l):
	l-=1
	m1, m2, m3 = l//3, l//5, l//15
	return (3*m1*(m1+1) + 5*m2*(m2+1) - 15*m3*(m3+1)) //2
# ~3µ




# @timer
# def main(l):
# 	def series_multiples_of(n):
# 		p = (l-1)//n
# 		return n*p*(p+1)*0.5
# 	return series_multiples_of(3) + series_multiples_of(5) - series_multiples_of(15)
# ~4µ


# @timer
# def main(n):
# 	sum=0
# 	for i in range(n):
# 		if i%3<1 or i%5<1: sum+=i
# 	print(sum)
# ~200µ runtime






main(1000)



