import random

from behave import *

from board import Board, PlacementError

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
    for player in context.board.ships:
        assert not context.board.ships[player]


@when("Player {player_id:d} fires a random shot")
def step_impl(context, player_id):
    """
    :type context: behave.runner.Context
    """
    game_board = context.board
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


@then("it's Player {player_id:d}'s turn")
def step_impl(context, player_id):
    """
    :type context: behave.runner.Context
    """
    assert context.board.current_player == player_id


@when("Player {player_id:d} places a ship")
def step_impl(context, player_id):
    """
    :type context: behave.runner.Context
    """
    start_coordinate = 'A1'
    length = 5
    orientation = "DOWN"
    context.board.place_ship(player=player_id,
                             start_coordinate=start_coordinate,
                             length=length,
                             orientation=orientation)


@then("it is placed on Player {player_id:d}'s board")
def step_impl(context, player_id):
    """
    :type context: behave.runner.Context
    """
    assert context.board.ships[player_id]


@given("a game with one ship")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.b = Board()
    context.b.place_ship(1, start_coordinate='A1', length=1, orientation='DOWN')
    context.amount_of_ships = len(context.b.ships[1])


@when("Player 1 places a ship in the same location")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.b.place_ship(1, start_coordinate='A1', length=1, orientation='RIGHT')
    except PlacementError:
        pass


@then("the ship is not placed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert len(context.b.ships[1]) == context.amount_of_ships