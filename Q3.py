class customList:
	def __init__(self):
		self.data = list()
	def append(self, num):
		while(len(self.data)>0 and self.data[-1]>num):
			self.data = self.data[:-1]
		self.data.append(num)

	def pop(self):
		self.data = self.data[:-1]
	def __len__(self):
		return len(self.data)

def main():
	samp = customList()
	q = int(input())
	for _ in range(q):
		inp = str(input()).split()
		if (inp[0] == 'size'):
			print( samp.__len__() )
		elif (inp[0] == 'append'):
			num = int(inp[1])
			samp.append(num)
		else:
			samp.pop()

if __name__ == '__main__':
	main()