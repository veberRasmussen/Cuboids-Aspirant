from config import DIMENSION, Brick, Building, MY_DIRECTIONS, BrickDirection, limited_permutations, OVERLAPPING
from active_builder_config import create_building
from common.bricks.touch_type import touch_type

# ============================================================================
# CONFIGURATION
# ============================================================================
NUMBER_OF_BRICKS = 50
NUMBER_OF_RANDOM_BRICKS = 10
INITIAL_GRID = 10

TEST_DIRECTIONS = {
    "4x2x1_chi2": limited_permutations((4,2,1),2),
    "2x1x1_chi2": limited_permutations((2,1,1),2),
    "2x1x1_chi3": limited_permutations((2,1,1),3),
    "2x2x1_chi3": limited_permutations((2, 2, 1), 3)
}
# ============================================================================


def get_local_dimension(directions: set[BrickDirection]) -> int:
    """Return the spatial dimension (number of axes) implied by a set of BrickDirections."""
    return len(next(iter(directions)))


def test_brick_are_correct_direction(test_building: Building, directions: set[BrickDirection], local_dimension: int):
    """Test that all bricks have a legal direction"""
    illegal_bricks = {brick for brick in test_building if brick[local_dimension:] not in directions}
    if not illegal_bricks:
        print(f"  ✅ PASSED — all {len(test_building)} bricks use a legal direction from {directions}")
    else:
        print(f"  ❌ FAILED — {len(illegal_bricks)} brick(s) use an illegal direction:")
        for brick in illegal_bricks:
            print(f"       {brick}  (direction: {brick[local_dimension:]})")


def test_brick_uses_all_directions(test_building: Building, directions: set[BrickDirection], local_dimension: int):
    """Test that every legal direction is actually used at least once in the building"""
    used_directions = {brick[local_dimension:] for brick in test_building}
    missing_directions = directions - used_directions
    if not missing_directions:
        print(f"  ✅ PASSED — all {len(directions)} expected directions are used in the building")
    else:
        print(f"  ❌ FAILED — {len(missing_directions)} direction(s) never used: {missing_directions}")


if __name__ == "__main__":

    print("=" * 70)
    print("BRICK DIRECTION TEST SUITE")
    print("=" * 70)
    print(f"number_of_bricks:        {NUMBER_OF_BRICKS}")
    print(f"number_of_random_bricks: {NUMBER_OF_RANDOM_BRICKS}")
    print(f"grid_size:               {INITIAL_GRID}")
    print()
    print(f"Testing {len(TEST_DIRECTIONS)} direction sets:")
    for name, directions in TEST_DIRECTIONS.items():
        print(f"  - {name}: {directions}")
    print("=" * 70)

    for direction_name, directions in TEST_DIRECTIONS.items():
        local_dimension = get_local_dimension(directions)

        print()
        print("-" * 70)
        print(f"CASE: {direction_name}  (dimension={local_dimension})")
        print(f"Allowed directions: {directions}")
        print("-" * 70)

        test_building = create_building(
            NUMBER_OF_BRICKS, NUMBER_OF_RANDOM_BRICKS, INITIAL_GRID, directions, local_dimension
        )

        print(f"Built {len(test_building)} / {NUMBER_OF_BRICKS} requested bricks")
        print(f"Building: {test_building}")
        print()

        test_brick_are_correct_direction(test_building, directions, local_dimension)
        test_brick_uses_all_directions(test_building, directions, local_dimension)

    print()
    print("=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)
