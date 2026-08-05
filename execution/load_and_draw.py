# execution/load_and_draw_building.py
"""Load a building from file, compute coloring, and visualize it."""
from common.buildings.move_to_origin import move_building_to_origin

from common.buildings.storage.load_building import load_building
from common.coloring_engine.satisfiability.colour_building import colour_building
from common.buildings.visualisation.draw_building import draw_building


def main():
    """Load building and display it."""

    print("\n" + "=" * 70)
    print("LOAD AND VISUALIZE BUILDING")
    print("=" * 70 + "\n")

    # Get filepath from user
    filepath = input("Enter path to building file: ").strip()

    try:
        # Load building
        print(f"\nLoading building...")
        print(f"  Path: {filepath}")
        building = move_building_to_origin(load_building(filepath))
        print(f"✓ Loaded {len(building)} bricks")

        # Compute coloring
        print(f"\nComputing optimal coloring...")
        colouring = colour_building(building)
        chromatic_number = colouring[0]
        color_map = colouring[1]
        print(f"✓ Chromatic number: {chromatic_number}")

        # Visualize
        print(f"\nDrawing building...")
        draw_building(building, color_map)

        print("\n" + "=" * 70)
        print("Complete!")
        print("=" * 70 + "\n")

    except FileNotFoundError as e:
        print(f"\n✗ Error: File not found")
        print(f"  {e}\n")
    except Exception as e:
        print(f"\n✗ Error: {e}\n")


if __name__ == "__main__":
    main()
