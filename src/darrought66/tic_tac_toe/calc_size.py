from math import factorial

from pympler import asizeof
import math
import time
from darrought66.tic_tac_toe.GameState import GameState
from darrought66.tic_tac_toe.Player import Player
from darrought66.tic_tac_toe.construct_state_tree import grow_tree, assign_outcome

# 363 megabytes
def print_size():
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
def print_actual_size():
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

#print_size()
#print_max_nodes()
#print_actual_size()
#generation_time()