import random

from behave import *

from board import Board

use_step_matcher("parse")


@then("we have an empty game board")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.board
    assert context.board.is_empty()
    assert context.board.cell_coordinates


@given("a new game")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("we start the game")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.board = Board()


@given("a started game")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.board = Board()


@when("Player {player} fires a random shot")
def step_impl(context, player):
    """
    :type context: behave.runner.Context
    """
    game_board = context.board
    player_id = int(player)
    all_coordinates = set(game_board.cell_coordinates)
    shots_already_fired = set(game_board.shots[player_id])
    possible_locations = list(all_coordinates - shots_already_fired)
    shot_location = random.choice(possible_locations)
    game_board.fire(player=player_id, coordinates=shot_location)
    context.shot_location = shot_location


@then("the shot is registered for player {player}")
def step_impl(context, player):
    """
    :type context: behave.runner.Context
    """
    player_id = int(player)
    assert context.board.shots[player_id]
