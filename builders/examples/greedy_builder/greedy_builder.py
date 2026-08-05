import random
from config import BrickDirection, Building, Brick, MY_DIRECTIONS, DIMENSION
from builders.examples.greedy_builder.greedy_helpers import (
    create_first_brick, get_all_candidates, get_legal_candidates
)


def greedy_builder(
        number_of_bricks: int,
        number_random_bricks: int = 1,
        grid_size: int = 10,
        directions: set[BrickDirection] = MY_DIRECTIONS,
        dimension: int = DIMENSION
) -> Building:
    """
    A greedy builder that grows a building one brick at a time, checking each
    candidate directly against every brick already placed.
    """
    building: list[Brick] = [create_first_brick(directions, dimension)]

    while len(building) < number_of_bricks:
        candidates = get_all_candidates(building, directions, dimension)
        legal_candidates = get_legal_candidates(candidates, building, dimension)

        if not legal_candidates:
            break  # no legal candidate found, stop early

        building.append(random.choice(legal_candidates))

    return set(building)
