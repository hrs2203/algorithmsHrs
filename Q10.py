mod = 10**9 + 7

def moduleExpo(a, n):
	result = 1
	while (n>0):
		if (n%2):
			result = (result*a) % mod
			n = n-1
		else:
			a = (a**2) % mod
			n = n/2
	return result

def totalPatterns(n):
	a = moduleExpo(24, n)
	b = ((9 * moduleExpo(8, n)) % mod)
	c = ((18 * moduleExpo(3, n)) % mod)
	d = ((9 * moduleExpo(2, n)) % mod)
	result = (a-b+c+d-24+(2*mod))%mod
	return result

def main():
	num = int(input())
	totalCount = totalPatterns( num )
	print(totalCount)

if __name__ == '__main__':
	main()