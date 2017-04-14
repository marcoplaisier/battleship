from itertools import product, chain, zip_longest


def is_player_element_empty(board):
    pass


class CoordinateError(BaseException):
    pass


class PlacementError(BaseException):
    pass


class Board:
    COLUMNS = 'ABCDEFGHIJ'
    ROWS = '12345678'
    cell_coordinates = ["".join(cell) for cell in product(COLUMNS, ROWS)]

    def __init__(self, players=2):
        self.boards = {}
        self.players = players
        self.shots = {player + 1: [] for player in range(players)}
        self.ships = {player + 1: [] for player in range(players)}
        self.current_player = 1

    def is_empty(self):
        return sum([len(ships) for ships in self.ships.values()]) + \
               sum([len(shots) for shots in self.shots.values()]) == 0

    def fire(self, player, coordinates):
        if coordinates not in self.cell_coordinates:
            raise CoordinateError("coordinates {} do not exist".format(coordinates))
        self.shots[player].append(coordinates)
        self.current_player += 1
        if self.current_player > self.players:
            self.current_player = 1

    def place_ship(self, player, start_coordinate, length, orientation):
        ship_coordinates = self.determine_possible_ship_coordinates(length, orientation, start_coordinate)

        if self.is_ship_out_of_bounds(length, ship_coordinates):
            raise PlacementError('Ship place out of bounds')
        if self.is_ship_overlapping(ship_coordinates):
            raise PlacementError('One or more of the coordinates are already occupied')

        ship = zip_longest(ship_coordinates, [length])
        self.ships[player].extend(ship)

    def determine_possible_ship_coordinates(self, length, orientation, start_coordinate):
        column, row = start_coordinate
        if orientation == 'DOWN':
            row = int(row) - 1
            ship_coordinates = [column + str(r) for r in self.ROWS[row:row + length]]
        elif orientation == 'RIGHT':
            column_index = self.COLUMNS.index(column)
            ship_coordinates = [c + str(row) for c in self.COLUMNS[column_index:column_index + length]]
        else:
            raise PlacementError('Orientation unknown')
        return ship_coordinates

    @staticmethod
    def is_ship_out_of_bounds(length, ship_coordinates):
        return len(ship_coordinates) != length

    def is_ship_overlapping(self, ship_coordinates):
        player = self.current_player
        for occupied_cells in self.ships[player]:
            coordinate, ship = occupied_cells
            return coordinate in ship_coordinates
