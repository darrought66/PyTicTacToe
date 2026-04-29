from darrought66.pytictactoe.GameState import GameState
from darrought66.pytictactoe.Outcome import Outcome
from darrought66.pytictactoe.Player import Player
from darrought66.pytictactoe.Status import Status
from darrought66.pytictactoe.debug_test_util import print_tree


# these methods construct the solution space, which is a doubly linked tree of GameState objects.

# creates a tree of game states.
def grow_tree(gs: GameState, player: Player, depth: int):
    # guard clause, depth = 0 is empty game. there are 9 spots in the game. therefore should never go deeper than 9.
    if depth > 9:
        raise RuntimeError("depth exceeded 10")

    open_locations = gs.open_locations()

    if len(open_locations) == 0:
        return

    for location in open_locations:
        child = gs.create_child(location, player)
        # status is set for terminal game states. do not generate past a terminal state.
        if child.status == Status.UNDECIDED:
            grow_tree(child, player.opposite(), depth + 1)

    return


# after the tree has been constructed then minimax values must be assigned to each node. the evaluations start from the
# leaves and proceed towards the root.
def assign_outcome(gs: GameState) -> Outcome:
    # if the game state minimax has not been calculated then calculate it
    if gs.minimax == Outcome.NONE:

        # calculate the minimax for each child that has not been calculated by recursive call
        for child in gs.children.values():
            if child.minimax == Outcome.NONE:
                assign_outcome(child)

            # the best option assuming the other player makes the optimal choice
            gs = minimax(gs, child)

        # this players minimax is the opposite of that for the other player.
        gs.minimax = gs.minimax.reverse()

        # the lookahead is the union of child minimax
        gs.lookahead = Outcome.NONE  # safety, should already be true
        for child in gs.children.values():
            gs.lookahead = calc_lookahead(gs, child)

        # this players minimax is the opposite of that for the other player.
        gs.lookahead = gs.lookahead.reverse()

    return gs.minimax


# calculate the lookahead
def calc_lookahead(gs: GameState, child: GameState) -> Outcome:
    if gs.lookahead == Outcome.NONE:
        gs.lookahead = child.minimax
    else:
        gs.lookahead = Outcome.union(gs.lookahead, child.minimax)

    return gs.lookahead


# calculate the best option assuming the other player will choose optimally
def minimax(gs: GameState, child: GameState) -> GameState:
    if gs.minimax == Outcome.NONE:
        gs.minimax = child.minimax
    elif Outcome.is_better(gs.minimax, child.minimax):
        gs.minimax = child.minimax

    return gs


# debugging. prints out the solution space for visual inspection.
if __name__ == '__main__':
    # create the solution space
    root_gs = GameState()
    grow_tree(root_gs, Player.X, 0)
    assign_outcome(root_gs)

    print_tree(root_gs)
