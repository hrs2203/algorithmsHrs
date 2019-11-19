import random

def printConnection(point):
	for i in point:
		print(i[0] , " " , i[1]);
	print(" ")


def kargerAlgo(edges,edge):
	while(edge>1):
		ind = random.randint(0,edge-1)
		pointa = [edges[ind][0]]
		# print(pointa)
		pointb = [edges[ind][1]]
		# print(pointb)

		temp = list()	# newly joined node
		temp.extend(pointa)
		temp.extend(pointb)
		print(temp)
		
		# finding all connetions of the randomly chosen graph
		# and changing them to with new connections

		newConnection = list()
		for i in edges:
			if ( i[0]==pointa and i[1]==pointb ):
				pass
			elif( i[0]==pointa or i[0]==pointb ):
				newConnection.append( temp,i[1] )
			elif( i[1]==pointa or i[1]==pointb ):
				newConnection.append( i[0],temp )
			else:
				newConnection.append(i)

		printConnection(newConnection)

		edges = newConnection
		edge -= 1

	return edges



def main():
	d = list( map( int, str(input()).split() ) )
	# nodes -> 0 indexed , edge
	node = d[0]
	edge = d[1]

	edges = list()

	# storing edges only
	for _ in range(edge):
		d = list(map(int,str(input()).split()))
		# a b
		edges.append(d)
	# printConnection(edges)

	data = kargerAlgo(edges,edge)
	printConnection(data)

	
if __name__ == '__main__':
	main()