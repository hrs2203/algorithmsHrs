def mul(a, b, m):
	val = a*b
	if (val <= m):
		return val
	else:
		raise ValueError("multiplication of "+str(a)+" and "+str(b)+" with bound "+str(m)+" not possible")

def main():
	n = int(input())
	for _ in range(n):
		[a, b, m] = list(map(int, str(input()).split() ) )
		try:
			print(mul(a,b,m))
		except ValueError as e:
			print(e.args[0])

if __name__ == '__main__':
	main()