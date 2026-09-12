from pathlib import Path
from ast import literal_eval

from config import Colouring


def load_colouring(
        filepath: str | Path
) -> Colouring:
    """
    Load a colouring from a text file.
    """

    filepath = Path(filepath)

    with open(filepath, "r") as f:
        content = f.read()

    return literal_eval(content)