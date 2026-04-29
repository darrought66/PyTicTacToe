from darrought66.pytictactoe.Outcome import Outcome
from darrought66.pytictactoe.Player import Player
from darrought66.pytictactoe.Status import Status
from darrought66.pytictactoe.evaluation import evaluate
from darrought66.pytictactoe.location import loc


# the 3 by 3 play area plus all associated state. this class is used as a node in a tree of all possible moves
# and outcomes. by inspection of any given node the application can determine the best move to make.
class GameState:
    class_count = 0  # number of classes instantiated, used for testing

    # create an empty game state
    def __init__(self):

        self.ordinal = GameState.class_count  # used as a key in db.
        GameState.class_count += 1 # because of this, only one tree can be created.
        # original game had 526,905 ordinals. you either fixed a bug or created one.
        if self.ordinal > 526905:
            raise Exception("ordinal max has been exceeded")

        self.play_area = {}
        for location in range(9):
            self.play_area[location] = Player.OPEN

        # tree is a doubly linked structure
        self.parent = None
        self.children = {}

        # has the game reached a terminal status; won, lost or tie?
        self.status = Status.UNDECIDED

        # this is what is the best that the player can do, if the other player chooses optimally.
        self.minimax = Outcome.NONE

        # lookahead is the union of child minimax. for choices with equal minimax the better lookahead should be chosen.
        # it means that the choice allows the other player to make suboptimal choices. for example choice 1 was a tie by
        # minimax, but a win could be obtained if the other player made a suboptimal choice. choice 2 is always tie.
        # you should choose 1 when playing a human player, as they notorious for making suboptimal choices.
        self.lookahead = Outcome.NONE

        # the move that was made to get from the parent state to this state. current player is kept for debugging
        # purposes. current location is used to locate a child game state based upon the move that created it.
        self.current_player = Player.OPEN
        self.current_location = -1

        return

    # string representation
    def __str__(self) -> str:

        # display STATUS MINIMAX LOOKAHEAD LOCATION PLAYER
        s = "(" + str(self.status) + " " + str(self.minimax) + " " + str(self.lookahead) + " " + str(
            self.current_location) + " " + str(
            self.current_player) + ") "

        # display play area data with rows separated by brackets.
        for row in range(3):
            s = s + " ["
            for col in range(3):
                if col == 0:
                    s = s + str(self.play_area[loc(row, col)])
                else:
                    s = s + " " + str(self.play_area[loc(row, col)])
            s = s + "]"

        return s

    # create a child game state with play area copied from parent plus one additional play.
    def create_child(self, location: int, player: Player) -> GameState:

        child = GameState()

        # copy states from parent
        for location0 in range(9):
            child.play_area[location0] = self.play_area[location0]

        # setup parent child relationship
        child.parent = self
        self.children[location] = child

        # make the one move the differs this child from its parent
        child.play_area[location] = player
        child.current_location = location
        child.current_player = player

        # set child's minimax, lookahead and status values.
        evaluate(child)

        return child

    # return a list of open locations.
    def open_locations(self) -> list[int]:

        open_locations = []
        for location in range(9):
            if self.play_area[location] == Player.OPEN:
                open_locations.append(location)

        return open_locations

    # return the child created by taking a given location.
    def get_child_by_location(self, loc: int) -> GameState:

        for child in self.children.values():
            if child.current_location == loc:
                return child

        # this method is used with open_locations method, so querying for an unknown location is a bug.
        raise Exception("No child with location " + str(loc))
