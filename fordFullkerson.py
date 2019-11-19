def printAdj(adjMatrix,nodes):
	for i in range(nodes):
		print(i , end=" ")
		print(adjMatrix[i])
	print(" ")

def residualPath(adjMatrix,nodes):
	# implimented using BFS somewhat
	path = []
	for _ in range(nodes):
		path.append(list())

	dist = [-1]*nodes

	dist[0] = 0
	queue = list()
	queue.append(0)	# default starting point
	while(len(queue)!=0):
		d = queue.pop()
		for i in range(nodes):
			if ((adjMatrix[d][i]!=0) and (dist[i]==-1)):
				queue.insert(0,i)
				dist[i] = dist[d]+1
				# creating path for each node
				path[i].extend( path[d] )
				path[i].append(d)
	for i in range(nodes):
		path[i].append(i)
	
	destination = nodes-1
	# shortest path from sourde to destination
	if path[destination][0]==0 and path[destination][-1]==destination:
		return path[destination]
	else:
		return -1

def findMaxCap(residualGraph,path):
	cap = 2e8
	for i in range( len(path)-1 ):
		d = residualGraph[ path[i] ][ path[i+1] ]
		if ( d!=0 and d< cap ):
			cap = d
	return cap

def fordFullkerson(adjMatrix,nodes):
	residualGraph = adjMatrix
	source = 0
	dest = nodes-1

	flowCap = 0
	
	path = residualPath(residualGraph,nodes)

	while(path!=-1):
		cap = findMaxCap(residualGraph,path)
		flowCap+=cap
		# change the residual graph
		for i in range(len(path)-1):
			start = path[i]
			end = path[i+1]
			residualGraph[start][end] -= cap
			residualGraph[end][start] += cap

		# printAdj(residualGraph,nodes)

		# check for path again
		path = residualPath(residualGraph,nodes)

	return flowCap

def main():
	d = list( map( int, str(input()).split() ) )
	# nodes -> 0 indexed , edges
	nodes = d[0]
	edges = d[1]

	adjMatrix = list()
	for _ in range(nodes):
		adjMatrix.append

	# creating empty nodesXnodes matrix
	for _ in range(nodes):
		d = [0]*nodes
		adjMatrix.append(d)

	for _ in range(edges):
		d = list(map(int,str(input()).split()))
		# source,dest,weight
		adjMatrix[d[0]][d[1]] = d[2]

	printAdj(adjMatrix,nodes)

	print("maxFlow capacity = " ,end=" ")
	print(fordFullkerson(adjMatrix,nodes))

# take input as directed graph
if __name__ == '__main__':
	main()

# 6 10
# 0 1 16
# 0 2 13
# 1 2 10
# 1 3 12
# 2 1 4
# 2 4 14
# 3 2 9
# 4 3 7
# 4 5 4
# 3 5 20