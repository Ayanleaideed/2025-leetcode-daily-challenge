'''
Problem Description:
The problem is to find the optimal way to organize flight routes in order to minimize the total flight distance. We are provided with a list of flight routes, and each route is represented as a 3-tuple containing departure city ID, destination city ID, and the distance between two cities.

Solution Approach:
The optimal way to solve this problem is by using the Dijkstra’s Algorithm. The algorithm creates a tree of shortest paths from the starting vertex, the source, to all other points in the graph. We utilize an adjacency list to record the city connection and distance relationship, then apply Dijkstra’s algorithm to find shortest distances from one city to other cities.

Complexity Analysis:
- Time: O(N^2), where N is number of routes. We need to traverse through all routes to build adjacency list and apply Dijkstra’s algorithm
- Space: O(N), where N is number of routes. The maximum space is taken by the distances variable and adj dict.


'''

from typing import List, Tuple
from collections import defaultdict
import heapq

def optimizeRoutes(flightRoutes: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    This function receives a list of flight routes and returns a list of routes that form the shortest 
    path across all cities.
    Args: flightRoutes: list of tuples. Each tuple contains the origin city Id, destination city Id and distance.
    Returns: Optimal sequence of routes. 
    """
    # Step1: Use dictionary to record flight routes as adjacency list 
    adj = defaultdict(list)
    for start, end, weight in flightRoutes:
        adj[start].append((end, weight))
        adj[end].append((start, weight))

    # Step2: Apply Dijkstra’s to find shortest distances from one city to all other cities
    start_city = flightRoutes[0][0]
    distances = {city: float('infinity') for city in adj}
    distances[start_city] = 0

    priority_queue = [(0, start_city, None)]
    prev_city = {start_city: None}
    while priority_queue:
        curr_distance, curr_city, from_city = heapq.heappop(priority_queue)
        if curr_distance != distances[curr_city]:
            continue
        if from_city is not None:
            if (from_city, curr_city, curr_distance) not in flightRoutes:
                flightRoutes.remove((curr_city, from_city, curr_distance))
            else:
                flightRoutes.remove((from_city, curr_city, curr_distance))
            flightRoutes.append((from_city, curr_city, curr_distance))
        for neighbor, weight in adj[curr_city]:
            distance = distances[curr_city] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor, curr_city))
                prev_city[neighbor] = curr_city
                
    return flightRoutes
