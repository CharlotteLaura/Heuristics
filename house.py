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
        self.connections = {}
