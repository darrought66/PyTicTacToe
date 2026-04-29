from math import factorial

from pympler import asizeof
import time
from darrought66.pytictactoe.GameState import GameState
from darrought66.pytictactoe.Player import Player
from darrought66.pytictactoe.construct_state_tree import grow_tree, assign_outcome

# 363 megabytes
def print_memory():
    root_gs = GameState()
    grow_tree(root_gs, Player.X, 0)
    assign_outcome(root_gs)
    print(asizeof.asizeof(root_gs) / 1024 / 1024)
    return

# 986,411
def print_max_nodes():
    count = 1
    for i in range(10):
        count += factorial(9) / factorial(i)
    print(count)
    return

# 526,906 = 53.4%
def print_actual_nodes():
    root_gs = GameState()
    grow_tree(root_gs, Player.X, 0)
    assign_outcome(root_gs)
    print(GameState.class_count)
    return

# 6.89 seconds
def generation_time():
    start = time.time_ns()
    root_gs = GameState()
    grow_tree(root_gs, Player.X, 0)
    assign_outcome(root_gs)
    end = time.time_ns()
    change = (end - start) / (1000 * 1000 * 1000)
    print(change)
    return

if __name__ == '__main__':
    ch = 1
    if ch == 0:
        print_memory()
    elif ch == 1:
        print_max_nodes()
    elif ch == 2:
        print_actual_nodes()
    elif ch == 3:
        generation_time()
