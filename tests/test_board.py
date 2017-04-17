import random
import pytest

from game.board import Board, CoordinateError, PlacementError


@pytest.fixture
def random_player(get_board):
    return random.randint(1, get_board.players)


@pytest.fixture
def get_board():
    return Board()


def test_fire(get_board, random_player):
    assert not get_board.shots[random_player]
    random_coordinates = random.choice(get_board.cell_coordinates)
    get_board.fire(random_player, random_coordinates)
    assert get_board.shots[random_player]
    assert get_board.shots[random_player].pop() == random_coordinates


def test_fire_not_existing_coordinate(get_board, random_player):
    with pytest.raises(CoordinateError):
        get_board.fire(random_player, (11, 20))


def test_place_ship(get_board, random_player):
    assert not get_board.ships[random_player]
    get_board.place_ship(random_player, orientation='DOWN', length=1, start_coordinate=(0, 0))
    assert get_board.ships[random_player]


def test_place_ship_out_of_bounds_right(get_board, random_player):
    assert not get_board.ships[random_player]
    with pytest.raises(PlacementError):
        get_board.place_ship(random_player, orientation='RIGHT', length=2, start_coordinate=(10, 11))
    assert not get_board.ships[random_player]


@pytest.mark.parametrize("coordinate,length,orientation", [
    ((0, 7), 2, "DOWN"), ((1, 8), 2, "DOWN"), ((2, 7), 2, "DOWN"), ((3, 8), 2, "DOWN"), ((4, 8), 2, "DOWN"),
    ((5, 7), 2, "DOWN"), ((6, 7), 2, "DOWN"), ((7, 7), 2, "DOWN"), ((8, 8), 2, "DOWN"), ((9, 8), 2, "DOWN"),
    ((0, 7), 3, "DOWN"), ((1, 7), 3, "DOWN"), ((2, 7), 3, "DOWN"), ((3, 7), 3, "DOWN"), ((4, 7), 3, "DOWN"),
    ((5, 7), 3, "DOWN"), ((6, 7), 3, "DOWN"), ((7, 7), 3, "DOWN"), ((8, 7), 3, "DOWN"), ((9, 7), 3, "DOWN"),
    ((0, 6), 4, "DOWN"), ((1, 6), 4, "DOWN"), ((2, 6), 4, "DOWN"), ((3, 6), 4, "DOWN"), ((4, 6), 4, "DOWN"),
    ((5, 6), 4, "DOWN"), ((6, 6), 4, "DOWN"), ((7, 6), 4, "DOWN"), ((8, 6), 4, "DOWN"), ((9, 6), 4, "DOWN"),
    ((0, 5), 5, "DOWN"), ((1, 5), 5, "DOWN"), ((2, 5), 5, "DOWN"), ((3, 5), 5, "DOWN"), ((4, 5), 5, "DOWN"),
    ((5, 5), 5, "DOWN"), ((6, 5), 5, "DOWN"), ((7, 5), 5, "DOWN"), ((8, 5), 5, "DOWN"), ((9, 5), 5, "DOWN"),
    ((9, 1), 2, "RIGHT"), ((9, 2), 2, "RIGHT"), ((9, 3), 2, "RIGHT"), ((9, 4), 2, "RIGHT"), ((9, 5), 2, "RIGHT"),
    ((9, 6), 2, "RIGHT"), ((9, 7), 2, "RIGHT"), ((9, 8), 2, "RIGHT"), ((8, 1), 3, "RIGHT"), ((8, 2), 3, "RIGHT"),
    ((8, 3), 3, "RIGHT"), ((8, 4), 3, "RIGHT"), ((8, 5), 3, "RIGHT"), ((8, 6), 3, "RIGHT"), ((8, 7), 3, "RIGHT"),
    ((8, 8), 3, "RIGHT"), ((7, 1), 4, "RIGHT"), ((7, 4), 4, "RIGHT"), ((7, 3), 4, "RIGHT"), ((7, 4), 4, "RIGHT"),
    ((7, 5), 4, "RIGHT"), ((7, 6), 4, "RIGHT"), ((7, 7), 4, "RIGHT"), ((7, 8), 4, "RIGHT"), ((6, 1), 5, "RIGHT"),
    ((6, 5), 5, "RIGHT"), ((6, 3), 5, "RIGHT"), ((6, 4), 5, "RIGHT"), ((6, 5), 5, "RIGHT"), ((6, 6), 5, "RIGHT"),
    ((6, 7), 5, "RIGHT"), ((6, 7), 5, "RIGHT")
])
def test_out_of_bounds(get_board, random_player, coordinate, length, orientation):
    board = get_board
    assert not board.ships[random_player]
    with pytest.raises(PlacementError):
        board.place_ship(random_player, orientation=orientation, length=length, start_coordinate=coordinate)
    assert not board.ships[random_player]


@pytest.mark.parametrize("coordinate,length,orientation", [
    ((0, 5), 2, "DOWN"), ((1, 6), 2, "DOWN"), ((2, 6), 2, "DOWN"), ((3, 6), 2, "DOWN"), ((4, 6), 2, "DOWN"),
    ((5, 5), 2, "DOWN"), ((6, 6), 2, "DOWN"), ((7, 6), 2, "DOWN"), ((8, 6), 2, "DOWN"), ((9, 6), 2, "DOWN"),
    ((0, 4), 3, "DOWN"), ((1, 5), 3, "DOWN"), ((2, 5), 3, "DOWN"), ((3, 5), 3, "DOWN"), ((4, 5), 3, "DOWN"),
    ((5, 4), 3, "DOWN"), ((6, 5), 3, "DOWN"), ((7, 5), 3, "DOWN"), ((8, 5), 3, "DOWN"), ((9, 5), 3, "DOWN"),
    ((0, 4), 4, "DOWN"), ((1, 4), 4, "DOWN"), ((2, 4), 4, "DOWN"), ((3, 4), 4, "DOWN"), ((4, 4), 4, "DOWN"),
    ((5, 4), 4, "DOWN"), ((6, 4), 4, "DOWN"), ((7, 4), 4, "DOWN"), ((8, 4), 4, "DOWN"), ((9, 4), 4, "DOWN"),
    ((0, 3), 5, "DOWN"), ((1, 3), 5, "DOWN"), ((2, 3), 5, "DOWN"), ((3, 3), 5, "DOWN"), ((4, 3), 5, "DOWN"),
    ((5, 3), 5, "DOWN"), ((6, 3), 5, "DOWN"), ((7, 3), 5, "DOWN"), ((8, 3), 5, "DOWN"), ((9, 3), 5, "DOWN"),
    ((7, 0), 2, "RIGHT"), ((7, 1), 2, "RIGHT"), ((7, 2), 2, "RIGHT"), ((7, 3), 2, "RIGHT"), ((7, 4), 2, "RIGHT"),
    ((7, 5), 2, "RIGHT"), ((7, 6), 2, "RIGHT"), ((7, 7), 2, "RIGHT"), ((7, 1), 3, "RIGHT"), ((7, 2), 3, "RIGHT"),
    ((7, 3), 3, "RIGHT"), ((6, 4), 3, "RIGHT"), ((7, 5), 3, "RIGHT"), ((7, 6), 3, "RIGHT"), ((7, 7), 3, "RIGHT"),
    ((6, 7), 3, "RIGHT"), ((6, 1), 4, "RIGHT"), ((6, 4), 4, "RIGHT"), ((6, 3), 4, "RIGHT"), ((6, 4), 4, "RIGHT"),
    ((6, 5), 4, "RIGHT"), ((6, 6), 4, "RIGHT"), ((6, 7), 4, "RIGHT"), ((5, 1), 5, "RIGHT"), ((5, 5), 5, "RIGHT"),
    ((5, 3), 5, "RIGHT"), ((5, 4), 5, "RIGHT"), ((5, 5), 5, "RIGHT"), ((5, 6), 5, "RIGHT"), ((5, 7), 5, "RIGHT"),
    ((5, 7), 5, "RIGHT")
])
def test_some_placements_inside_of_bounds(get_board, random_player, coordinate, length, orientation):
    board = get_board
    assert not board.ships[random_player]
    board.place_ship(random_player, orientation=orientation, length=length, start_coordinate=coordinate)
    assert board.ships[random_player]


def test_next_player(get_board):
    board = get_board
    assert board.current_player == 1
    player = board.next_player()
    assert player == 2
    assert board.current_player == 2
