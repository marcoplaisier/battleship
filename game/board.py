from itertools import product, zip_longest


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
        self.other_player = 2

    def has_lost(self, player):
        if self.ships[player]:
            return all(ship.is_sunk() for ship in self.ships[player])
        else:
            return True

    def fire(self, player, coordinate):
        if coordinate not in self.cell_coordinates:
            raise CoordinateError("coordinates {} do not exist".format(coordinate))
        self.shots[player].append(coordinate)

        return any([ship.hit(coordinate) for ship in self.ships[self.other_player]])

    def next_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player
        return self.current_player

    def place_ship(self, player, start_coordinate, length, orientation):
        possible_ship = Ship(start_coordinate=start_coordinate, length=length, orientation=orientation)
        ship_coordinates = possible_ship.coordinates()

        if self.is_ship_out_of_bounds(length, ship_coordinates):
            raise PlacementError('Ship place out of bounds')
        for existing_ship in self.ships[player]:
            if possible_ship.is_overlapping(existing_ship):
                raise PlacementError('One or more of the coordinates are already occupied')

        self.ships[player].append(possible_ship)

    @staticmethod
    def is_ship_out_of_bounds(length, ship_coordinates):
        return len(ship_coordinates) != length


class Ship:
    DOWN = "DOWN"
    RIGHT = "RIGHT"

    def __init__(self, start_coordinate=None, orientation=None, length=None):
        self.length = length
        self.orientation = orientation
        self.start_coordinate = start_coordinate
        self.hits = []

    def is_overlapping(self, other_ship):
        this_coordinates = self.coordinates()
        other_coordinates = other_ship.coordinates()
        overlap = set(this_coordinates).intersection(set(other_coordinates))
        return bool(overlap)

    def coordinates(self):
        column, row = self.start_coordinate
        if self.orientation == Ship.DOWN:
            row = int(row) - 1
            ship_coordinates = [column + str(r) for r in Board.ROWS[row:row + self.length]]
        elif self.orientation == Ship.RIGHT:
            column_index = Board.COLUMNS.index(column)
            ship_coordinates = [c + str(row) for c in Board.COLUMNS[column_index:column_index + self.length]]
        else:
            raise PlacementError('Orientation unknown')
        return ship_coordinates

    def hit(self, coordinate):
        if coordinate in self.coordinates():
            self.hits.append(coordinate)
            return True
        else:
            return False

    def is_sunk(self):
        return len(self.hits) == self.length
