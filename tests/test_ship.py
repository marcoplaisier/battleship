import pytest

from game.board import Ship


def test_is_overlapping():
    ship = Ship(length=1, start_coordinate=(0, 0), orientation=Ship.DOWN)
    other_ship = Ship(length=1, start_coordinate=(0, 0), orientation=Ship.DOWN)
    assert ship.is_overlapping(other_ship)


def test_coordinates():
    ship = Ship(length=1, start_coordinate=(0, 0), orientation=Ship.DOWN)
    coordinates = ship.coordinates()
    assert [(0, 0)] == coordinates


@pytest.mark.parametrize("length,start_coordinate,orientation", [
    (2, (2, 2), Ship.RIGHT), (2, (3, 2), Ship.RIGHT), (5, (1, 2), Ship.RIGHT), (5, (2, 2), Ship.RIGHT), (5, (3, 2), Ship.RIGHT),
    (5, (1, 3), Ship.RIGHT), (5, (1, 4), Ship.RIGHT), (5, (1, 2), Ship.RIGHT), (1, (3, 3), Ship.RIGHT), (1, (3, 3), Ship.DOWN)
])
def test_bulk_overlap(length, start_coordinate, orientation):
    ship = Ship(length=3, start_coordinate=(3, 2), orientation=Ship.DOWN)
    other_ship = Ship(length=length, start_coordinate=start_coordinate, orientation=orientation)
    assert ship.is_overlapping(other_ship)


@pytest.mark.parametrize("length,start_coordinate,orientation", [
    (2, (2, 2), Ship.DOWN), (5, (5, 2), Ship.DOWN)
])
def test_bulk_no_overlap(length, start_coordinate, orientation):
    ship = Ship(length=3, start_coordinate=(3, 2), orientation=Ship.DOWN)
    other_ship = Ship(length=length, start_coordinate=start_coordinate, orientation=orientation)
    assert not ship.is_overlapping(other_ship)


def test_hit():
    ship = Ship(length=1, orientation=Ship.RIGHT, start_coordinate=(1, 5))
    ship.hit((1, 5))
    assert ship.hits


def test_no_hit():
    ship = Ship(length=1, orientation=Ship.RIGHT, start_coordinate=(1, 5))
    ship.hit((1, 6))
    assert not ship.hits
