#!python3

import argparse
from graphs.graph import Graph
from utils.read_file import read_file

def main(text_file):
    '''
    Generate a graph from a file
    text_file -> name of file to open with graph data
    '''
    # Challenge 1: Output the vertices & edges
    graph, verts, edges = read_file(text_file)

    # Adds all the vertexes to Graph
    for vertex in verts:
        graph.add_vertex(vertex)

    # Adds all undirectional edges to Graph
    for edge in edges:
        graph.add_edge(edge[0], edge[1]) 

    print("Challenge One --------------------")
    print(f"Verticies:{verts}")
    print("Edges:")
    for fromVert, toVert in edges:
        print(f"({fromVert}, {toVert})")

    print("Challenge Two -------------------")
    for neighbor in graph.vert_dict:
        print("Neighbors:", graph.vert_dict[neighbor])

    print("Challenge Three -------------------")
    print(graph.breadth_first_search("Ryan"))

    print("Challenge Four ---------------------")
    print(graph.find_path("Eddie", "Ruhsane"))

    print("Challenge Five ---------------------")
    print(graph.find_shortest_path("Eddie", "Ruhsane"))

    print("Challenge Six ----------------------")
    print(graph.clique())
    return graph

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename)
            
