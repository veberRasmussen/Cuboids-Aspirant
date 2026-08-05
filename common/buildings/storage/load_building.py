from pathlib import Path
from config import Building


def load_building(filepath: Path | str) -> Building:
    """
    Load building from a text file.

    Args:
        filepath: Path to the building file (can be string or Path object)

    Returns:
        Building (set of bricks)
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"Building file not found: {filepath}")

    building: Building = set()

    with open(filepath, 'r') as f:
        content = f.read().strip()

    building: Building = eval(content)
    return building