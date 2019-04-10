class Battery():
    """
    Representation of a battery in smartgrid
    """

    def __init__(self, id, x, y, capacity):
        """
        Create batteries for specific district
        """
        self.x = x
        self.y = y
        self.capacity = capacity
        self.connections = {}
