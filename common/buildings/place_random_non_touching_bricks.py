from config import MY_DIRECTIONS, DIMENSION, NOT_TOUCHING, Brick, BrickDirection
from common.bricks.touching_bricks import touching_bricks
from common.bricks.overlapping_bricks import overlapping_bricks
import random


def place_random_non_touching_bricks(
        num_rand_bricks: int,
        grid: int,
        directions: set[BrickDirection] = MY_DIRECTIONS,
        dimension: int = DIMENSION
) -> set[Brick]:

    placed_bricks: set[Brick] = set()
    illegal_bricks: set[Brick] = set()
    max_attempts = 500  # avoid infinite loops if grid too small

    attempts = 0
    while len(placed_bricks) < num_rand_bricks and attempts < max_attempts:
        attempts += 1

        # Random root position
        root = tuple(random.randint(0, grid - 1) for _ in range(dimension))
        # Random allowed orientation
        direction = random.choice(list(directions))
        candidate: Brick = root + direction

        # Check against all existing bricks
        if candidate not in illegal_bricks:
            placed_bricks.add(candidate)
            #add all touching and overlapping bricks to illegal bricks
            illegal_bricks |= touching_bricks(brick=candidate, dimension=dimension, directions=directions)
            illegal_bricks |= overlapping_bricks(brick=candidate, dimension=dimension, directions=directions)
            attempts = 0  # reset attempts after successful placement

    if len(placed_bricks) < num_rand_bricks:
        print(f"Warning: could only place {len(placed_bricks)} non-touching bricks in the grid")

    return placed_bricks