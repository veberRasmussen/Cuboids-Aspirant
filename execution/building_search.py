from active_builder_config import create_building
from common.buildings.visualisation.draw_building import draw_building
from common.buildings.storage.save_building import save_building
from common.coloring_engine.satisfiability.colour_building import colour_building
from config import MY_DIRECTIONS

"""Find a building with target chromatic number."""


# ============================================================================
# CONFIGURATION
# ============================================================================
NUMBER_OF_BRICKS = 10000
NUMBER_OF_RANDOM_BRICKS = 30
INITIAL_GRID = 20
CHROMATIC_NUMBER_GOAL = 6
MAX_ATTEMPTS = 1000
# ============================================================================

def find_building_with_chromatic_goal():
    """Search for building with target chromatic number."""

    print("\n" + "=" * 70)
    print("SEARCHING FOR BUILDING WITH TARGET CHROMATIC NUMBER")
    print("=" * 70)
    print(f"Target chromatic number larger than: {CHROMATIC_NUMBER_GOAL}")
    print(f"Bricks: {NUMBER_OF_BRICKS}")
    print(f"Random initial: {NUMBER_OF_RANDOM_BRICKS}")
    print(f"Grid size: {INITIAL_GRID}x{INITIAL_GRID}x{INITIAL_GRID}")
    print(f"Max attempts: {MAX_ATTEMPTS}")
    print("=" * 70 + "\n")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        building_temp = create_building(
            NUMBER_OF_BRICKS,
            NUMBER_OF_RANDOM_BRICKS,
            INITIAL_GRID,
            MY_DIRECTIONS
        )
        colouring_temp = colour_building(building_temp)
        chromatic = colouring_temp[0]

        print(f"Attempt {attempt:4d}/{MAX_ATTEMPTS} | Chromatic: {chromatic}")

        if chromatic >= CHROMATIC_NUMBER_GOAL:
            print("\n" + "=" * 70)
            print(f"SUCCESS! Found building with chromatic number at least {CHROMATIC_NUMBER_GOAL}")
            print("=" * 70 + "\n")

            print("Saving building...")
            save_building(building_temp)

            first_brick = next(iter(building_temp))
            brick_length = len(first_brick)

            if brick_length == 6: # only allowed to use draw building for 3D
                print("Drawing building...")
                draw_building(building_temp, colouring_temp[1])

            return

    print("\n" + "=" * 70)
    print(f"FAILED: Could not find chromatic number greater than or equal to {CHROMATIC_NUMBER_GOAL} in {MAX_ATTEMPTS} attempts")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    find_building_with_chromatic_goal()

