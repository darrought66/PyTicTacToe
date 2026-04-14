from enum import Enum


# the player names. X always goes first. in the context of a grid, OPEN indicates
# that a player has not been assigned.
class Player(Enum):
    OPEN = 1
    X = 2
    O = 3

    # gives the opposite player. OPEN does not have an opposite and returns itself.
    def opposite(self):
        if self == Player.X: return Player.O
        if self == Player.O: return Player.X
        return Player.OPEN

    # string representation
    def __str__(self):
        if self == Player.X: return "X"
        if self == Player.O: return "O"
        return "-"
