from enum import Enum


# this is a state specific status. in other words this state represents a WIN or a TIE.
class Status(Enum):

    UNDECIDED = 1
    X_WON = 2
    O_WON = 3
    TIE = 4

    # string representation
    def __str__(self):
        if self == Status.X_WON: return "X  "
        if self == Status.O_WON: return "O  "
        if self == Status.TIE: return "TIE"
        return "???"

# this speaks to an subtree. in other words WIN indicates that there is a path to WIN
# regardless of what the opponent chooses. this value is always interpreted in terms
# of the current player.
class TreeStatus:

    # call once to create singleton values.
    @classmethod
    def define_singletons(cls):

        cls.LOSE = TreeStatus("__L")
        cls.TIE_OR_WORSE = TreeStatus("_TL")
        cls.ANY = TreeStatus("WTL")
        cls.TIE = TreeStatus("_T_")
        cls.TIE_OR_BETTER = TreeStatus("WT_")
        cls.WIN = TreeStatus("W__")
        cls.WIN_OR_LOSE = TreeStatus("W_L")

        # NONE only occurs before the variable is initialized. for that reason
        # it is not included in values.
        cls.NONE = TreeStatus("___")

        # these are ordered from worst to best.
        cls.values = [cls.WIN, cls.TIE_OR_BETTER, cls.TIE, cls.ANY, cls.WIN_OR_LOSE, cls.TIE_OR_WORSE, cls.LOSE]

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

        # for a given position there are only two possibilities. for example the
        # first position will have W or _. Underscore represents not having an
        # element. so union takes the letter if either code has it.

        s = ""
        for i in range(3):
            if self.code[i] == "_" and p.code[i] == "_":
                s = s + "_"
            elif self.code[i] == "_":
                s = s + p.code[i]  # p must have letter
            else:
                s = s + self.code[i]  # self must have letter

        return self.from_code(s)

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

        return self.from_code(s)

    # reverse the meaning
    def reverse(self):

        s = TreeStatus.NONE
        if self.code[0] == "W":
            s = s.union(TreeStatus.LOSE)
        if self.code[1] == "T":
            s = s.union(TreeStatus.TIE)
        if self.code[2] == "L":
            s = s.union(TreeStatus.WIN)

        return s

    # returns a tree status from a code value. useful internally for implementing
    # set operations.
    def from_code(self, code):

        for s in TreeStatus.values:
            if code == s.code: return s

        if code == "___":
            return TreeStatus.NONE

        raise RuntimeError("unknown tree status code: " + code)
