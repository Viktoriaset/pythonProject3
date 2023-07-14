from Christophides.Graph import Graph
from Christophides.Vertex import Vertex


class SpanningTree:

    sourceGraph: Graph

    # вершины и ребра оставного дерева
    vertexList: list = list()

    vertexesForAlgPrima: list = list()

    def __init__(self, graph):
        self.sourceGraph = graph
        for i in range(1, self.sourceGraph.countVertex() + 1):
            self.vertexList.append(Vertex(i, []))

    def build(self):
        self.prima_cicle()
        self.addReverseEdges()
        self.vertexList = sorted(self.vertexList)

    def prima_cicle(self):
        vertex = self.sourceGraph.vertexList[0]
        self.vertexesForAlgPrima.append(vertex)

        while len(self.vertexesForAlgPrima) < self.sourceGraph.countVertex():
            vertexFrom, minEdge = self.findMinEdgeAndNextVertex()

            self.vertexList[vertexFrom.numberVertex - 1].appendEdge(minEdge)

            self.vertexesForAlgPrima.append(self.sourceGraph.vertexList[minEdge.vertex - 1])


    def prima(self, index=0, edge=None):
        vertex: Vertex = self.sourceGraph.vertexList[index]

        self.vertexesForAlgPrima.append(vertex)

        if edge is not None:
            self.vertexesForAlgPrima[-1].deleteEdge(edge)

        if self.countSumEdges() == self.sourceGraph.countVertex() - 1:
            return

        nextVertex, minEdge = self.findMinEdgeAndNextVertex()

        self.vertexList[nextVertex.numberVertex - 1].appendEdge(minEdge)

        self.vertexesForAlgPrima[-1].deleteEdge(minEdge)

        reverseEdge = Vertex.Edge(index + 1, minEdge.weight)
        self.prima(minEdge.vertex - 1, reverseEdge)

    def countSumEdges(self):
        ans = 0
        for vertex in self.vertexList:
            ans += len(vertex.edgeList)
        return ans

    def findMinEdgeAndNextVertex(self):
        vertexFrom = None
        minEdge = Vertex.Edge(0, 1000000)

        for i in range(0, len(self.vertexesForAlgPrima)):
            flag = False
            vertex = self.vertexesForAlgPrima[i]
            for edge in vertex.edgeList:
                if edge < minEdge and Vertex(edge.vertex) not in self.vertexesForAlgPrima:
                    vertexFrom = vertex
                    minEdge = edge

        return [vertexFrom, minEdge]

    def searchVertex(self, vertex):
        for v in self.vertexesForAlgPrima:
            if v.numberVertex == vertex:
                return True
        return False

    def addReverseEdges(self):
        for vertex in self.vertexList:
            for edge in vertex.edgeList:
                self.vertexList[edge.vertex - 1].appendEdge(Vertex.Edge(vertex.numberVertex, edge.weight))
