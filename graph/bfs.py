class Graph:
    def __init__(self) -> None:
        self.mydict = {}

    def __setattr__(self, __name: int, __value: int) -> None:
        pass

    def add(self, vertex, co_vertex):
        '''Its important to add two way relationsip between vertex & co-vertex'''
        if self.mydict.get(vertex):
            myset = self.mydict.get(vertex)
            myset.add(co_vertex)
            self.mydict[vertex] = myset
        else:
            self.mydict[vertex] = {co_vertex, }

        # This is alterate 1 line implementation o above code
        # self.mydict[vertex] = {co_vertex, }.union(self.mydict.get(vertex) or set())

        # make a complement of vertex
        if self.mydict.get(co_vertex):
            myset = self.mydict.get(co_vertex)
            myset.add(vertex)
            self.mydict[co_vertex] = myset
        else:
            self.mydict[co_vertex] = {vertex, }

    def __repr__(self) -> str:
        return f'{self.mydict}'

    
class BFS:
    def __init__(self) -> None:
        self.myqueue = []
        self.visited = []

    def search(self, graph:Graph, vertex):
        self.myqueue.extend(graph.mydict[vertex])
        self.visited.append(vertex)

        while len(self.myqueue) != 0:
            popped = self.myqueue.pop(0)
            if popped not in self.visited:
                self.myqueue.extend(graph.mydict[popped])
                self.visited.append(popped)

        print(self.visited)



if __name__ == '__main__':
    graph = Graph()
    graph.add(0, 1)
    graph.add(0, 2)
    graph.add(0, 3)
    graph.add(1, 2)
    graph.add(1, 0)
    graph.add(2, 4)

    print(graph)

    bfs = BFS()
    bfs.search(graph, 1)
