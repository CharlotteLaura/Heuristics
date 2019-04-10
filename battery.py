class Battery():
    """
    Representation of a battery in smartgrid
    """

    def __init__(self, id, position, capacity):
        """
        Create batteries for specific district
        """
        self.position = position
        self.capacity = capacity
        self.connections = {}
