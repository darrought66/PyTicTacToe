from enum import Enum


# the player names. X always goes first.
class Player(Enum):
    OPEN = 1  # indicates that no player has not been assigned to the spot.
    X = 2
    O = 3

    # string representation
    def __str__(self):
        if self == Player.X: return "X"
        if self == Player.O: return "O"
        return "-"

    # convert string representation to object.
    @classmethod
    def from_str(cls, desc: str) -> "Player":
        if desc == "X": return Player.X
        if desc == "O": return Player.O
        if desc == "-": return Player.OPEN

        raise ValueError("Invalid player string")

    # gives the opposite player. OPEN does not have an opposite and returns itself.
    def opposite(self) -> "Player":
        if self == Player.X: return Player.O
        if self == Player.O: return Player.X
        return self
