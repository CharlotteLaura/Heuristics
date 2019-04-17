from house import House

class Battery():
    """
    Representation of a battery in smartgrid
    """

    def __init__(self, id, x, y, capacity):
        """
        Create batteries for specific district
        """
        self.id = id
        self.x = x
        self.y = y
        self.capacity = capacity
        self.connections = []

    def add_connection(self, house):
        """
        Adds a house to the set of connections
        """
        if house not in self.connections and house.max_output < self.capacity:
            self.connections.append(house)
            self.capacity = self.capacity - house.max_output
            house.connected_battery = self.id
        else:
            print("Battery does not have enough capacity to connect this house")

    def get_connections(self):
        """
        Returns a list of which houses are connected to a specific battery
        """
        return self.connections

    def __str__(self):
        return "Battery " + str(self.id)

    def __repr__(self):
        return "Battery " + str(self.id) + " X: " + str(self.x) + " Y: " + str(self.y)
