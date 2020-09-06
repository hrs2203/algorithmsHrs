def flipNeeded(n, mat):
	return (n>0) and (mat[n-1][n] != mat[n][n]-4) and (mat[n][n-1] != mat[n][n]-1)


def flipOperation(mat, l):
	for x in range(l):
		for y in range(x+1,l):
			temp = mat[x][y]
			mat[x][y] = mat[y][x]
			mat[y][x] = temp


w = int(input())

for _ in range(w):
	n = int(input())
	mat = []
	final = []

	for i in range(n):
		temp = list(map(int, str(input()).split()))
		mat.append(temp)
		final.append( [ 1+d+(4*i) for d in range(n) ] )

	count = 0


	for i in range(n-1, 0, -1):
		if (flipNeeded(i, mat)):
			flipOperation(mat, i)
			count+=1

	print(count)

