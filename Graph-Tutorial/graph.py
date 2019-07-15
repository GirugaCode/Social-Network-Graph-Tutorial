#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # TODO check if vertex is already a neighbor
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
        # TODO if not, add vertex to neighbors and assign weight.

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        # TODO return the neighbors
        return self.neighbors

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        # TODO return the weight of the edge from this
        # vertext to the given vertex.
        return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vert_list = {}
        self.num_verticies = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # TODO increment the number of vertices
        self.num_verticies += 1
        # TODO create a new vertex
        new_vertex = Vertex(key)
        # TODO add the new vertex to the vertex list
        self.vert_list[key] = new_vertex
        # TODO return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """return the vertex if it exists"""
        # TODO return the vertex if it is in the graph
        if key in self.vert_list:
            return self.vert_list[key]

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if f and t not in self.vert_list:
            self.add_vertex(f)
            self.add_vertex(t)
        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the add_neighbor method of the Vertex class.
        if f and t in self.vert_list:
            self.vert_list[f].add_neighbor(self.vert_list[t], weight=0)
        # Hint: the vertex f is stored in self.vert_list[f].
    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_list.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_list.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Eddie")
    g.add_vertex("Shawn")
    g.add_vertex("Kevin")
    g.add_vertex("Nick")
    g.add_vertex("Tim")
    g.add_vertex("Jian")
    g.add_vertex("Aaron")
    g.add_vertex("Luis")
    g.add_vertex("Ruhsane")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Eddie", "Shawn")
    g.add_edge("Eddie", "Kevin")
    g.add_edge("Eddie", "Nick")
    g.add_edge("Eddie", "Tim")
    g.add_edge("Eddie", "Jian")
    g.add_edge("Shawn", "Kevin")
    g.add_edge("Shawn", "Nick")
    g.add_edge("Shawn", "Jian")
    g.add_edge("Shawn", "Nick")
    g.add_edge("Kevin", "Nick")
    g.add_edge("Kevin", "Jian")
    g.add_edge("Kevin", "Tim")
    g.add_edge("Nick", "Tim")
    g.add_edge("Nick", "Jian")
    g.add_edge("Tim", "Ruhsane")
    g.add_edge("Luis", "Aaron")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g:
        # print(v)
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
