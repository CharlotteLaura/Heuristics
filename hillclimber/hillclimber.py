class Hillclimber():
    "tries to find a better solution than the random Grid solution"

    def __init__(self, current_grid):
        self.current_grid = current_grid
        solutions = {}

    def optimize(self):
        # lengte van kabels

        for i in range(len(self.current_grid.houses.values())):

            dict = {}

            dict[0] = (abs(self.current_grid.houses[i].x - self.current_grid.batteries[0].x)
            + abs(self.current_grid.houses[i].y - self.current_grid.batteries[j].y), self.current_grid.batteries[0])
            dict[1] = (abs(self.current_grid.houses[i].x - self.current_grid.batteries[1].x)
            + abs(self.current_grid.houses[i].y - self.current_grid.batteries[j].y), self.current_grid.batteries[1])
            dict[2] = (abs(self.current_grid.houses[i].x - self.current_grid.batteries[2].x)
            + abs(self.current_grid.houses[i].y - self.current_grid.batteries[j].y), self.current_grid.batteries[2])
            dict[3] = (abs(self.current_grid.houses[i].x - self.current_grid.batteries[3].x)
            + abs(self.current_grid.houses[i].y - self.current_grid.batteries[j].y), self.current_grid.batteries[3])
            dict[4] = abs(self.current_grid.houses[i].x - self.current_grid.batteries[4].x)
            + abs(self.current_grid.houses[i].y - self.current_grid.batteries[j].y), self.current_grid.batteries[4])

            ans = min(dict[1][0], dict[2][0], dict[3][0], dict[4][0], dict[5][0])

            for k, v in dict.items():
                if ans == v:
                    self.current_grid.houses[i].set_battery_id(k)

            # ID van de laagste afstand assignen:

            # daarna een kosten functie toepassen voor volle batterijen:


# je hebt batterijen en huizen
# deze staan een bepaalde afstand van elkaar verwijderd
# de afstand bepaalt de prijs in de eerste opdracht (en van capaciteit en max-output huis)
# hoe optimaliseer je de afstand van elk huis tot aan de batterij?
# door het huis aan de juiste batterij te koppelen.
# hoe kijk je welke de juiste(re) batterij is? door een score te geven aan een huis
# de score van het huis is de afstand tot aan de batterij
