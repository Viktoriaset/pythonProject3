from Christophides.Vertex import Vertex


class Graph:
    vertexList: list = list()

    def countVertex(self):
        return len(self.vertexList)

    def createSubGraph(self, vertexes):
        answer = list()
        for vertex in self.vertexList:
            if vertex in vertexes:
                newVertex = Vertex(vertex.numberVertex, [])
                for edge in vertex.edgeList:
                    if Vertex(edge.vertex, []) in vertexes:
                        newVertex.appendEdge(edge)
                answer.append(newVertex)
        return answer

    def parseFileWithInputData(self, fileWithInputData):
        with open(fileWithInputData, 'r') as f:
            lines = f.readlines()
            for line in lines:
                edgeData = line.split()
                edge = []
                for data in edgeData:
                    edge.append(int(data))
                self.saveEdge(edge)

        self.sortVertexes()

    def saveEdge(self, edgeData):
        firstVertex = Vertex(edgeData[0], [Vertex.Edge(edgeData[1], edgeData[2])])
        secondVertex = Vertex(edgeData[1], [Vertex.Edge(edgeData[0], edgeData[2])])

        self.saveVertex(firstVertex)
        self.saveVertex(secondVertex)

    def saveVertex(self, vertex):
        if vertex not in self.vertexList:
            self.vertexList.append(vertex)
        else:
            self.vertexList[self.vertexList.index(vertex)].appendEdge(vertex.edgeList[0])

    def sortVertexes(self):
        self.vertexList = sorted(self.vertexList)

        for vertex in self.vertexList:
            vertex.edgeList = sorted(vertex.edgeList)


