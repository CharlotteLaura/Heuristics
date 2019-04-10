class Grid():
    """
    Contrains necessary attributes and methods to set up
    a twodimensional grid with houses, batteries and cables.
    """

    def __init__(self, district):
        """
        Create rooms and items for the appropriate 'game' version.
        """
        self.houses = self.load_rooms(f"data/{game}Rooms.txt")
        self.batteries = self.load_items(f"data/{game}Items.txt")
        self.cables = Inventory()

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
        for house_data in houses_data:
            id = id_nr
            house.insert(0, id)
            x = int(house_data[0]
            y = int(house_data[1]
            max_output = float(house_data[2])
            id_nr += 1
            #initialize a house object and put it in a dict with id as key
            house = House(id, x, y, max_output)
            houses[id] = house

        return houses

    def load_batteries(self, filename):
        """"
        Load batteries from filename.
        returns a dictionary of "id" : Battery objects
        """
        battery_data = []
        with open(filename, "r") as file:
            for line in file:
                
