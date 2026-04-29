from enum import Enum


# outcome is used to describe ranges of game outcomes, such as required for minimax and lookahead variables.
class Outcome(Enum):
    WIN = "W__"
    TIE_OR_BETTER = "WT_"
    TIE = "_T_"
    ANY = "WTL"
    WIN_OR_LOSE = "W_L"
    TIE_OR_WORSE = "_TL"
    LOSE = "__L"
    NONE = "___"  # only occurs before a variable is initialized.

    # these are ordered from worst to best. the purpose is to convert a singleton into an ordinal.
    @classmethod
    def ordinal(cls, outcome):
        return [Outcome.NONE, Outcome.LOSE, Outcome.TIE_OR_WORSE, Outcome.WIN_OR_LOSE, Outcome.ANY, Outcome.TIE,
                Outcome.TIE_OR_BETTER, Outcome.WIN].index(outcome)

    # used to create singletons
    def __init__(self, code: str):
        self.code = code
        return

    # string representation
    def __str__(self):
        return self.code

    # convert string representation to object.
    @classmethod
    def from_str(cls, desc: str) -> Outcome:

        for s in Outcome:
            if desc == s.code:
                return s

        raise ValueError("Invalid status string")

    # takes the union of two sets of possible outcomes.
    def union(self, p: Outcome) -> Outcome:

        # for a given position there are only two possibilities. for example the first position will have W or _.
        # Underscore represents not having an element. so union takes the letter if either code has it.

        s = ""
        for i in range(3):
            # if element missing in both the assign underscore
            if self.code[i] == "_" and p.code[i] == "_":
                s = s + "_"
            # whichever one has underscore assign the other one, since one of them has code.
            elif self.code[i] == "_":
                s = s + p.code[i]  # p must have letter
            else:
                s = s + self.code[i]  # self must have letter

        # convert to object
        return Outcome.from_str(s)

    # convert the Outcome from one players point of view to the others.
    def reverse(self) -> Outcome:

        s = Outcome.NONE
        if self.code[0] == "W":
            s = s.union(Outcome.LOSE)
        if self.code[1] == "T":
            s = s.union(Outcome.TIE)
        if self.code[2] == "L":
            s = s.union(Outcome.WIN)

        return s

    # return true if P is preferable to Q
    @classmethod
    def is_better(cls, p: Outcome, q: Outcome) -> bool:
        return cls.ordinal(p) < cls.ordinal(q)
