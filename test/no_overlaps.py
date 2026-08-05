from config import DIMENSION, Brick, Building, MY_DIRECTIONS, OVERLAPPING
from active_builder_config import create_building
from common.bricks.touch_type import touch_type

# ============================================================================
# CONFIGURATION
# ============================================================================
NUMBER_OF_BRICKS = 50
NUMBER_OF_RANDOM_BRICKS = 10
INITIAL_GRID = 10
# ============================================================================


def bricks_overlap(brick1: Brick, brick2: Brick, dimension:int=DIMENSION) -> bool:
    """Check if two bricks overlap."""
    return touch_type(brick1, brick2, dimension=dimension) == OVERLAPPING


def test_no_overlaps_in_building(test_building_temp: Building, dimension:int= DIMENSION):
    """Test that the built building has no overlapping bricks."""
    bricks_list = list(test_building_temp)
    overlapping_pairs = []

    for i in range(len(bricks_list)):
        for j in range(i + 1, len(bricks_list)):
            if bricks_overlap(bricks_list[i], bricks_list[j], dimension=dimension):
                overlapping_pairs.append((bricks_list[i], bricks_list[j]))

    if not overlapping_pairs:
        print("PASSED: no overlapping bricks in building")
    else:
        print(f"FAILED: found {len(overlapping_pairs)} overlapping brick pairs:")
        for brick1, brick2 in overlapping_pairs:
            print(f"  {brick1} overlaps {brick2}")


if __name__ == "__main__":

    print("Running test for if graph is connected with parameters:" )
    print("number_of_bricks: ", NUMBER_OF_BRICKS)
    print("number_random_bricks: ", NUMBER_OF_RANDOM_BRICKS)
    print("grid_size: ", INITIAL_GRID)
    print("directions: ", MY_DIRECTIONS)
    print("")

    test_building = create_building(NUMBER_OF_BRICKS,NUMBER_OF_RANDOM_BRICKS, INITIAL_GRID, MY_DIRECTIONS)
    print("test building is: ", test_building)
    print("")

    test_no_overlaps_in_building(test_building)