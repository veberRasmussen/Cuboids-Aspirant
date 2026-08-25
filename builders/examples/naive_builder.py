from config import MY_DIRECTIONS, BrickDirection, Building, DIMENSION, Brick


def naive_builder(
        number_of_bricks: int,
        number_random_bricks: int,
        grid_size: int = 10,
        directions: set[BrickDirection] = MY_DIRECTIONS,
        dimension: int = DIMENSION
) -> Building:
    building: set[Brick] = set()
    my_direction = list(directions)[0]
    for i in range(number_of_bricks):
        root = (0,0,i*my_direction[2])
        brick = root+my_direction
        building.add(brick)
    return building

