class House():
    """
    Representation of a house in smartgrid
    """

    def __init__(self, id, x, y, max_output):
        """
        Create houses for specific district
        """
        self.id = id
        self.x = x
        self.y = y
        self.max_output = max_output
        self.connected_battery = None

    def __str__(self):
        return "House " + str(self.id) + " Connected to battery " + str(self.connected_battery) + " Max output: "+ str(self.max_output)

    def __repr__(self):
        return "House " + str(self.id) + " Connected to battery " + str(self.connected_battery) + " Max output: "+ str(self.max_output)
