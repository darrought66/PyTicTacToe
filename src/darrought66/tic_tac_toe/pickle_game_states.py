import pickle

from darrought66.tic_tac_toe.GameState import GameState


# it is useful for unit testing for better performance to generate the solution space once and keep it in file.

# serialize entire game tree to a file.
def pickle_game_tree(root_gs: GameState):
    with open("tic_tac_toe_game_tree.pkl", "wb") as file:
        pickle.dump(root_gs, file)
    return


# restore entire game tree from a file.
def restore_game_tree() -> GameState:
    with open("tic_tac_toe_game_tree.pkl", "rb") as file:
        root_gs = pickle.load(file)
    return root_gs
