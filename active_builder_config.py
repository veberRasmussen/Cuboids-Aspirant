from config import MY_DIRECTIONS, BrickDirection, Building, DIMENSION

#import of builders
from builders.empire_strikes_builder.builder import create_building as empire_strikes_builder
#from builders.return_of_the_builder.builder import create_building as return_of_the_builder
# from builders.new_hope_builder.builder import create_building as new_hope_builder
# from builders.examples.naive_builder import naive_builder
# from builders.examples.random_builder import random_builder
# from builders.examples.greedy_builder.greedy_builder import greedy_builder as greedy_builder



# CHANGE THIS LINE TO SELECT WHICH BUILDER TO USE
ACTIVE_BUILDER = empire_strikes_builder
"""
Options: 
    empire_strikes_builder, 
    new_hope_builder, 
    return_of_the_builder,
    naive_builder, 
    random_builder,
    greedy_builder,
"""

def create_building(
        number_of_bricks: int,
        number_random_bricks: int = 1,
        grid_size: int = 10,
        directions: set[BrickDirection] = MY_DIRECTIONS,
        dimension: int = DIMENSION
) -> Building:
    return ACTIVE_BUILDER(number_of_bricks,number_random_bricks, grid_size, directions, dimension)