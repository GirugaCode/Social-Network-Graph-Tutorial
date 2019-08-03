#!python3

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""
class Vertex:

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
        #  check if vertex is already a neighbor
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
            # print("weight:", weight)
        #  if not, add vertex to neighbors and assign weight.

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjacent to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        #  return the neighbors
        return self.neighbors

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        #  return the weight of the edge from this
        # vertext to the given vertex.
        return self.neighbors[vertex]