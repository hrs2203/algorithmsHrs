def main():
	s = str(input())
	l = set(['a','e','i','o','u'])
	r = ""
	v = ""
	for i in s:
		if i not in l:
			r+=i
		else:
			v+=i
	print(r)
	print(v)

if __name__ == '__main__':
	main()