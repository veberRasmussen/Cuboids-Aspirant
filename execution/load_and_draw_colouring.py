"""Load a colouring from file and visualize it."""

from common.buildings.storage.load_colouring import load_colouring
from common.buildings.visualisation.draw_building import draw_building


def main():
    """Load a colouring and display it."""

    print("\n" + "=" * 70)
    print("LOAD AND VISUALIZE COLOURING")
    print("=" * 70 + "\n")

    filepath = input("Enter path to colouring file: ").strip()

    try:
        print("\nLoading colouring...")
        print(f"  Path: {filepath}")

        chromatic_number, colour_map = load_colouring(filepath)

        print(f"✓ Loaded {len(colour_map)} bricks")
        print(f"✓ Chromatic number: {chromatic_number}")

        print("\nDrawing building...")

        draw_building(colour_map)

        print("\n" + "=" * 70)
        print("Complete!")
        print("=" * 70 + "\n")

    except FileNotFoundError as e:
        print("\n✗ Error: File not found")
        print(f"  {e}\n")

    except Exception as e:
        print(f"\n✗ Error: {e}\n")


if __name__ == "__main__":
    main()