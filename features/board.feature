Feature: Boards
  # Enter feature description here

  Scenario: Create a new board
    Given a new game
    When we start the game
    Then we have an empty game board

  Scenario: Player 1 fires a shot
    Given a started game
    When Player 1 fires a random shot
    Then the shot is registered for player 1

  Scenario: Player places a ship
    Given a started game
    When Player 1 places a ship
    Then it is placed on Player 1's board

  Scenario: Player places a ship
    Given a game with one ship for Player 1
    When Player 1 places a ship in the same location
    Then the ship is not placed for Player 1

  Scenario: Player places a ship
    Given a game with one ship for Player 1
    When Player 2 places a ship in the same location
    Then it is placed on Player 2's board