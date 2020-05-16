def main():
	[s ,n] = list(map(int , str(input()).split() ))
	s += s%2
	for i in range(n):
		print(s, end=" ")
		s+=2
	print()

if __name__ == '__main__':
	main()