# Dijkstra's Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(|E| + |V|log|V|)
# python python dijkstra.py 6 "[1,2,3],[2,2,1],[3,1,4],[1,6,99],[2,3,1],[3,4,5],[4,5,1],[5,6,14],[2,6,1]" 1 6

# imports
import sys

# dijsktra's algorithm
def dijkstra(fromNode, toNode, adjMatrix):
	numNodes = len(adjMatrix)
	dist = [[sys.maxint, []]] * numNodes
	visited = [0] * numNodes
	for i in range(0, len(adjMatrix))
		bestPathTo[i]
	return []

def dijsktraRecurse(currentNode, currentPath, visit, dist, adjMatrix):


# converts the string into an adjacency matrix
def stringToAdjMatrix(totalNodes, strList):
	adjList = [[0] * totalNodes for _ in range(0, totalNodes)]
	strList = strList.replace(" ", "")
	splitString = strList.split("],[")
	for tuple in splitString:
		tuple = tuple.replace("[", "")
		tuple = tuple.replace("]", "")
		tupleList = tuple.split(",")
		adjList[int(tupleList[0]) - 1][int(tupleList[1]) - 1] = int(tupleList[2])
	return adjList

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nDijkstra's Algorithm by William M Mortl")
		print("Usage: python dijkstra.py {total edges} \"{[from node, to node, weight], [fn2, tn2, w2], ...}\" {from node} {to node}")
		print("Example: python dijkstra.py 6 \"[1,2,3],[2,2,1],[3,1,4],[1,6,99],[2,3,1],[3,4,5],[4,5,1],[5,6,14],[2,6,1]\" 1 6\r\n")
	else:
		adjMatrix = stringToAdjMatrix(int(sys.argv[1]), sys.argv[2])
		fromNode = int(sys.argv[3])
		toNode = int(sys.argv[4])
		print(("\r\nLooking for the shortest path between nodes: %s and %s") % (str(fromNode), str(toNode)))
		shortestPath = dijkstra(fromNode, toNode, adjMatrix)
		print(("Shortest path\r\n%s\r\n") % str(shortestPath))