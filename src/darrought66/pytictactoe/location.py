# the GameState object keeps the play area in a dict that is keyed by integers. these method translate from integers to
# ordinates and vice versa.

"""
            (0,0)=0 (0,1)=1 (0,2)=2
            (1,0)=3 (1,1)=4 (1,2)=5
            (2,0)=6 (2,1)=7 (2,2)=8
"""

# convert ordinates to a location
def loc(row: int, col: int) -> int:
    return row * 3 + col


# extract column from a location
def col(loc: int) -> int:
    return loc % 3


# extract row from a location
def row(loc: int) -> int:
    return loc // 3
