from config import DIMENSION, Brick, Building, MY_DIRECTIONS
from active_builder_config import create_building

# ============================================================================
# CONFIGURATION
# ============================================================================
NUMBER_OF_BRICKS = 50
NUMBER_OF_RANDOM_BRICKS = 10
INITIAL_GRID = 10
# ============================================================================


def test_brick_is_tuple(test_building:Building):
    """Test that bricks are tuples."""
    if all(isinstance(brick, tuple) for brick in test_building):
        print("PASSED: all bricks in building are tuples")
    else:
        print("FAILED: not all bricks in building are tuples: ", test_building)


def test_brick_has_correct_length(test_building:Building):
    """Test that bricks have correct length (2*dimension)."""
    if all(len(brick) == 2 * DIMENSION for brick in test_building):
        print("PASSED: all bricks in building are length 2*DIMENSION")
    else:
        print("FAILED: not all bricks in building are length 2*DIMENSION: ", test_building)

def test_brick_elements_are_integers(test_building:Building):
    """Test that all brick elements are integers."""
    if all(all(isinstance(coord, int) for coord in brick) for brick in test_building):
        print("PASSED: all bricks in building has integer coordinates")
    else:
        print("FAILED: not all bricks in building has integer coordinates: ", test_building)

def test_building_is_set(test_building:Building):
    """Test that building is a set."""
    if isinstance(test_building, set):
        print("PASSED: building is a set")
    else:
        print("FAILED: building is NOT a set: ", test_building)


if __name__ == "__main__":


    print("Running test for if graph is connected with parameters:" )
    print("number_of_bricks: ", NUMBER_OF_BRICKS)
    print("number_random_bricks: ", NUMBER_OF_RANDOM_BRICKS)
    print("grid_size: ", INITIAL_GRID)
    print("directions: ", MY_DIRECTIONS)
    print("")

    my_test_building = create_building(NUMBER_OF_BRICKS, NUMBER_OF_RANDOM_BRICKS, INITIAL_GRID, MY_DIRECTIONS)
    print("test building is ", my_test_building)
    print("")

    test_brick_is_tuple(my_test_building)
    test_brick_has_correct_length(my_test_building)
    test_brick_elements_are_integers(my_test_building)
    test_building_is_set(my_test_building)



