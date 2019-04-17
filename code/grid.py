from sys import argv
import matplotlib.pyplot as plt
from battery import Battery
from house import House


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


if __name__ == "__main__":
    # makes sure proper command line argument from user
    if len(argv) != 2 or argv[1] not in (["wijk1", "wijk2", "wijk3"]):
        print("Usage: grid.py district")
        exit(1)

    grid = Grid(argv[1])

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

    # print(grid.batteries[0].get_connections())
    # print(grid.batteries[1].get_connections())
    # print(grid.batteries[2].get_connections())
    # print(grid.batteries[3].get_connections())
    # print(grid.batteries[4].get_connections())

    grid.visualize()

    # grid.batteries[0].add_connection(grid.houses[0])
    # #print(grid.batteries[0].get_connections())
    # grid.batteries[0].add_connection(grid.houses[1])
    # grid.batteries[0].add_connection(grid.houses[2])
    # grid.batteries[0].add_connection(grid.houses[3])
    # grid.batteries[0].add_connection(grid.houses[4])
    # grid.batteries[0].add_connection(grid.houses[5])
    # grid.batteries[0].add_connection(grid.houses[6])
    # grid.batteries[0].add_connection(grid.houses[7])
    # grid.batteries[0].add_connection(grid.houses[8])
    # grid.batteries[0].add_connection(grid.houses[9])
    # grid.batteries[0].add_connection(grid.houses[10])
    # grid.batteries[0].add_connection(grid.houses[11])
    # grid.batteries[0].add_connection(grid.houses[12])
    # grid.batteries[0].add_connection(grid.houses[13])
    # grid.batteries[0].add_connection(grid.houses[14])
    # grid.batteries[0].add_connection(grid.houses[15])
    # grid.batteries[0].add_connection(grid.houses[16])
    # grid.batteries[0].add_connection(grid.houses[17])
    # grid.batteries[0].add_connection(grid.houses[18])
    # grid.batteries[0].add_connection(grid.houses[19])
    # grid.batteries[0].add_connection(grid.houses[20])
    # grid.batteries[0].add_connection(grid.houses[21])
    # grid.batteries[0].add_connection(grid.houses[22])
    # grid.batteries[0].add_connection(grid.houses[23])
    # grid.batteries[0].add_connection(grid.houses[24])
    # grid.batteries[0].add_connection(grid.houses[25])
    # grid.batteries[0].add_connection(grid.houses[26])
    # grid.batteries[0].add_connection(grid.houses[27])
    # grid.batteries[0].add_connection(grid.houses[28])
    # grid.batteries[0].add_connection(grid.houses[29])
    # print(grid.batteries[0].get_connections())
