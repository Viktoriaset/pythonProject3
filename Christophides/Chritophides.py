import copy

from Christophides.Graph import Graph
from Christophides.SpanningTree import SpanningTree
from Christophides.MultiGraph import MultiGraph
from Christophides.Traversal import Traversal


class Christophides:
    filePath: str
    traversal: list
    weight: int = 0

    def __init__(self, filePath):
        self.filePath = filePath
        self.traversal = list()

    def findTraversal(self):
        graph = Graph()
        graph.parseFileWithInputData(self.filePath)

        tree = SpanningTree(copy.deepcopy(graph))
        tree.build()

        oddVertex = list()

        for vertex in tree.vertexList:
            if len(vertex.edgeList) % 2 != 0:
                oddVertex.append(vertex)

        subGraph = graph.createSubGraph(oddVertex)

        multiGraph = MultiGraph(subGraph, tree)
        multiGraph.build()

        traversalt = Traversal(graph, multiGraph)
        traversalt.build()

        for vertex in traversalt.vertexList:
            self.traversal.append(vertex.numberVertex)
            self.weight += vertex.edgeList[0].weight
