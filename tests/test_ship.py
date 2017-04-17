import pytest

from game.board import Ship


def test_is_overlapping():
    ship = Ship(length=1, start_coordinate='A1', orientation=Ship.DOWN)
    other_ship = Ship(length=1, start_coordinate='A1', orientation=Ship.DOWN)
    assert ship.is_overlapping(other_ship)


def test_coordinates():
    ship = Ship(length=1, start_coordinate='A1', orientation=Ship.DOWN)
    coordinates = ship.coordinates()
    assert ['A1'] == coordinates


@pytest.mark.parametrize("length,start_coordinate,orientation", [
    (2, 'C3', Ship.RIGHT), (2, 'D3', Ship.RIGHT), (5, 'B3', Ship.RIGHT), (5, 'C3', Ship.RIGHT), (5, 'D3', Ship.RIGHT),
    (5, 'B4', Ship.RIGHT), (5, 'B5', Ship.RIGHT), (5, 'B3', Ship.RIGHT), (1, 'D4', Ship.RIGHT), (1, 'D4', Ship.DOWN)
])
def test_bulk_overlap(length, start_coordinate, orientation):
    ship = Ship(length=3, start_coordinate='D3', orientation=Ship.DOWN)
    other_ship = Ship(length=length, start_coordinate=start_coordinate, orientation=orientation)
    assert ship.is_overlapping(other_ship)


@pytest.mark.parametrize("length,start_coordinate,orientation", [
    (2, 'C3', Ship.DOWN), (5, 'F3', Ship.DOWN)
])
def test_bulk_no_overlap(length, start_coordinate, orientation):
    ship = Ship(length=3, start_coordinate='D3', orientation=Ship.DOWN)
    other_ship = Ship(length=length, start_coordinate=start_coordinate, orientation=orientation)
    assert not ship.is_overlapping(other_ship)


def test_hit():
    ship = Ship(length=1, orientation=Ship.RIGHT, start_coordinate='B6')
    ship.hit('B6')
    assert ship.hits


def test_no_hit():
    ship = Ship(length=1, orientation=Ship.RIGHT, start_coordinate='B6')
    ship.hit('B7')
    assert not ship.hits
