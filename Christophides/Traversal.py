import copy

from Christophides.Graph import Graph
from Christophides.MultiGraph import MultiGraph
from Christophides.Vertex import Vertex


class Traversal:
    graph: Graph
    multiGraph: MultiGraph
    numberOfVisitsVertex: list
    vertexList: list


    def __init__(self, graph, multiGraph):
        self.graph = graph
        self.multiGraph = multiGraph
        self.numberOfVisitsVertex = [0] * (graph.countVertex() + 1)
        self.vertexList = list()

    def build(self):
        self.findEulerPath()
        self.findTraversal()


    def findEulerPath(self):
        sourceMultiGraph = copy.deepcopy(self.multiGraph.vertexList)

        startVertex = self.multiGraph.oddVertex
        if startVertex is None:
            startVertex = self.multiGraph.vertexList[0]

        s = [startVertex]
        while len(s) > 0:
            vertex = s.pop()
            self.numberOfVisitsVertex[vertex.numberVertex] += 1

            if (vertex.deg() == 0):
                return

            edge = vertex.edgeList[0]

            s.append(sourceMultiGraph[edge.vertex - 1])

            sourceMultiGraph[vertex.numberVertex - 1].deleteEdge(edge)

            reversedEdge = Vertex.Edge(vertex.numberVertex, edge.weight)
            sourceMultiGraph[edge.vertex - 1].deleteEdge(reversedEdge)

            sourceMultiGraph.append(Vertex(vertex.numberVertex, [edge]))
            self.vertexList.append(Vertex(vertex.numberVertex, [edge]))


    def findTraversal(self):
        flag = True
        for i in range(1, len(self.numberOfVisitsVertex) - 1):
            if self.numberOfVisitsVertex[i] > 1:
                self.deleteRepeatVertex(self.multiGraph.vertexList[i - 1])
                flag = False
        return flag

    def deleteRepeatVertex(self, vertex):
        firstVertex = self.graph.vertexList[0]
        for edge in vertex.edgeList:
            if Vertex(edge.vertex) == self.multiGraph.oddVertex:
                firstVertex = self.graph.vertexList[self.multiGraph.oddVertex.numberVertex - 1]
                break
            else:
                firstVertex = self.graph.vertexList[edge.vertex - 1]

        secondVertex = None
        deletingEdge = None
        for edge in vertex.edgeList:
            if firstVertex.existsEdgeToVertex(edge.vertex):
                secondVertex = self.graph.vertexList[edge.vertex - 1]
                deletingEdge = edge
                break

        vertex.deleteEdge(deletingEdge)
        self.multiGraph.vertexList[deletingEdge.vertex - 1].deleteEdge(Vertex.Edge(vertex.numberVertex, deletingEdge.weight))

        addingEdge = None
        for edge in secondVertex.edgeList:
            if edge.vertex == firstVertex.numberVertex:
                addingEdge = edge
                break

        self.multiGraph.vertexList[secondVertex.numberVertex - 1].appendEdge(addingEdge)

        reversedEdge = Vertex.Edge(secondVertex.numberVertex, addingEdge.weight)
        self.multiGraph.vertexList[firstVertex.numberVertex - 1].appendEdge(reversedEdge)
