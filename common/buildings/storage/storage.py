from config import (
    STORAGE_PATH
)
def ensure_storage_dir():
    """Create storage directory if it doesn't exist."""
    STORAGE_PATH.mkdir(parents=True, exist_ok=True)