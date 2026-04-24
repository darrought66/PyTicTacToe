# the GameState object keeps the play area in a dict that is keyed by integers. these method translate from integers to
# ordinates and vice versa.

# 1 2 3
# 4 5 6
# 7 8 9

# convert ordinates to a location
def loc(row: int, col: int) -> int:
    return row * 3 + col


# extract column from a location
def col(loc: int) -> int:
    return loc % 3


# extract row from a location
def row(loc: int) -> int:
    return loc // 3
