"""
Stanford Algorithms - Course 4 Week 3
Programming Assignment

Solution by Alexandria O'Mara

TASK
In this assignment we will revisit an old friend, the traveling salesman problem
(TSP). This week you will implement a heuristic for the TSP, rather than an
exact algorithm, and as a result will be able to handle much larger problem
sizes.

This file (nn.txt) describes a TSP instance with the structure:
[number of cities]
[city 1 index] [city 1 x coordinate] [city 1 y coordinate]
[city 2 index] [city 2 x coordinate] [city 2 y coordinate]
...

You should implement the nearest neighbor heuristic:
    1. Start the tour at the first city.
    2. Repeatedly visit the closest city that the tour hasn't visited yet. In
       case of a tie, go to the closest city with the lowest index.
    3. Once every city has been visited exactly once, return to the first city.

Find the cost of the traveling salesman tour computed by the nearest neighbor
heuristic for this instance, rounded down to the nearest integer.

NOTE: The distance between two cities is defined as the Euclidean distance, and
      the Euclidean square is defined as the Euclidean distance without the
      square root function applied.
"""


import sys
import math


def get_maximum_city_index(file_name):
    """ Uses file_name to retrieve the number of cities.
    """
    with open(file_name) as file:
        for line in file:
            max_city_index = int((line.split())[0])
            return max_city_index


def calculate_euclidean_square(x_1, x_2, y_1, y_2):
    """ Uses x and y coordinates to find the euclidean square.
    """
    
    squared_x = (x_1 - x_2) ** 2
    squared_y = (y_1 - y_2) ** 2
    euclidean_square = squared_x + squared_y
    return euclidean_square


def create_visited_cities_list(max_cities):
    """ Creates array to keep track of visited cities.
    """

    visited_list = [True]
    for i in range(max_cities):
        visited_list.append(False)
    return visited_list


def get_city_coordinates(file_name):
    """ Uses file_name to get all x and y coordinates of all cities.
    Returns 2 arrays: x coordinates and y coordinates.
    """
    
    x_coords = [None]
    y_coords = [None]
    with open(file_name) as file:
        for line in file:
            city_description = line.split()
            if len(city_description) > 1:
                x_coords.append(float(city_description[1]))
                y_coords.append(float(city_description[2]))
    return x_coords, y_coords



def get_euclidean_squares(visited_list, x_coords, y_coords, max_cities):
    """ Uses the nearest neighbour heuristic to find the travel order of the tour.
    Returns array of Euclidean squares.

    1. Start the tour at the first city.
    2. Repeatedly visit the closest city that the tour hasn't visited yet. In
       case of a tie, go to the closest city with the lowest index.
    3. Once every city has been visited exactly once, return to the first city.
    """

    euclidean_squares = []
    current_city = 1
    visited_list[current_city] = True

    while False in visited_list:
        best_distance = 0
        best_city = None
        current_x = x_coords[current_city]
        current_y = y_coords[current_city]
        for next_city in range(2, max_cities + 1):

            if next_city != current_city and visited_list[next_city] == False:
                next_x = x_coords[next_city]
                next_y = y_coords[next_city]
                distance = calculate_euclidean_square(current_x, next_x, current_y, next_y)

                if best_distance == 0 or ((best_distance > 0) and (distance < best_distance)):
                    best_distance = distance
                    best_city = next_city
                elif distance == best_distance:
                    if next_city < best_city:
                        best_city = next_city

        current_city = best_city
        euclidean_squares.append(best_distance)
        visited_list[best_city] = True
    
    current_x = x_coords[current_city]
    current_y = y_coords[current_city]
    final_x = x_coords[1]
    final_y = y_coords[1]
    final_distance = calculate_euclidean_square(current_x, final_x, current_y, final_y)
    euclidean_squares.append(final_distance)
    
    return euclidean_squares


def calculate_tour_cost(euclidean_squares):
    """ Uses tsp_tour to calculate the overall cost of the tour.
    """

    total_cost = 0
    for i in range(len(euclidean_squares)):
        cost = (euclidean_squares[i] ** 0.5)
        total_cost = total_cost + cost
    total_cost = math.floor(total_cost)
    return total_cost


def tsp_heuristic(file_name):
    """ Algorithm used to find the overall cost of a TSP tour.
    """
    
    max_cities = get_maximum_city_index(file_name)
    visited_list = create_visited_cities_list(max_cities)
    x_coords, y_coords = get_city_coordinates(file_name)
    euclidean_squares = get_euclidean_squares(visited_list, x_coords, y_coords, max_cities)
    total_cost = calculate_tour_cost(euclidean_squares)
    print(total_cost)


def main():
    file_name = str(sys.argv[1])
    tsp_heuristic(file_name)


if __name__ == "__main__":
    main()


"""
TO DO:

x. Create shell script

"""