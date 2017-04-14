import random
from unittest import TestCase

import pytest

from board import Board, CoordinateError


class TestBoard(TestCase):
    @pytest.fixture
    def setUp(self):
        self.b = Board()
        self.player = random.randint(1, self.b.players)

    def test_fire(self):
        assert not self.b.shots[self.player]
        random_coordinates = random.choice(self.b.cell_coordinates)
        self.b.fire(self.player, random_coordinates)
        assert self.b.shots[self.player]
        assert self.b.shots[self.player].pop() == random_coordinates

    def test_fire_not_existing_coordinate(self):
        with pytest.raises(CoordinateError):
            self.b.fire(self.player, 'Z0')