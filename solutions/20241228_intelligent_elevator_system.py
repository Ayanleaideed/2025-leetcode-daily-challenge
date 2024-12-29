#Author: Ayanle 
#Data: Datetime.now()
'''
Problem Description:
The task is to calculate the minimum total time required to transport all passengers in an intelligent elevator system. The elevator moves at a speed of one floor per second, and people take 1 second to board or exit the elevator. Multiple people can board or exit concurrently.

Solution Approach:
The problem can be solved using a greedy approach. We first sort the list of passengers based on their start floors. Then, for each passenger in the sorted list, if the elevator is currently above the passenger's start floor, it travels down to that floor in |current - start| seconds. If the elevator is currently below the start floor, it travels to that floor in the same amount of time. The passenger then boards the elevator, taking 1 second. Finally, the elevator takes the passenger to their destination floor in |start - end| seconds.

The time complexity of this solution is determined by the sorting operation. In Python, the `sorted` function uses a variant of the Timsort algorithm whose worst-case time complexity is O(n log n). Therefore, the overall time complexity of this solution is O(n log n).

The space complexity of this solution is O(n), arising from the storage of the passenger list.

---

def minElevatorTime(n, passengers):
    """
    Function to calculate the minimum total time to transport all passengers in an intelligent elevator system.
    Args: 
    - n: An integer representing the number of floors.
    - passengers: A list of lists, where each inner list contains two integers representing the start and end floors of a passenger.
    
    Returns: 
    - An integer representing the minimum total time to transport all passengers.
    """

    # Sort the passengers based on their start floors
    passengers = sorted(passengers)

    total_time = 0
    current_floor = 0

    for passenger in passengers:
        start, end = passenger

        # Elevator travels to the start floor
        total_time += abs(current_floor - start) 

        # Passenger boards the elevator
        total_time += 1 

        # Elevator travels to the end floor
        total_time += abs(start - end) 

        # Passenger exits the elevator
        total_time += 1

        # Update the current floor of the elevator
        current_floor = end 

    return total_time
'''
