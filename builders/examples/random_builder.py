import random
from config import BrickDirection, Building, OVERLAPPING, MY_DIRECTIONS, DIMENSION
from common.bricks.touch_type import touch_type


def random_builder(
        number_of_bricks: int,
        number_random_bricks: int,
        grid_size: int = 10,
        directions: set[BrickDirection] = MY_DIRECTIONS,
        dimension:int = DIMENSION
) -> Building:

    building: Building = set()
    directions_list = list(directions)
    max_attempts = number_of_bricks * 5

    attempts = 0

    while len(building) < number_of_bricks and attempts < max_attempts:
        attempts += 1

        root = (random.randint(0, grid_size - 1),random.randint(0, grid_size - 1),random.randint(0, grid_size - 1))
        direction = random.choice(directions_list)
        brick = root + direction

        overlaps = any(
            touch_type(brick, existing) == OVERLAPPING
            for existing in building
        )

        if not overlaps:
            building.add(brick)

    return building