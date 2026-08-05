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
    "2x1_chi2":       limited_permutations((2,1), 2),
    "4x2x1_chi2":     limited_permutations((4,2,1), 2),
    "2x1x1_chi2":     limited_permutations((2,1,1), 2),
    "2x1x1_chi3":     limited_permutations((2,1,1), 3),
    "2x1x1x1_chi2":   limited_permutations((2,1,1,1), 2),
    "2x1x1x1x1_chi2": limited_permutations((2,1,1,1,1), 2),
}
# ============================================================================


def get_local_dimension(directions_local: set[BrickDirection]) -> int:
    """Return the spatial dimension (number of axes) implied by a set of BrickDirections."""
    return len(next(iter(directions_local)))


def split_brick(brick: Brick, local_dimension_temp: int) -> tuple[tuple, tuple]:
    """Split a brick tuple into its root (position) and direction (size) parts."""
    return brick[:local_dimension_temp], brick[local_dimension_temp:]


def test_brick_length_matches_dimension(test_building_temp: Building, local_dimension: int):
    """Test that every brick's tuple length is exactly root_dimension + direction_dimension"""
    expected_length = 2 * local_dimension
    bad_bricks = {brick for brick in test_building_temp if len(brick) != expected_length}
    if not bad_bricks:
        print(f"  ✅ PASSED — all {len(test_building_temp)} bricks have length {expected_length} "
              f"(root {local_dimension} + direction {local_dimension})")
    else:
        print(f"  ❌ FAILED — {len(bad_bricks)} brick(s) have wrong total length (expected {expected_length}):")
        for brick in bad_bricks:
            print(f"       {brick}  (length: {len(brick)})")


def test_brick_root_is_integer(test_building: Building, local_dimension: int):
    """Test that every brick's root (position) coordinates are integers"""
    bad_bricks = {
        brick for brick in test_building
        if not all(isinstance(coord, int) for coord in split_brick(brick, local_dimension)[0])
    }
    if not bad_bricks:
        print(f"  ✅ PASSED — all {len(test_building)} bricks have integer-valued roots")
    else:
        print(f"  ❌ FAILED — {len(bad_bricks)} brick(s) have non-integer root coordinates:")
        for brick in bad_bricks:
            print(f"       {brick}  (root: {split_brick(brick, local_dimension)[0]})")


def test_brick_are_correct_direction(test_building: Building, directions: set[BrickDirection], local_dimension: int):
    """Test that all bricks have a legal direction"""
    illegal_bricks = {
        brick for brick in test_building
        if split_brick(brick, local_dimension)[1] not in directions
    }
    if not illegal_bricks:
        print(f"  ✅ PASSED — all {len(test_building)} bricks use a legal direction from {directions}")
    else:
        print(f"  ❌ FAILED — {len(illegal_bricks)} brick(s) use an illegal direction:")
        for brick in illegal_bricks:
            print(f"       {brick}  (direction: {split_brick(brick, local_dimension)[1]})")


def test_brick_uses_all_directions(test_building: Building, directions: set[BrickDirection], local_dimension: int):
    """Test that every legal direction is actually used at least once in the building"""
    used_directions = {split_brick(brick, local_dimension)[1] for brick in test_building}
    missing_directions = directions - used_directions
    if not missing_directions:
        print(f"  ✅ PASSED — all {len(directions)} expected directions are used in the building")
    else:
        print(f"  ❌ FAILED — {len(missing_directions)} direction(s) never used: {missing_directions}")


def test_no_duplicate_roots(test_building: Building, local_dimension: int):
    """Test that no two bricks share the exact same root (position) — would imply overlap/duplication"""
    roots = [split_brick(brick, local_dimension)[0] for brick in test_building]
    duplicate_roots = {r for r in roots if roots.count(r) > 1}
    if not duplicate_roots:
        print(f"  ✅ PASSED — all {len(test_building)} bricks have unique roots")
    else:
        print(f"  ❌ FAILED — {len(duplicate_roots)} duplicate root(s) found: {duplicate_roots}")


if __name__ == "__main__":

    print("=" * 70)
    print("BRICK ROOT & DIRECTION TEST SUITE (multi-dimensional)")
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

        test_brick_length_matches_dimension(test_building, local_dimension)
        test_brick_root_is_integer(test_building, local_dimension)
        test_no_duplicate_roots(test_building, local_dimension)
        test_brick_are_correct_direction(test_building, directions, local_dimension)
        test_brick_uses_all_directions(test_building, directions, local_dimension)

    print()
    print("=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)
