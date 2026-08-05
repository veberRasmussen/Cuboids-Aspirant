import itertools
from config import DIMENSION, CANONICAL_BRICK, MY_DIRECTIONS, Brick, BrickDirection

def overlapping_bricks(
        brick: Brick,
        dimension: int = DIMENSION,
        directions: set[BrickDirection] = MY_DIRECTIONS
) -> set[Brick]:
    """
    Generate all bricks that overlap (not just touch) with the given brick.
    Each overlap means: intervals intersect in every dimension.
    Returns a set of Brick tuples.
    """
    overlapping_bricks_temp: set[Brick] = set()
    root = brick[:dimension]
    direction = brick[dimension:]

    for new_dir in directions:
        # For each dimension, generate all positions that lead to overlap
        possible_ranges = []
        for i in range(dimension):
            a_start = root[i]
            a_end = root[i] + direction[i]
            # To overlap, the new brick's start must be < a_end and end > a_start
            # That means: start ∈ [a_start - new_dir[i] + 1, a_end - 1]
            start_min = a_start - new_dir[i] + 1
            start_max = a_end - 1
            possible_ranges.append(range(start_min, start_max + 1))

        # Cartesian product over all possible root coordinates
        for coords in itertools.product(*possible_ranges):
            new_brick = tuple(coords) + new_dir
            overlapping_bricks_temp.add(new_brick)

    return overlapping_bricks_temp

if __name__ == "__main__":
    overlapping_positions_temp = overlapping_bricks(CANONICAL_BRICK)

    print('overlapping with standard brick', len(overlapping_positions_temp), overlapping_positions_temp)
