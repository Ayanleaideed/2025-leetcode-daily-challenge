'''
Problem:
In a given undirected and weighted graph, I have to find the shortest path from a specific starting point to every other vertex in the graph.

Approach:
This problem can be solved using Dijkstra's algorithm. We initialize the distance to the starting vertex as 0 and to all other vertices as infinity. Then, for each unvisited vertex, we select the vertex with the least distance and update the distances to its neighbors. The procedure is repeated until all the vertices are visited.

Complexity:
- Time: O(V + ElogE)
- Space: O(V)
'''

import heapq

def shortest_path(graph, start):
    # The heap data structure (priority queue) to keep track of
    # vertices with the least distance
    heap_data = [(0, start)]
    # A dictionary to maintain the shortest distance to all vertices
    least_distances = {vertex: float('infinity') for vertex in graph}
    least_distances[start] = 0
    # A dictionary to maintain the parent node of each vertex
    parent = {start: None}

    while heap_data:
        (dist, curr_vertex) = heapq.heappop(heap_data)

        # Proceed further only if the popped vertex isn't processed
        if dist != least_distances[curr_vertex]:
            continue

        for neighbor, weight in graph[curr_vertex].items():
            old_distance = least_distances[curr_vertex]
            new_distance = old_distance + weight

            # If the new distance is less than the current least, update it
            if new_distance < least_distances[neighbor]:
                least_distances[neighbor] = new_distance
                heapq.heappush(heap_data, (new_distance, neighbor))
                parent[neighbor] = curr_vertex

    # Return the shortest distances and the path to all vertices
    return least_distances, parent