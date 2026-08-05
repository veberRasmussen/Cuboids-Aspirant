# execution/extract_and_save_critical.py
"""Load building, extract critical bricks, and save."""

import re
from pathlib import Path
from common.buildings.storage.load_building import load_building
from common.buildings.extract_critical import extract_critical, extract_critical_combined
from common.buildings.storage.save_building import save_building

def update_filename_with_critical(original_filename: str, new_size: int) -> str:
    """
    Update filename to reflect critical building.

    If filename matches format: xxx_chi{p}_colours{c}_{date}_{index}_size{s}...
    Updates the size (size{s}) and adds _critical suffix.

    Otherwise just appends _critical to filename.
    """
    # Pattern: size{number} (size indicator)
    size_pattern = r'(_size)(\d+)'

    # Check if filename matches the expected format
    if re.search(size_pattern, original_filename):
        # Replace the size with new size and add _critical
        updated = re.sub(size_pattern, rf'\g<1>{new_size}', original_filename)
        return f"{updated}_critical"
    else:
        # Just append _critical if format doesn't match
        return f"{original_filename}_critical"


def main():
    """Extract critical building and save it."""

    print("\n" + "=" * 70)
    print("EXTRACT CRITICAL BUILDING")
    print("=" * 70 + "\n")

    # Get filepath from user
    filepath = input("Enter path to building file: ").strip()

    try:
        # Load building
        print(f"\nLoading building...")
        print(f"  Path: {filepath}")
        building = load_building(filepath)
        print(f"✓ Loaded {len(building)} bricks")

        # Extract critical
        print(f"\nExtracting critical building...")
        building_critical = extract_critical(building)
        reduction = len(building) - len(building_critical)
        percent = (reduction / len(building) * 100) if len(building) > 0 else 0
        print(f"✓ Critical building has {len(building_critical)} bricks")
        print(f"  Removed {reduction} bricks ({percent:.1f}%)")

        # Save critical
        print(f"\nSaving critical building...")
        original_filename = Path(filepath).stem
        critical_filename = update_filename_with_critical(original_filename, len(building_critical))
        save_building(building_critical, filename=critical_filename)
        print(f"✓ Saved as: {critical_filename}")

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
