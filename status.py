from enum import Enum


# this is a state specific outcome. in other words this state represents a WIN
# or a TIE. notice that while Outcome is relative to the player this is absolute.
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


# this speaks to a subtree. in other words WIN indicates that every path leads
# to a WIN regardless of what the opponent chooses. TIE_OR_BETTER indicates
# every path leads to a WIN or TIE regardless of what the opponent chooses.
class Outcome:

    # call once to create singleton values.
    @classmethod
    def define_singletons(cls):

        # sort by worst outcome, then subsort by best outcome
        cls.WIN = Outcome("W__")
        cls.TIE_OR_BETTER = Outcome("WT_")
        cls.TIE = Outcome("_T_")
        cls.ANY = Outcome("WTL")
        cls.WIN_OR_LOSE = Outcome("W_L")
        cls.TIE_OR_WORSE = Outcome("_TL")
        cls.LOSE = Outcome("__L")
        # NONE only occurs before the variable is initialized.
        cls.NONE = Outcome("___")

        # these are ordered from worst to best. the purpose is to convert a
        # singleton into an ordinal.
        cls.values = [cls.NONE, cls.LOSE, cls.TIE_OR_WORSE, cls.WIN_OR_LOSE, cls.ANY, cls.TIE, cls.TIE_OR_BETTER,
                      cls.WIN]

        return

    # used to create singletons
    def __init__(self, code):
        self.code = code
        return

    # string representation
    def __str__(self):
        return self.code

    # takes the union of two sets of possible outcomes.
    def union(self, p):

        # for a given position there are only two possibilities. for example
        # the first position will have W or _. Underscore represents not having
        # an element. so union takes the letter if either code has it.

        s = ""
        for i in range(3):
            if self.code[i] == "_" and p.code[i] == "_":
                s = s + "_"
            elif self.code[i] == "_":
                s = s + p.code[i]  # p must have letter
            else:
                s = s + self.code[i]  # self must have letter

        return from_code(s)

    # takes the intersection of two sets of possible outcomes.
    def intersection(self, p):

        # for a given position there are only two possibilities. for example the
        # first position will have W or _. Underscore represents not having an
        # element. so intersection takes the letter if both codes have it.

        s = ""
        for i in range(3):
            if self.code[i] == '_' or p.code[i] == '_':
                s = s + "_"
            else:
                # neither is underscore, so either would work.
                s = s + self.code[i]

        return from_code(s)

    # convert the outcome from one players point of view to the others. in other
    # words a win for X is a loss for O.
    def reverse(self):

        s = Outcome.NONE
        if self.code[0] == "W":
            s = s.union(Outcome.LOSE)
        if self.code[1] == "T":
            s = s.union(Outcome.TIE)
        if self.code[2] == "L":
            s = s.union(Outcome.WIN)

        return s


# returns a outcome from a code value. useful internally for implementing
# set operations.
def from_code(code):
    for s in Outcome.values:
        if code == s.code: return s

    raise RuntimeError("unknown outcome code: " + code)
