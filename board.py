from itertools import product, chain


def is_player_element_empty(board):
    pass


class CoordinateError(BaseException):
    pass


class Board:
    cell_coordinates = ["".join(cell) for cell in product('ABCDEFGHIJ', '12345678')]

    def __init__(self, players=2):
        self.boards = {}
        self.players = players
        self.shots = {player+1: [] for player in range(players)}
        self.ships = {player+1: [] for player in range(players)}

    def is_empty(self):
        return sum([len(ships) for ships in self.ships.values()]) + \
               sum([len(shots) for shots in self.shots.values()]) == 0

    def fire(self, player, coordinates):
        if coordinates not in self.cell_coordinates:
            raise CoordinateError("coordinates {} do not exist".format(coordinates))
        self.shots[player].append(coordinates)
