import itertools
from config import DIMENSION, TOUCHING, OVERLAPPING, NOT_TOUCHING, Brick

def touch_type(
        brick1: Brick,
        brick2: Brick,
        dimension: int = DIMENSION
) -> str:
    """
    Determine the touch type between two bricks:
      - "overlapping" if they overlap in all dimensions
      - "touching" if they overlap in all but one dimension and are tangent in that one
      - "nottouching" if there are more than one non-overlapping dimension
    """
    overlap_count = 0
    tangent_count = 0

    for i in range(dimension):
        start1, end1 = brick1[i], brick1[i] + brick1[dimension + i]
        start2, end2 = brick2[i], brick2[i] + brick2[dimension + i]

        if end1 <= start2 or end2 <= start1:
            # no overlap in this dimension
            if end1 == start2 or end2 == start1:
                tangent_count += 1  # exactly touching
            else:
                return NOT_TOUCHING  # gap => not touching
        else:
            # some overlap in this dimension
            overlap_count += 1

    if overlap_count == dimension:
        return OVERLAPPING
    elif overlap_count == dimension - 1 and tangent_count == 1:
        return TOUCHING
    else:
        return NOT_TOUCHING

