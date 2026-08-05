import time
from builders.empire_strikes_builder.builder import create_building as empire_strikes_builder
from builders.return_of_the_builder.builder import create_building as return_of_the_builder
#from builders.new_hope_builder.builder import create_building as new_hope_builder
from config import MY_DIRECTIONS


# ============================================================================
# CONFIGURATION
# ============================================================================
NUMBER_OF_RANDOM_BRICKS = 5
INITIAL_GRID = 10
TEST_RUNS = [5, 10, 50, 100, 200, 300, 400, 500]
RUNS_PER_TEST = 10

builders = {
#    "New Hope Builder": new_hope_builder,
    "Empire Strikes Builder": empire_strikes_builder,
    "Return of the Builder": return_of_the_builder
}
# ============================================================================


def benchmark_builder(
        builder_func,
        number_of_bricks: int,
        number_of_runs: int = RUNS_PER_TEST) -> float:
    """
    Benchmark a builder by running it multiple times.
    Returns average time in seconds.
    """
    times = []

    for _ in range(number_of_runs):
        start = time.time()
        building = builder_func(
            number_of_bricks,
            NUMBER_OF_RANDOM_BRICKS,
            INITIAL_GRID,
            MY_DIRECTIONS
        )
        end = time.time()
        times.append(end - start)

    return sum(times) / len(times)


def main():
    """Run benchmark comparison."""

    print("=" * 70)
    print("BUILDER PERFORMANCE BENCHMARK")
    print("=" * 70)
    print(f"Random bricks: {NUMBER_OF_RANDOM_BRICKS}")
    print(f"Grid size: {INITIAL_GRID}x{INITIAL_GRID}x{INITIAL_GRID}")
    print(f"Runs per test: {RUNS_PER_TEST}")
    print("=" * 70)
    print()

    # Test each number of bricks
    for num_bricks in TEST_RUNS:
        print(f"Building with {num_bricks} bricks:")
        print("-" * 70)

        for builder_name, builder_func in builders.items():
            try:
                avg_time = benchmark_builder(builder_func, num_bricks)
                print(f"  {builder_name:30s}: {avg_time:.4f}s")
            except Exception as e:
                print(f"  {builder_name:30s}: ERROR - {e}")

        print()

    print("=" * 70)
    print("Benchmark complete!")


if __name__ == "__main__":
    main()