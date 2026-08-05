from itertools import permutations
from pathlib import Path

"""Global configuration parameters."""

# Canonical setup
#CANONICAL_DIRECTION = (4, 2, 1)
CANONICAL_DIRECTION = (2, 1, 1)
DIMENSION:int = len(CANONICAL_DIRECTION)
CHI = 3
CANONICAL_BRICK = (0,) * DIMENSION + CANONICAL_DIRECTION

# Grid and building defaults
DEFAULT_GRID_SIZE = 10
DEFAULT_NUM_BRICKS = 50
DEFAULT_NUM_RANDOM_INIT = 10

# storage path
STORAGE_PATH = Path(__file__).parent / "building_storage"


# Datatypes
Brick = tuple[int, ...]
BrickDirection = tuple[int, ...]
Building = set[Brick]
TouchingType = str
ColourMap = list[str]
Colouring = [int,ColourMap]


# Touching type constants
TOUCHING = "touching"
NOT_TOUCHING = "nottouching"
OVERLAPPING = "overlapping"
TOUCHING_TYPES = {TOUCHING, NOT_TOUCHING, OVERLAPPING}

# Colors for coloring
COLORS = ['yellow', 'red', 'blue', 'white', 'black', 'green', 'cyan', 'magenta']



def all_permutations(
        canonical_direction:BrickDirection,
        dimension:int
)->set[BrickDirection]:
    return set(permutations(canonical_direction, dimension))

def limited_permutations(
        direction:BrickDirection,
        perm:int
) -> set[BrickDirection]:
    first_part = direction[:perm]
    rest = direction[perm:]
    return {p + rest for p in permutations(first_part)}


ALL_DIRECTIONS = all_permutations(CANONICAL_DIRECTION, DIMENSION)
MY_DIRECTIONS = limited_permutations(CANONICAL_DIRECTION, CHI)

if __name__ == "__main__":
    print('all directions ', len(ALL_DIRECTIONS), ALL_DIRECTIONS)
    print('my directions ', len(MY_DIRECTIONS), MY_DIRECTIONS)