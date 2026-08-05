import itertools
from config import DIMENSION, CANONICAL_BRICK, MY_DIRECTIONS, Brick, BrickDirection

def touching_bricks(
        brick: Brick,
        dimension: int = DIMENSION,
        directions: set[BrickDirection] = MY_DIRECTIONS
) -> set[Brick]:
    """
    Generate all bricks where:
      - All but one dimension overlap fully
      - The last dimension is tangent (touching)
    Returns a set of Brick tuples.
    """
    adjacent_bricks: set[Brick] = set()
    root = brick[:dimension]
    extent = brick[dimension:]

    for tangent_dimension in range(dimension):  # dimension that will only touch
        overlap_dimensions = [i for i in range(dimension) if i != tangent_dimension]

        for new_direction in directions:
            # Determine range for overlap dimensions (we align fully)
            overlap_positions = {i: range(root[i]-new_direction[i]+1, root[i] + extent[i]) for i in overlap_dimensions}

            # All combinations of positions in overlapping dimensions
            for possible_combination in itertools.product(*overlap_positions.values()):
                # Two possibilities for tangent dimension: before or after
                for sign in [-1, 1]:
                    new_root = [0] * dimension
                    # Set overlapping dimensions
                    for idx, dim in enumerate(overlap_dimensions):
                        new_root[dim] = possible_combination[idx]
                    # Set tangent dimension
                    if sign == -1:  # before
                        new_root[tangent_dimension] = root[tangent_dimension] - new_direction[tangent_dimension]
                    else:  # after
                        new_root[tangent_dimension] = root[tangent_dimension] + extent[tangent_dimension]

                    new_brick: Brick = tuple(new_root + list(new_direction))
                    adjacent_bricks.add(new_brick)

    return adjacent_bricks





if __name__ == "__main__":
    touch_positions_temp = touching_bricks(CANONICAL_BRICK)

    print('touching with standard brick', len(touch_positions_temp), touch_positions_temp)
