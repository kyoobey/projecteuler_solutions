
def timer(f):
	from time import time
	def wrapper(*a):
		s = time()
		f(*a)
		s = f'{time() - s}'.split('.')
		print(f"{s[0]}s {s[1][:3]}m {s[1][3:6]}µ {s[1][6:9]}n")
	return wrapper
