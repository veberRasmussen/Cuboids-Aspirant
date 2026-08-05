import networkx as nx
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


def test_building_graph_is_connected(number_of_bricks: int = 50):
    """Test that the contact graph is connected."""
    building = create_building(number_of_bricks, number_random_bricks = NUMBER_OF_RANDOM_BRICKS, grid_size=INITIAL_GRID, directions=MY_DIRECTIONS)
    graph = graph_from_building(building)

    # Check if graph is connected
    if not nx.is_connected(graph):
        print("FAILED: Contact graph is not connected for test with ", number_of_bricks)
    else:
        print("PASSED: Contact graph is connected for test with ", number_of_bricks)


if __name__ == "__main__":
    print("Running test for if graph is connected with parameters:" )
    print("number_random_bricks: ", NUMBER_OF_RANDOM_BRICKS)
    print("grid_size: ", INITIAL_GRID)
    print("directions: ", MY_DIRECTIONS)
    print("")
    for test_run in TEST_RUNS:
        test_building_graph_is_connected(test_run)

