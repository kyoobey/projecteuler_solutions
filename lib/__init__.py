from time import time

def timer(f):
	def wrapper(*a):
		s = time()
		o = f(*a)
		s = f"{time()-s:.24f}".split('.')
		print(f"output: {o}")
		print(f"{s[0]}s {s[1][:3]}m {s[1][3:6]}µ {s[1][6:9]}n")
	return wrapper
