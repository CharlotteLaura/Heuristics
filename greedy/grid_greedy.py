from sys import argv
import matplotlib.pyplot as plt
from battery import Battery
from house import House
from scipy.spatial import distance
import math


class Grid():
    """
    Contraints necessary attributes and methods to set up
    a twodimensional grid with houses, batteries and cables.
    """

    def __init__(self, district):
        """
        Create rooms and items for the appropriate 'game' version.
        """
        self.houses = self.load_houses(f"{district}_huizen.csv")
        self.batteries = self.load_batteries(f"{district}_batterijen.txt")

    def load_houses(self, filename):
        """
        Load houses from filename.
        Returns a dictionary of 'id' : House objects.
        """
        # First parse data from file
        # Save parsed lines to houses_data
        houses_data = []
        with open(filename, "r") as file:
            for line in file:
                stripped_line = line.strip('\n')
                houses_data.append(stripped_line.split(','))
        # Create house objects for each set of data just parsed.
        houses = {}
        id_nr = 0
        for house in houses_data:
            id = id_nr
            house.insert(0, id)
            x = int(house[1])
            y = int(house[2])
            max_output = float(house[3])
            id_nr += 1
            # initialize a house object and put it in a dict with id as key
            house = House(id, x, y, max_output)
            houses[id] = house
        #print(houses)
        return houses

    def load_batteries(self, filename):
        """"
        Load batteries from filename.
        returns a dictionary of "id" : Battery objects
        """
        battery_data = []
        with open(filename, "r") as file:
            for line in file:
                line = line.strip('\n')
                battery_data.append(line.split(','))

        batteries = {}
        id_nr = 0

        for battery in battery_data:
            id = id_nr
            battery.insert(0, id)
            x = int(battery[1])
            y = int(battery[2])
            capacity = float(battery[3])
            id_nr += 1
            #initialize a house object and put it in a dict with id as key
            battery = Battery(id, x, y, capacity)
            batteries[id] = battery

        return batteries

    def get_manhattan_distance(self):
        """ Return manhattan distance for all pair of batteries and houses"""
        import collections
        # Looping though each battery, then houses
        manhattan_distance = {}
        for battery_key, battery_value in self.batteries.items():
            battery_position = battery_value.x, battery_value.y
            for house_key, house_value in self.houses.items():
                house_position = house_value.x, house_value.y
                manhattan_distance[(battery_key, house_key)] = distance.cityblock(battery_position, house_position)

        sorted_manhattan_distance = sorted(manhattan_distance.items(), key=lambda kv: kv[1])
        print(collections.OrderedDict(sorted_manhattan_distance))
        return collections.OrderedDict(sorted_manhattan_distance)

    def get_manhattan_distance2(self):
        """ Return manhattan distance for all pair of batteries and houses"""
        import collections
        # Looping though each battery, then houses
        manhattan_distance = {}
        for battery_key, battery_value in self.batteries.items():
            battery_position = battery_value.x, battery_value.y
            for house_key, house_value in self.houses.items():
                house_position = house_value.x, house_value.y
                manhattan_distance[(battery_key, house_key)] = distance.cityblock(battery_position, house_position)

        max = 90
        sorted_manhattan_distance = sorted(manhattan_distance.items(), key=lambda kv: max * kv[0][0] + kv[1])
        print(collections.OrderedDict(sorted_manhattan_distance))
        return collections.OrderedDict(sorted_manhattan_distance)

    def get_longest_shortest_routes(self):
        """ Return manhattan distance for all pair of batteries and houses"""
        import collections
        #import math

        manhattan_distance = []
        for house_key, house_value in self.houses.items():
            house_position = house_value.x, house_value.y
            for battery_key, battery_value in self.batteries.items():
                battery_position = battery_value.x, battery_value.y
                manhattan_distance.append([house_key, battery_key, distance.cityblock(battery_position, house_position)])

        # shortest routes
        shortest_distance_per_house = []
        for house in self.houses:
            shortest_distance = math.inf
            for i in manhattan_distance:
                #if i[0] == house and i == 0:
                if i[0] == house:
                    if i[2] < shortest_distance:
                        shortest_distance = i[2]
            shortest_distance_per_house.append(shortest_distance)

        smallest_object_value = 0
        for i in shortest_distance_per_house:
            smallest_object_value += i

        print(smallest_object_value)

        # largest routes
        largest_distance_per_house = []
        for house in self.houses:
            largest_distance = 0
            for i in manhattan_distance:
                #if i[0] == house and i == 0:
                if i[0] == house:
                    if i[2] > largest_distance:
                        largest_distance = i[2]
            largest_distance_per_house.append(largest_distance)

        biggest_object_value = 0
        for i in largest_distance_per_house:
            biggest_object_value += i

        print(biggest_object_value)


        return manhattan_distance

    def get_score(self):
        score = 0
        for battery_key, battery_value in self.batteries.items():
            battery_position = battery_value.x, battery_value.y
            for house in battery_value.connections:
                house_position = house.x, house.y
                score += distance.cityblock(battery_position, house_position)

        print(score)
        return score


    def swap_connection(self, from_battery, to_battery, from_house, to_house):
        swap_flag = True
        from_battery.delete_connection(from_house)
        to_battery.delete_connection(to_house)
        if not from_battery.add_connection(to_house):
            swap_flag = False
        if not to_battery.add_connection(from_house):
            swap_flag = False

        return swap_flag


    def greedy(self):
        manhattan_distance = self.get_manhattan_distance()


        for key, value in manhattan_distance.items():
            curr_battery = self.batteries[key[0]]
            curr_house = self.houses[key[1]]
            if curr_house.connected_battery is None:
                curr_battery.add_connection(curr_house)

        unconnected_houses = []
        unconnected_house = None
        for house in self.houses.values():
            if house.connected_battery is None:
                unconnected_houses.append(house)
                unconnected_house = house

        #print("Unconnected house: ", unconnected_house)

        unconnected_houses = [house for house in self.houses.values() if house.connected_battery is None]


        for unconnected_house in unconnected_houses:
#            unconnected_dis = {}
#            for battery_id in self.batteries.keys():
#                unconnected_dis[(battery_id, unconnected_house.id)] = manhattan_distance[(battery_id, unconnected_house.id)]
#
            max_output = 0
            max_battery = None
            for battery in self.batteries.values():
                if battery.capacity > max_output:
                    max_output = battery.capacity
                    max_battery = battery

            max_out = 0
            max_house = None
            for house in max_battery.connections:
                if house.max_output > max_out:
                    max_out = house.max_output
                    max_house = house

            max_battery.delete_connection(max_house)

            max_battery.add_connection(unconnected_house)

            remain_capacity = max_battery.capacity

            output = 0
            second_best_battery = None
            for battery in self.batteries.values():
                if (battery.capacity > output) and (battery.capacity < remain_capacity):
                    output = battery.capacity
                    second_best_battery = battery

            output = 0
            disconnected_house = None
            for house in second_best_battery.connections:
                if (house.max_output > output) and (house.max_output <= remain_capacity):
                    output = house.max_output
                    disconnected_house = house

            second_best_battery.delete_connection(disconnected_house)

            max_battery.add_connection(disconnected_house)

            second_best_battery.add_connection(max_house)

        #return
    def greedy2(self):
        """
        Implements greedy per battery, this version is hardcoded
        """
        manhattan_distance0 = self.get_manhattan_distance_per_battery(0)
        for key, value in manhattan_distance0.items():
            curr_battery = self.batteries[0]
            curr_house = self.houses[key[1]]
            if curr_house.connected_battery is None:
                curr_battery.add_connection(curr_house)

        manhattan_distance1 = self.get_manhattan_distance_per_battery(1)
        for key, value in manhattan_distance1.items():
            curr_battery = self.batteries[1]
            curr_house = self.houses[key[1]]
            if curr_house.connected_battery is None:
                curr_battery.add_connection(curr_house)

        manhattan_distance2 = self.get_manhattan_distance_per_battery(2)
        for key, value in manhattan_distance2.items():
            curr_battery = self.batteries[2]
            curr_house = self.houses[key[1]]
            if curr_house.connected_battery is None:
                curr_battery.add_connection(curr_house)

        manhattan_distance3 = self.get_manhattan_distance_per_battery(3)
        for key, value in manhattan_distance3.items():
            curr_battery = self.batteries[3]
            curr_house = self.houses[key[1]]
            if curr_house.connected_battery is None:
                curr_battery.add_connection(curr_house)

        manhattan_distance4 = self.get_manhattan_distance_per_battery(4)
        for key, value in manhattan_distance4.items():
            curr_battery = self.batteries[4]
            curr_house = self.houses[key[1]]
            if curr_house.connected_battery is None:
                curr_battery.add_connection(curr_house)

        # connecting unconnected houses
#         unconnected_houses = [house for house in self.houses.values() if house.connected_battery is None]
#         for unconnected_house in unconnected_houses:
# #            unconnected_dis = {}
# #            for battery_id in self.batteries.keys():
# #                unconnected_dis[(battery_id, unconnected_house.id)] = manhattan_distance[(battery_id, unconnected_house.id)]
# #
#             max_output = 0
#             max_battery = None
#             for battery in self.batteries.values():
#                 if battery.capacity > max_output:
#                     max_output = battery.capacity
#                     max_battery = battery
#
#             max_out = 0
#             max_house = None
#             for house in max_battery.connections:
#                 if house.max_output > max_out:
#                     max_out = house.max_output
#                     max_house = house
#
#             max_battery.delete_connection(max_house)
#
#             max_battery.add_connection(unconnected_house)
#
#             remain_capacity = max_battery.capacity
#
#             output = 0
#             second_best_battery = None
#             for battery in self.batteries.values():
#                 if (battery.capacity > output) and (battery.capacity < remain_capacity):
#                     output = battery.capacity
#                     second_best_battery = battery
#
#             output = 0
#             disconnected_house = None
#             for house in second_best_battery.connections:
#                 if (house.max_output > output) and (house.max_output <= remain_capacity):
#                     output = house.max_output
#                     disconnected_house = house
#
#             second_best_battery.delete_connection(disconnected_house)
#
#             max_battery.add_connection(disconnected_house)
#
#             second_best_battery.add_connection(max_house)


    def get_manhattan_distance_per_battery(self, batteryId):
        import collections
        # Looping though each battery, then houses
        manhattan_distance = {}
        current_battery = self.batteries[batteryId]
        battery_position = self.batteries[batteryId].x, self.batteries[batteryId].y
        for house_key, house_value in self.houses.items():
            house_position = house_value.x, house_value.y
            manhattan_distance[(current_battery.id, house_key)] = distance.cityblock(battery_position, house_position)

        sorted_manhattan_distance = sorted(manhattan_distance.items(), key=lambda kv: kv[1])
        #print(collections.OrderedDict(sorted_manhattan_distance))
        #print(collections.OrderedDict(sorted_manhattan_distance))

        return collections.OrderedDict(sorted_manhattan_distance)


    def visualize(self):
        """
        Visualizes batteries and houses in a scatterplot
        """
        x_battery = []
        y_battery = []
        for i in range(len(self.batteries)):
            x_battery.append(self.batteries[i].x)
            y_battery.append(self.batteries[i].y)
        x_house = []
        y_house = []
        for i in range(len(self.houses)):
            x_house.append(self.houses[i].x)
            y_house.append(self.houses[i].y)

        plt.scatter(x_battery, y_battery, marker='s', color='red')
        plt.scatter(x_house, y_house, marker='^', color='blue')
        plt.grid()
        plt.show()

    def visualize2(self):
        """
        Visualizes batteries and houses in a scatterplot
        """

        # opdelen zodat alle huizen gekleurd kunnen worden a.d.h. de gekoppelde batterij:

        x_battery = {}
        y_battery = {}
        x_house = {}
        y_house = {}

        for i in range(len(self.batteries)):
            x_battery[i] = self.batteries[i].x
            y_battery[i] = self.batteries[i].y
            x_house[i] = []
            y_house[i] = []

        for i in range(len(self.houses)):
            if self.houses[i].connected_battery == 0:
                x_house[0].append(self.houses[i].x)
                y_house[0].append(self.houses[i].y)
            elif self.houses[i].connected_battery == 1:
                x_house[1].append(self.houses[i].x)
                y_house[1].append(self.houses[i].y)
            elif self.houses[i].connected_battery == 2:
                x_house[2].append(self.houses[i].x)
                y_house[2].append(self.houses[i].y)
            elif self.houses[i].connected_battery == 3:
                x_house[3].append(self.houses[i].x)
                y_house[3].append(self.houses[i].y)
            elif self.houses[i].connected_battery == 4:
                x_house[4].append(self.houses[i].x)
                y_house[4].append(self.houses[i].y)

            else:
                print("what happened?")

        # plotting the batteries:
        plt.scatter(x_battery[0], y_battery[0], marker='s', color='blue')
        plt.scatter(x_battery[1], y_battery[1], marker='s', color='red')
        plt.scatter(x_battery[2], y_battery[2], marker='s', color='purple')
        plt.scatter(x_battery[3], y_battery[3], marker='s', color='pink')
        plt.scatter(x_battery[4], y_battery[4], marker='s', color='orange')

        #plotting the houses (same color as battery they belong to):
        plt.scatter(x_house[0], y_house[0], marker='2', color='blue')
        plt.scatter(x_house[1], y_house[1], marker='2', color='red')
        plt.scatter(x_house[2], y_house[2], marker='2', color='purple')
        plt.scatter(x_house[3], y_house[3], marker='2', color='pink')
        plt.scatter(x_house[4], y_house[4], marker='2', color='orange')

        # plot grid and show image:
        plt.grid()
        plt.show()

    def hardcoded_solution(self):
        for i in range(150):
            if grid.batteries[0].capacity >= grid.houses[i].max_output:
                grid.batteries[0].add_connection(grid.houses[i])
            elif grid.batteries[1].capacity >= grid.houses[i].max_output:
                grid.batteries[1].add_connection(grid.houses[i])
            elif grid.batteries[2].capacity >= grid.houses[i].max_output:
                grid.batteries[2].add_connection(grid.houses[i])
            elif grid.batteries[3].capacity >= grid.houses[i].max_output:
                grid.batteries[3].add_connection(grid.houses[i])
            elif grid.batteries[4].capacity >= grid.houses[i].max_output:
                grid.batteries[4].add_connection(grid.houses[i])
            else:
                print("No more batteries left")

if __name__ == "__main__":
    # makes sure proper command line argument from user
    if len(argv) != 2 or argv[1] not in (["wijk1", "wijk2", "wijk3"]):
        print("Usage: grid.py district")
        exit(1)

    grid = Grid(argv[1])
    #grid.get_longest_shortest_routes()
    #grid.greedy()
    #grid.hardcoded_solution()
    #grid.greedy2()
    #grid.visualize2()
    #grid.get_score()
    grid.get_manhattan_distance()

    # for i in grid.batteries:
    #     print(f"Battery {i}: ")
    #     for connection in grid.batteries[i].get_connections():
    #         print(connection)

    print('\n-------------------------------------------------------------\n')

    #
    # for i in grid.batteries.values():
    #     print(f"Battery {i}: ")
    #     print(i.capacity)
    #     # for connection in i.get_connections():
    #     #     print(connection)

    # print("Score: ")
    # grid.get_score()
    #
    # print("Remaining houses: ")
    # for house in grid.houses.values():
    #     if house.connected_battery is None:
    #         print(house.id, house.max_output)
    #
    # print("Remaining capacities: ")
    # for battery in grid.batteries.values():
    #     print(f"Battery{battery}: ")
    #     print(battery.capacity)



#    grid.visualize()
