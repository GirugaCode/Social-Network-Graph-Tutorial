""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""
from graphs.vertex import Vertex
from data_structures.queue import LinkedQueue
class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vert_dict = {}
        self.num_verticies = 0
        self.num_edges = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        #  increment the number of vertices
        self.num_verticies += 1
        #  create a new vertex
        new_vertex = Vertex(key)
        #  add the new vertex to the vertex list
        self.vert_dict[key] = new_vertex
        #  return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """return the vertex if it exists"""
        #  return the vertex if it is in the graph
        if key in self.vert_dict:
            return self.vert_dict[key]

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        #  if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if f not in self.vert_dict:
            self.add_vertex(f)
        if t not in self.vert_dict:
            self.add_vertex(t)
        #  if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the add_neighbor method of the Vertex class.
        self.vert_dict[f].add_neighbor(self.vert_dict[t], weight=2)
        self.vert_dict[t].add_neighbor(self.vert_dict[f], weight=2)
        self.num_edges += 1
        
    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.keys()

    def get_edges(self, vertex):
        dict_edges = self.vert_dict[vertex].neighbors
        return dict_edges

    def breadth_first_search(self, start_vertex):
        # Stores all the vertexes visited in a set
        visited = set()
        # Using Queues to traverse through the graph
        queue = LinkedQueue()
        queue.enqueue(start_vertex)

        levels = {}
        levels[start_vertex] = 0

        while not queue.is_empty(): # Loop as long as the queue contains verticies 
            vertex = queue.dequeue() # Dequeue the vertex
            for neighbor in self.vert_dict[vertex].neighbors: # Iterating through the dictionary of neighbors 
                if neighbor.id not in visited: # Check all neighbors if they are not visited
                    queue.enqueue(neighbor.id) # Enqueue the neighbors id that are not in visited
                    visited.add(neighbor.id) # Add the neighbor that is not in visited

                    levels[neighbor.id] = levels[vertex] + 1
        print("Levels:", levels)
        return visited

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())

