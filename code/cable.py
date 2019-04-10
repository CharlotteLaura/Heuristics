class Cable():
    """
    Representation of a cable in smartgrid
    """

    def __init__(self, house, battery):
        """
        Create cables for specific district
        """
        self.house = house
        self.battery = battery
        
