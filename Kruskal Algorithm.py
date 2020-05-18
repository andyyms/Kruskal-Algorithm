class Kruskal:
    def SortEdgeByWeight(self, u, v, w, index=0):
        while index < len(w):
            if index >= 1:
                if w[index] < w[index - 1]:
                    w[index], w[index - 1] = w[index - 1], w[index]
                    u[index], u[index - 1] = u[index - 1], u[index]
                    v[index], v[index - 1] = v[index - 1], v[index]
                    return self.SortEdgeByWeight(u, v, w, index - 1)
            index = index + 1


    def createGraph(self, u ,v, w):
        self.SortEdgeByWeight(u, v, w)
        graph = {}
        set = list(zip(u, v))
        for i, val in enumerate(set):
            graph[val] = w[i]
        return graph


    def FindMST(self, graph):
        MST = []
        Parent = []
        for edge, weight in graph.items():
            if not all(elem in Parent for elem in edge):
                for n in edge:
                    if not n in Parent:
                        Parent.append(n)
                MST.append(edge)
        return MST

    def TotalWeightofMST(self, graph, mst):
        weight = 0
        for item in mst:
            weight += graph.get(item)
        return weight


# Test Program
u = [1, 1, 4, 2, 3, 3]
v = [2, 3, 1, 4, 2, 4]
w = [5, 3, 6, 7, 4, 5]

kruskal = Kruskal()
graph = kruskal.createGraph(u, v, w)
print(graph)
# {(1, 3): 3, (3, 2): 4, (1, 2): 5, (3, 4): 5, (4, 1): 6, (2, 4): 7}

mst = kruskal.FindMST(graph)
print(mst)
# [(1, 3), (3, 2), (3, 4)]

mst_weight = kruskal.TotalWeightofMST(graph, mst)
print(mst_weight)
# 12