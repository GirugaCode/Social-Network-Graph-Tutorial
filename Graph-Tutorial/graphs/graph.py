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

    def find_path(self, to_vert, from_vert):
        """
        Finds the shortest path between two vertexes

        Credit: Vincenzo Marcella (@C3NZ)
        for helping me out with the code and logic to find the shortest path

        Args:
        from_vert -> Starting Vertex
        to_vert -> Ending Vertex
        
        Returns:
        A list of verticies the from_vert traversed to get to the to_vert
        """

        # Initializes the queue, verticies visited and the current vertex
        queue = LinkedQueue()
        visited = set()
        curr_vertex = self.vert_dict[from_vert]

        # Helps to start finding the path
        path_found = False
        curr_vertex.parent = None
        
        # Enqueues the from_vertex and marks it as visited
        queue.enqueue(curr_vertex)
        visited.add(curr_vertex.id)

        
        while not queue.is_empty():
            curr_vertex = queue.dequeue()
            if curr_vertex.id == to_vert:
                path_found = True
                # break # Breaks out of the while loop once the path is found

            # Traverse through the graph until the from_vertex and to_vertex is found
            for neighbor in curr_vertex.neighbors: 
                if neighbor.id not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor.id)
                    neighbor.parent = curr_vertex

        # Once path_found is true add the shortest one in the list
        if path_found:
            path = []
            while curr_vertex:
                path.append(curr_vertex.id)
                curr_vertex = curr_vertex.parent
            return path[::-1] # Reverse the list because we are traversing backwards

    def find_shortest_path(self, to_vert, from_vert):
        """
        Finds the shortest path between two vertexes

        Credit: Vincenzo Marcella (@C3NZ)
        for helping me out with the code and logic to find the shortest path

        Args:
        from_vert -> Starting Vertex
        to_vert -> Ending Vertex
        
        Returns:
        A list of verticies the from_vert traversed to get to the to_vert
        """

        # Initializes the queue, verticies visited and the current vertex
        queue = LinkedQueue()
        visited = set()
        curr_vertex = self.vert_dict[from_vert]

        # Helps to start finding the path
        path_found = False
        curr_vertex.parent = None
        
        # Enqueues the from_vertex and marks it as visited
        queue.enqueue(curr_vertex)
        visited.add(curr_vertex.id)

        
        while not queue.is_empty():
            curr_vertex = queue.dequeue()
            if curr_vertex.id == to_vert:
                path_found = True
                break # Breaks out of the while loop once the path is found

            # Traverse through the graph until the from_vertex and to_vertex is found
            for neighbor in curr_vertex.neighbors: 
                if neighbor.id not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor.id)
                    neighbor.parent = curr_vertex

        # Once path_found is true add the shortest one in the list
        if path_found:
            path = []
            while curr_vertex:
                path.append(curr_vertex.id)
                curr_vertex = curr_vertex.parent
            return path[::-1] # Reverse the list because we are traversing backwards

    def clique(self):
        
        clique_result = set()
        start_vertex = list(self.vert_dict.keys())[0]
        clique_result.add(start_vertex)

        for vertex in self.vert_dict:
            if vertex not in clique_result:
                if vertex in self.vert_dict[vertex].neighbors:
                    clique_result.add(vertex)
        return clique_result


    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())

