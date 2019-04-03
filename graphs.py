class Graph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict

    def display_vertices(self):
        return list(self.graph_dict.keys())

    def display_edges(self):
        edges = []
        for vrtx in self.graph_dict:
            for pairVrtx in self.graph_dict[vrtx]:
                if {vrtx, pairVrtx} not in edges:
                    edges.append({pairVrtx, vrtx})
        return edges

    def add_vertex(self, vrtx):
        if vrtx not in self.graph_dict:
            self.graph_dict[vrtx] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.graph_dict:
            self.graph_dict[vrtx1].append(vrtx2)
        else:
            self.graph_dict[vrtx1] = [vrtx2]
        if vrtx2 in self.graph_dict:
            self.graph_dict[vrtx2].append(vrtx1)
        else:
            self.graph_dict[vrtx2] = [vrtx1]


graph_dict = { 'a' : ['b', 'c'],
               'b' : ['a', 'd'],
               'c' : ['a', 'd'],
               'd' : ['e'],
               'e' : ['d']
             }


g = Graph(graph_dict)

print(g.display_vertices())

print(g.display_edges())

g.add_vertex('f')
g.add_edge({'a', 'e'})
g.add_edge({'f', 'e'})
g.add_edge({'b', 'f'})

print(g.display_vertices())

print(g.display_edges())

print(g.graph_dict)

