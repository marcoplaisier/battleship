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