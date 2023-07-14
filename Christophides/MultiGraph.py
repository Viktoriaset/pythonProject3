from Christophides.Vertex import Vertex
from Christophides.SpanningTree import SpanningTree

class MultiGraph:
    PM: list # PerfectMatching
    graph: list
    MST: SpanningTree
    vertexList: list
    oddVertex: Vertex | None

    def __init__(self, graph, MST):
        self.graph = graph
        self.MST = MST
        self.PM = list()
        self.vertexList = list()

    def build(self):
        self.searchPerfectMatching()
        self.unionMstAndPm()
        self.oddVertex = self.findOddVertex()
        sorted(self.vertexList)

    def searchPerfectMatching(self):
        for vertex in self.graph:
            edge = self.searchMinEdge(vertex)

            pair = Vertex(vertex.numberVertex, [edge])
            self.PM.append(pair)

            self.graph.remove(vertex)
            self.graph.remove(Vertex(edge.vertex))

    def searchMinEdge(self, vertex):
        for edge in vertex.edgeList:
            if Vertex(edge.vertex) in self.graph:
                return edge

    def unionMstAndPm(self):
        for pair in self.PM:

            edge = pair.edgeList[0]
            self.MST.vertexList[pair.numberVertex - 1].appendEdge(edge)

            reversedEdge = Vertex.Edge(pair.numberVertex, edge.weight)
            self.MST.vertexList[edge.vertex - 1].appendEdge(reversedEdge)

        self.vertexList = self.MST.vertexList

    def findOddVertex(self):
        vertex = self.vertexList[0]
        for v in self.vertexList:
            if v.deg() % 2 == 1 and vertex.deg() > v.deg():
                vertex = v
        return vertex
