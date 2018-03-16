from kruskal import  *

def test_kruskal():
	class kruskal_test(Kruskal):
		noOfEdges = 9
		noOfVertices = 7
		edges = [[4, [1, 2]], [2, [7, 2]], [3, [6, 2]], [1, [6, 5]], [20, [5, 3]], [6, [4, 3]], [7, [1, 4]], [2, [2, 5]], [1, [2, 3]]]
	a_test = kruskal_test()
	a_test.sort()
	a_test.createMST()
	# no of edges and weight of mst is already calculated for checking
	assert a_test.mstWeight == 16
	assert a_test.mstEdges == 6
	
test_kruskal()