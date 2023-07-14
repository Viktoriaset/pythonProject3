from dataclasses import dataclass


class Vertex:
    numberVertex: int
    edgeList: list

    def __init__(self, numberVertex, edgeList=[]):
        self.numberVertex = numberVertex
        self.edgeList = edgeList

    def appendEdge(self, edge):
        if edge in self.edgeList:
            return

        self.edgeList.append(edge)

    def deleteEdge(self, edge):
        if self.edgeList.count(edge) > 0:
            self.edgeList.remove(edge)

    def deg(self):
        return len(self.edgeList)

    def existsEdgeToVertex(self, numbberVertex):
        for edge in self.edgeList:
            if edge.vertex == numbberVertex:
                return True
        return False

    def __str__(self):
        return 'vertex:' + str(self.numberVertex) + ' edges:' + str(self.edgeList)

    def __lt__(self, other):
        return self.numberVertex < other.numberVertex

    def __eq__(self, other):
        return self.numberVertex == other.numberVertex

    @dataclass
    class Edge:
        vertex: int
        weight: int

        def __lt__(self, other):
            return self.weight < other.weight

        def __le__(self, other):
            return self.weight <= other.weight

        def __eq__(self, other):
            return self.vertex == other.vertex
