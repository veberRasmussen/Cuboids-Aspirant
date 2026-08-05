from config import Building

def move_building_to_origin(building: Building) -> Building:
    """
    Translate a building so that its minimum coordinate along every axis is 0.

    Only the root (position) part of each brick is shifted; the direction
    (size) part is left unchanged.
    """
    if not building:
        return set()

    dimension = len(next(iter(building))) // 2

    mins = [
        min(brick[axis] for brick in building)
        for axis in range(dimension)
    ]

    return {
        tuple(brick[axis] - mins[axis] for axis in range(dimension)) + brick[dimension:]
        for brick in building
    }