import random
from unittest import TestCase

import pytest

from board import Board, CoordinateError, PlacementError


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
        get_board.fire(random_player, 'Z0')


def test_place_ship(get_board, random_player):
    assert not get_board.ships[random_player]
    get_board.place_ship(random_player, orientation='DOWN', length=1, start_coordinate='A1')
    assert get_board.ships[random_player]


def test_place_ship_out_of_bounds_right(get_board, random_player):
    assert not get_board.ships[random_player]
    with pytest.raises(PlacementError):
        get_board.place_ship(random_player, orientation='RIGHT', length=2, start_coordinate='J1')
    assert not get_board.ships[random_player]


@pytest.mark.parametrize("coordinate,length,orientation", [
    ('A8', 2, "DOWN"), ('B8', 2, "DOWN"), ('C8', 2, "DOWN"), ('D8', 2, "DOWN"), ('E8', 2, "DOWN"), ('F8', 2, "DOWN"),
    ('G8', 2, "DOWN"), ('H8', 2, "DOWN"), ('I8', 2, "DOWN"), ('J8', 2, "DOWN"), ('A7', 3, "DOWN"), ('B7', 3, "DOWN"),
    ('C7', 3, "DOWN"), ('D7', 3, "DOWN"), ('E7', 3, "DOWN"), ('F7', 3, "DOWN"), ('G7', 3, "DOWN"), ('H7', 3, "DOWN"),
    ('I7', 3, "DOWN"), ('J7', 3, "DOWN"), ('A6', 4, "DOWN"), ('B6', 4, "DOWN"), ('C6', 4, "DOWN"), ('D6', 4, "DOWN"),
    ('E6', 4, "DOWN"), ('F6', 4, "DOWN"), ('G6', 4, "DOWN"), ('H6', 4, "DOWN"), ('I6', 4, "DOWN"), ('J6', 4, "DOWN"),
    ('A5', 5, "DOWN"), ('B5', 5, "DOWN"), ('C5', 5, "DOWN"), ('D5', 5, "DOWN"), ('E5', 5, "DOWN"), ('F5', 5, "DOWN"),
    ('G5', 5, "DOWN"), ('H5', 5, "DOWN"), ('I5', 5, "DOWN"), ('J5', 5, "DOWN"), ('J1', 2, "RIGHT"), ('J2', 2, "RIGHT"),
    ('J3', 2, "RIGHT"), ('J4', 2, "RIGHT"), ('J5', 2, "RIGHT"), ('J6', 2, "RIGHT"), ('J7', 2, "RIGHT"),
    ('J8', 2, "RIGHT"), ('I1', 3, "RIGHT"), ('I2', 3, "RIGHT"), ('I3', 3, "RIGHT"), ('I4', 3, "RIGHT"),
    ('I5', 3, "RIGHT"), ('I6', 3, "RIGHT"), ('I7', 3, "RIGHT"), ('I8', 3, "RIGHT"), ('H1', 4, "RIGHT"),
    ('H4', 4, "RIGHT"), ('H3', 4, "RIGHT"), ('H4', 4, "RIGHT"), ('H5', 4, "RIGHT"), ('H6', 4, "RIGHT"),
    ('H7', 4, "RIGHT"), ('H8', 4, "RIGHT"), ('G1', 5, "RIGHT"), ('G5', 5, "RIGHT"), ('G3', 5, "RIGHT"),
    ('G4', 5, "RIGHT"), ('G5', 5, "RIGHT"), ('G6', 5, "RIGHT"), ('G7', 5, "RIGHT"), ('G8', 5, "RIGHT")
])
def test_out_of_bounds(get_board, random_player, coordinate, length, orientation):
    board = get_board
    assert not board.ships[random_player]
    with pytest.raises(PlacementError):
        board.place_ship(random_player, orientation=orientation, length=length, start_coordinate=coordinate)
    assert not board.ships[random_player]


@pytest.mark.parametrize("coordinate,length,orientation", [
    ('A8', 2, "DOWN"), ('B8', 2, "DOWN"), ('C8', 2, "DOWN"), ('D8', 2, "DOWN"), ('E8', 2, "DOWN"), ('F8', 2, "DOWN"),
    ('G8', 2, "DOWN"), ('H8', 2, "DOWN"), ('I8', 2, "DOWN"), ('J8', 2, "DOWN"), ('A7', 3, "DOWN"), ('B7', 3, "DOWN"),
    ('C7', 3, "DOWN"), ('D7', 3, "DOWN"), ('E7', 3, "DOWN"), ('F7', 3, "DOWN"), ('G7', 3, "DOWN"), ('H7', 3, "DOWN"),
    ('I7', 3, "DOWN"), ('J7', 3, "DOWN"), ('A6', 4, "DOWN"), ('B6', 4, "DOWN"), ('C6', 4, "DOWN"), ('D6', 4, "DOWN"),
    ('E6', 4, "DOWN"), ('F6', 4, "DOWN"), ('G6', 4, "DOWN"), ('H6', 4, "DOWN"), ('I6', 4, "DOWN"), ('J6', 4, "DOWN"),
    ('A5', 5, "DOWN"), ('B5', 5, "DOWN"), ('C5', 5, "DOWN"), ('D5', 5, "DOWN"), ('E5', 5, "DOWN"), ('F5', 5, "DOWN"),
    ('G5', 5, "DOWN"), ('H5', 5, "DOWN"), ('I5', 5, "DOWN"), ('J5', 5, "DOWN"), ('J1', 2, "RIGHT"), ('J2', 2, "RIGHT"),
    ('J3', 2, "RIGHT"), ('J4', 2, "RIGHT"), ('J5', 2, "RIGHT"), ('J6', 2, "RIGHT"), ('J7', 2, "RIGHT"),
    ('J8', 2, "RIGHT"), ('I1', 3, "RIGHT"), ('I2', 3, "RIGHT"), ('I3', 3, "RIGHT"), ('I4', 3, "RIGHT"),
    ('I5', 3, "RIGHT"), ('I6', 3, "RIGHT"), ('I7', 3, "RIGHT"), ('I8', 3, "RIGHT"), ('H1', 4, "RIGHT"),
    ('H4', 4, "RIGHT"), ('H3', 4, "RIGHT"), ('H4', 4, "RIGHT"), ('H5', 4, "RIGHT"), ('H6', 4, "RIGHT"),
    ('H7', 4, "RIGHT"), ('H8', 4, "RIGHT"), ('G1', 5, "RIGHT"), ('G5', 5, "RIGHT"), ('G3', 5, "RIGHT"),
    ('G4', 5, "RIGHT"), ('G5', 5, "RIGHT"), ('G6', 5, "RIGHT"), ('G7', 5, "RIGHT"), ('G8', 5, "RIGHT")
])
def test_some_placements_inside_of_bounds(get_board, random_player, coordinate, length, orientation):
    board = get_board
    assert not board.ships[random_player]
    if orientation == "RIGHT":
        i = 0
    board.place_ship(random_player, orientation=orientation, length=length - 1, start_coordinate=coordinate)
    assert board.ships[random_player]
