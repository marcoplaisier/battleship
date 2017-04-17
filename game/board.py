from itertools import product, chain


class CoordinateError(BaseException):
    pass


class PlacementError(BaseException):
    pass


class Board:
    COLUMNS = range(10)
    ROWS = range(8)
    cell_coordinates = [cell for cell in product(COLUMNS, ROWS)]

    def __init__(self, players=2):
        self.boards = {}
        self.players = players
        self.shots = {player + 1: [] for player in range(players)}
        self.ships = {player + 1: [] for player in range(players)}
        self._current_player = 1
        self._other_player = 2

    @property
    def current_player(self):
        return self._current_player

    @property
    def other_player(self):
        return self._other_player

    @current_player.setter
    def current_player(self, player_id):
        if player_id != self._current_player:
            self.next_player()

    def next_player(self):
        self._current_player, self._other_player = self.other_player, self._current_player
        return self._current_player

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

    def place_ship(self, player, start_coordinate, length, orientation):
        possible_ship = Ship(start_coordinate=start_coordinate, length=length, orientation=orientation)
        ship_coordinates = possible_ship.coordinates()

        if self.is_ship_out_of_bounds(ship_coordinates):
            raise PlacementError('Ship place out of bounds')
        for existing_ship in self.ships[player]:
            if possible_ship.is_overlapping(existing_ship):
                raise PlacementError('One or more of the coordinates are already occupied')

        self.ships[player].append(possible_ship)

    def is_ship_out_of_bounds(self, ship_coordinates):
        for column, row in ship_coordinates:
            if column not in self.COLUMNS:
                out_of_bounds = True
                break
            elif row not in self.ROWS:
                out_of_bounds = True
                break
        else:
            out_of_bounds = False

        return out_of_bounds

    def hits(self, player):
        return len(self.hit_coordinates(player))

    def hit_coordinates(self, player):
        return list(chain.from_iterable([ship.hits for ship in self.ships[player]]))

    def get_possible_moves(self, player):
        return list(set(self.cell_coordinates) - set(self.shots[player]))


class Ship:
    DOWN = "DOWN"
    RIGHT = "RIGHT"

    def __init__(self, start_coordinate=None, orientation=None, length=None):
        self.length = length
        if not (orientation == self.DOWN or orientation == self.RIGHT):
            raise PlacementError('Orientation unknown')
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
            ship_coordinates = [(column, r) for r in range(row, row + self.length)]
        elif self.orientation == Ship.RIGHT:
            ship_coordinates = [(c, row) for c in range(column, column + self.length)]
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
