import random

from darrought66.pytictactoe.GameState import GameState
from darrought66.pytictactoe.Outcome import Outcome
from darrought66.pytictactoe.Player import Player
from darrought66.pytictactoe.Status import Status
from darrought66.pytictactoe.construct_state_tree import grow_tree, assign_outcome
from darrought66.pytictactoe.location import loc


# a command line version of the game for testing and basic use. this version generates and uses the solution space.

# draws a game state on a text console for simple play and debugging.
def display_game_state(gs: GameState):
    # iterate rows/cols
    for row in range(3):
        print("|", end="")

        for col in range(3):
            location = loc(row, col)

            if gs.play_area[location] == Player.OPEN:
                # use an location as a placeholder for unoccupied spots
                print(str(loc(row, col)) + "|", end="")
            else:
                print(str(gs.play_area[location]) + "|", end="")

        print("")
    print("")

    return


# query the user as to which player he would like to be.
def choose_player() -> Player:
    print("Player X always goes first")

    answers = ["X", "x", "O", "o"]
    chosen = " "
    while chosen not in answers:
        chosen = input("Do you want X or O ? ")

    return Player.X if chosen == "X" or chosen == "x" else Player.O


# query the user for which play he would like to make.
def read_users_choice(gs: GameState) -> int:
    answers = gs.open_locations()
    chosen = -1
    while chosen not in answers:
        chosen = int(input("Please enter your choice: "))

    return chosen


# choose the best move for the machine.
def make_machines_choice(gs: GameState) -> int:
    # explain the machines choice
    printout = {}

    # determine the best minimax
    max_child_outcome = Outcome.NONE
    for loc in gs.open_locations():
        child = gs.get_child_by_location(loc)
        # initialize the printout
        printout[loc] = str(child.minimax)
        # update max value when latest exceeds prior
        if max_child_outcome == Outcome.NONE or Outcome.is_better(max_child_outcome, child.minimax):
            max_child_outcome = child.minimax

    # collect all choices that give that minimax
    optimal_locations = []
    for loc in gs.open_locations():
        child = gs.get_child_by_location(loc)
        # copy children with optimal minimax to list
        if max_child_outcome == child.minimax:
            optimal_locations.append(loc)
            # update the printout
            printout[loc] = printout[loc] + " optimal"

    if len(optimal_locations) == 1:
        print_machine_choice(printout)
        return optimal_locations[0]

    # from the optimal choices determine the best lookahead
    max_range = Outcome.NONE
    for loc in optimal_locations:  # iterate only optimal choices
        child = gs.get_child_by_location(loc)
        # update best lookahead when latest exceeds prior
        if max_range == Outcome.NONE or Outcome.is_better(max_range, child.lookahead):
            max_range = child.lookahead

    # make a list of optimal choices with best lookahead
    best_locations = []
    for loc in optimal_locations:  # iterate only optimal choices
        child = gs.get_child_by_location(loc)
        # copy child to list if it has the maximum best_lookahead value
        if child.lookahead == max_range:
            # update the printout
            printout[loc] = printout[loc] + " best"
            best_locations.append(loc)

    if len(best_locations) == 1:
        print_machine_choice(printout)
        return best_locations[0]

    # randomly pick an option
    ndx = random.randint(0, len(best_locations) - 1)
    loc = best_locations[ndx]
    printout[loc] = printout[loc] + " random"
    return loc


# printout the options that the machine chose from
def print_machine_choice(printout: dict) -> None:
    tracing_on = True

    for loc in printout:
        if tracing_on: print(str(printout[loc]))

    if tracing_on: print("")

    return


# print a message summarizing the game status.
def print_status_msg(gs: GameState, player: Player):
    if gs.status == Status.X_WON and player == Player.X:
        print("Congratulations, You Won")
    elif gs.status == Status.X_WON and player == Player.O:
        print("Sorry, You Lost")

    if gs.status == Status.O_WON and player == Player.X:
        print("Sorry, You Lost")
    elif gs.status == Status.O_WON and player == Player.O:
        print("Congratulations, You Won")

    if gs.status == Status.TIE:
        print("The Game Was A Tie")

    return


# main line for the players turn
def players_turn(gs: GameState) -> GameState:
    loc = read_users_choice(gs)
    gs = gs.get_child_by_location(loc)
    display_game_state(gs)

    return gs


# main line for the machines turn
def machines_turn(gs: GameState) -> GameState:
    loc = make_machines_choice(gs)
    gs = gs.get_child_by_location(loc)
    display_game_state(gs)

    return gs


if __name__ == '__main__':

    print("Let's Play Tic Tac Toe")

    # create the solution space
    root_gs = GameState()
    grow_tree(root_gs, Player.X, 0)
    assign_outcome(root_gs)

    player = choose_player()
    # number turns 0 to 8 or 1 to 9
    turn = 0 if player == Player.X else 1
    max_turn = 8 if player == Player.X else 9
    gs = root_gs

    display_game_state(gs)  # display initial empty play area

    while gs.status == Status.UNDECIDED and turn <= max_turn:

        if turn % 2 == 0:
            gs = players_turn(gs)
        else:
            gs = machines_turn(gs)

        turn = turn + 1

    # print a summary (i.e. player won, lost or tied)
    print_status_msg(gs, player)
