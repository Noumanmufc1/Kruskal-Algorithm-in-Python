class Kruskal:
    fathers, edges, mst = [], [], []
    noOfEdges, noOfVertices, mstEdges, mstWeight, mstNi = 0, 0, 0, 0, 0
    
    def find(self, x):
        if(self.fathers[x] == x):
            return x;
        return (self.find(self.fathers[x]))
    
    def unite(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        self.fathers[fx] =  fy
        
    def __init__(self):
        for i in range(100):
            self.fathers.append(i)
            
    def verEdges(self):
        while(True):
            try:
                self.noOfEdges = int(input("Enter the number of edges: "))
                self.noOfVertices = int(input("Enter the number of vertices: "))
                break
            except:
                print("Invalid Input. Try again")
                continue
        
    def takeInput(self):
        count = 0
        while(count < self.noOfEdges):
            try:
                edge1 = int(input("Enter vertex 1 of edge {}: ".format(count + 1)))
                edge2 = int(input("Enter vertex 2 of edge {}: ".format(count + 1)))
                weight = int(input("Enter the weight between vertex number {} and vertex number {}: ".format(edge1, edge2)))
                self.edges.append([weight,[edge1, edge2]])
                count += 1
            except:
                print("Invalid Input. Try again")
                continue
            
    def sort(self):
        for i in range(len(self.edges)):
            maxWeight = self.edges[0][0]
            index = 0
            for j in range(len(self.edges) - i):
                if (maxWeight < self.edges[j][0]):
                    maxWeight = self.edges[j][0]
                    index = j
            temp = self.edges[index]
            self.edges[index] = self.edges[self.noOfEdges - (i + 1)]
            self.edges[self.noOfEdges - (i + 1)] = temp
    
    def createMST(self):
        while(self.mstEdges < self.noOfVertices - 1 and self.mstNi < self.noOfEdges):
            a = self.edges[self.mstNi][1][0]
            b = self.edges[self.mstNi][1][1]
            w = self.edges[self.mstNi][0]
            if(self.find(a) != self.find(b)):
                self.unite(a, b)
                self.mstWeight += w
                self.mstEdges += 1
                self.mst.append(self.edges[self.mstNi])
            self.mstNi += 1
            
    def printMST(self):
        for i in range(self.mstEdges):
            print("Edge between Vertex {} and Vertex {}. Weight = {}".format(self.mst[i][1][0], self.mst[i][1][1], self.mst[i][0]))
        print("The total weight of the minimum spanning tree is {}".format(self.mstWeight))
        
    def printAllEdges(self):
        for i in range(self.noOfEdges):
            print("Edge between Vertex {} and Vertex {}. Weight = {}".format(self.edges[i][1][0], self.edges[i][1][1], self.edges[i][0]))   
    
             
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        