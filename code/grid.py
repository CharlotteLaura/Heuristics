from sys import argv
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
        #self.cables =

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

        print(houses)
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

        print(batteries)

if __name__ == "__main__":
    # makes sure proper command line argument from user
    if len(argv) != 2 or argv[1] not in (["wijk1", "wijk2", "wijk3"]):
        print("Usage: grid.py district")
        exit(1)

    Grid(argv[1])
