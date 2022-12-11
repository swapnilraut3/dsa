# You can use adjacency list or set 
# mygraph = {
#     0: [1, 2, 3],
#     1: [1, 2],
#     2: [0, 1],
#     3: [0]
# }

class Graph:
    def __init__(self) -> None:
        self.mydict = {}

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


if __name__ == "__main__":
    mygraph = Graph()
    mygraph.add(0, 1)
    mygraph.add(1, 2)
    mygraph.add(1, 3)
    print(mygraph)
