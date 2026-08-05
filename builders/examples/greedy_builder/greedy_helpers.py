import random
from config import Brick, Building, BrickDirection
from common.bricks.touch_type import touch_type
from common.bricks.touching_bricks import touching_bricks
from config import OVERLAPPING


def create_first_brick(directions: set[BrickDirection], dimension: int) -> Brick:
    """Create a single starting brick at the origin, with a random direction."""
    first_root = (0,)*dimension
    return first_root + random.choice(list(directions))


def get_all_candidates(
        building: list[Brick],
        directions: set[BrickDirection],
        dimension: int
) -> set[Brick]:
    """Gather every candidate position touching any brick currently in the building."""
    candidates: set[Brick] = set()
    for existing_brick in building:
        candidates |= touching_bricks(brick=existing_brick, dimension=dimension, directions=directions)
    return candidates


def is_legal(candidate: Brick, building: list[Brick], dimension: int) -> bool:
    """Check whether a candidate brick overlaps with any brick already in the building."""
    return not any(
        touch_type(candidate, existing_brick, dimension=dimension) == OVERLAPPING
        for existing_brick in building
    )


def get_legal_candidates(
        candidates: set[Brick],
        building: list[Brick],
        dimension: int
) -> list[Brick]:
    """Filter a set of candidates down to only those that don't overlap the building."""
    return [candidate for candidate in candidates if is_legal(candidate, building, dimension=dimension)]
