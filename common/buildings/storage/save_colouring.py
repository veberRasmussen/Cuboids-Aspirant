from common.buildings.storage.storage import ensure_storage_dir
from config import (
    STORAGE_PATH, Colouring
)


def save_colouring(
        filename: str,
        colouring: Colouring,
        path: str | Path | None = None
) -> str:
    """
    Save colouring to a text file.

    Args:
        filename: Base filename (without extension).
        colouring: The colouring tuple to save.
        path: Optional directory to save to. If None, uses STORAGE_PATH.

    Returns:
        The filename used, including extension.
    """
    ensure_storage_dir()

    if path is None:
        colouring_path = STORAGE_PATH / f"{filename}_colour.txt"
    else:
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        colouring_path = path / f"{filename}_colour.txt"

    with open(colouring_path, 'w') as f:
        f.write(f"{colouring}")

    print(f"Saved to: {colouring_path}")
    return f"{filename}_colour.txt"