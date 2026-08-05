from active_builder_config import create_building
from common.buildings.visualisation.draw_building import draw_building
from common.coloring_engine.satisfiability.colour_building import colour_building
from common.coloring_engine.linear_programming.colour_building_lp import colour_building_lp
from config import MY_DIRECTIONS
from common.graphs.draw_graph import draw_graph
from common.graphs.graph_from_building import graph_from_building
from common.buildings.extract_critical import extract_critical

"""Create a building, optionally extract critical, and analyze it."""

# ============================================================================
# CONFIGURATION
# ============================================================================
MAKE_CRITICAL = False
DRAW_GRAPH = False
NUMBER_OF_BRICKS = 200
NUMBER_OF_RANDOM_BRICKS = 4
INITIAL_GRID = 10
# ============================================================================


def main():
    """Create, analyze, and visualize a building."""

    print("\n" + "=" * 70)
    print("BUILDING and COLOURING")
    print("=" * 70)

    # Create building
    print("\nCreating building...")
    building = create_building(
        NUMBER_OF_BRICKS,
        NUMBER_OF_RANDOM_BRICKS,
        INITIAL_GRID,
        MY_DIRECTIONS
    )
    print(f"✓ Building created with {len(building)} bricks")

    # Extract critical if requested
    if MAKE_CRITICAL:
        print("\nExtracting critical building...")
        building = extract_critical(building)
        print(f"✓ Critical building has {len(building)} bricks")

    # Compute coloring
    print("\nComputing coloring...")
    colouring = colour_building(building)
    chromatic_number = colouring[0]
    color_map = colouring[1]
    print(f"✓ Chromatic number: {chromatic_number}")
    print(f"✓ Colour map: {color_map}")

    print("\n" + "=" * 70)
    print("VISUALIZATION")
    print("=" * 70)

    # Draw building
    print("\nDrawing 3D building...")
    draw_building(building, color_map)

    if DRAW_GRAPH:
        # Draw graph
        print("Drawing contact graph...")
        graph = graph_from_building(building)
        draw_graph(graph, color_map)

    print("\n" + "=" * 70)
    print("finished")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
