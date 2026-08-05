from pathlib import Path
from datetime import datetime
from common.coloring_engine.satisfiability.colour_building import colour_building
from config import (
    CANONICAL_DIRECTION, CHI, Building, STORAGE_PATH, Colouring
)


def ensure_storage_dir():
    """Create storage directory if it doesn't exist."""
    STORAGE_PATH.mkdir(parents=True, exist_ok=True)


def generate_filename(chromatic_number: int, size_building: int) -> str:
    """
    Generate filename with convention:
    x_y_z_chi{permutations}_colours{chromatic}_{date}_{index}_size{size}

    Works for any dimension by joining canonical direction with 'x'.
    Size is always at the very end, even after index.
    """
    # Join canonical direction values with 'x' (works for any dimension)
    direction_str = "x".join(str(d) for d in CANONICAL_DIRECTION)
    date = datetime.now().strftime("%Y%m%d")

    base_name = (
        f"{direction_str}_chi{CHI}_"
        f"colours{chromatic_number}_{date}"
    )

    # Check if this filename already exists, add index if needed
    counter = 0
    while True:
        if counter == 0:
            filename = f"{base_name}_size{size_building}"
        else:
            filename = f"{base_name}_{counter}_size{size_building}"

        building_path = STORAGE_PATH / f"{filename}.txt"
        if not building_path.exists():
            break
        counter += 1

    return filename


def save_building(
        building: Building,
        filename: str | None = None,
        path:str | None = None
) -> str:
    """
    Save building to text file.

    Args:
        building: The building to save
        filename: Optional custom filename. If None, generates one automatically.

    Returns:
        The filename used (without extension)
    """
    ensure_storage_dir()
    colouring = colour_building(building)

    if filename is None:
        filename = generate_filename(colouring[0], len(building))

    if path is None:
        building_path = STORAGE_PATH / f"{filename}.txt"
    else:
        building_path = path / f"{filename}.txt"

    with open(building_path, 'w') as f:
        f.write(f"{building}")

    print(f"Saved to: {filename}")
    return filename


def save_colouring(
        filename: str,
        colouring: Colouring,
) -> str:
    """
    Save colouring to text file.

    Args:
        filename: Base filename (without extension)
        colouring: The colouring tuple to save

    Returns:
        The filename used
    """
    ensure_storage_dir()

    colouring_path = STORAGE_PATH / f"{filename}_colour.txt"
    with open(colouring_path, 'w') as f:
        f.write(f"{colouring}")

    print(f"Saved to: {filename}_colour")
    return f"{filename}_colour.txt"
