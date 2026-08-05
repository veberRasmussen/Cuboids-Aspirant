from common.graphs.graph_from_building import graph_from_building
from active_builder_config import create_building
from config import MY_DIRECTIONS

# ============================================================================
# CONFIGURATION
# ============================================================================
NUMBER_OF_RANDOM_BRICKS = 5
INITIAL_GRID = 10
TEST_RUNS = [5, 10, 25, 50, 100]
# ============================================================================


def test_correct_brick_amount(target_bricks: int = 50):
    """Test that builder creates correct number of bricks."""
    building = create_building(target_bricks, number_random_bricks = NUMBER_OF_RANDOM_BRICKS, grid_size=INITIAL_GRID, directions=MY_DIRECTIONS)

    assert len(building) == target_bricks, \
        f"Expected {target_bricks} bricks, got {len(building)}"

    if not len(building) == target_bricks:
        print("FAILED: number of bricks is NOT the expected", target_bricks)
    else:
        print("PASSED: number of bricks is the expected", target_bricks)


if __name__ == "__main__":
    print("Running test for correct number of bricks with parameters:" )
    print("number_random_bricks: ", NUMBER_OF_RANDOM_BRICKS)
    print("grid_size: ", INITIAL_GRID)
    print("directions: ", MY_DIRECTIONS)
    print("")
    for test_run in TEST_RUNS:
        test_correct_brick_amount(test_run)