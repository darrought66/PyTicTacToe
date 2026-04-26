from enum import Enum


# this describes the state of the game; has a player won or tied?
class Status(Enum):
    UNDECIDED = 1
    X_WON = 2
    O_WON = 3
    TIE = 4

    # string representation
    def __str__(self):
        if self == Status.X_WON: return "X WINS"
        if self == Status.O_WON: return "O WINS"
        if self == Status.TIE: return "TIE"
        return "???"

    # convert string representation to object.
    @classmethod
    def from_str(cls, desc: str) -> Status:

        if desc == "X WINS": return Status.X_WON
        if desc == "O WINS": return Status.O_WON
        if desc == "TIE": return Status.TIE
        if desc == "???": return Status.UNDECIDED

        raise ValueError("Invalid status string")
