from darrought66.tic_tac_toe.GameState import GameState


# prints a tree of game states
def print_tree(root_tree: GameState):
    print(str(root_tree) + "\n")  # print root game state
    print_tree0(root_tree, 1)  # print tree
    return


# prints tree of provided game state
def print_tree0(parent: GameState, depth: int):
    is_print = depth < 3

    for child in parent.children.values():
        if is_print: print(("\t" * depth) + str(child) + "\n")
        print_tree0(child, depth + 1)

    return
