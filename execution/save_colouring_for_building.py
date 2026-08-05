# execution/extract_and_save_critical.py
"""Load building, extract critical bricks, and save."""

import re
from pathlib import Path
from common.buildings.storage.load_building import load_building
from common.coloring_engine.satisfiability.colour_building import colour_building
from common.buildings.storage.save_building import save_colouring


def main():
    """Extract critical building and save it."""

    print("\n" + "=" * 70)
    print("SAVE COLOURING FOR BUILDING")
    print("=" * 70 + "\n")

    # Get filepath from user
    filepath = input("Enter path to building file to colour: ").strip()

    try:
        # Load building
        print(f"\nLoading building...")
        print(f"  Path: {filepath}")
        building = load_building(filepath)
        print(f"✓ Loaded {len(building)} bricks")

        print(f"\nColouring building...")
        colouring = colour_building(building)
        print(f"✓ Building Needs {colouring[0]} Colours")
        print(f"  Coloruing map is {colouring[1]}")

        # Save colouring
        print(f"\nSaving colouring...")
        original_filename = Path(filepath).stem
        new_filename = save_colouring(filename=original_filename,colouring=colouring)
        print(f"✓ Saved as: {new_filename}")

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
