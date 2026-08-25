import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from common.buildings.move_to_origin import move_building_to_origin
from config import Building, ColourMap


def draw_building_stepwise(
        building: Building,
        color_map: ColourMap,
        grid: int = 10):
    """
    Draw building one brick at a time, ordered by z, then x, then y.
    Press SPACE to advance to next brick.
    Bricks accumulate (not replaced).
    Grid auto-scales to fit building with 10% slack.
    """
    # Check that building is 3D
    if building:
        first_brick = next(iter(building))
        brick_length = len(first_brick)

        if brick_length != 6:
            raise ValueError(
                f"draw_building only works for 3D buildings. "
                f"Expected brick length 6, got {brick_length}. "
                f"This corresponds to dimension {brick_length // 2}."
            )

    # Sort by z, then x, then y (root coordinates)
    building_list = sorted(building, key=lambda brick: (brick[2], brick[0], brick[1]))

    # Create mapping from original building order to sorted order
    building_original = list(building)
    color_map_sorted = [
        color_map[building_original.index(brick)]
        for brick in building_list
    ]

    # Calculate grid bounds with 10% slack
    if building_list:
        min_coords = [min(brick[i] for brick in building_list) for i in range(3)]
        max_coords = [max(brick[i] + brick[3 + i] for brick in building_list) for i in range(3)]

        # Find the maximum extent
        max_extent = max(max_coords[i] - min_coords[i] for i in range(3))

        # Add 10% slack
        slack = max_extent * 0.1

        grid_min = min(min_coords) - slack
        grid_max = max(max_coords) + slack
    else:
        grid_min = 0
        grid_max = 10

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(grid_min, grid_max)
    ax.set_ylim(grid_min, grid_max)
    ax.set_zlim(grid_min, grid_max)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Draw all bricks transparently first
    for i, brick in enumerate(building_list):
        x_root, y_root, z_root = brick[:3]
        dx_dir, dy_dir, dz_dir = brick[3:6]
        ax.bar3d(x_root, y_root, z_root, dx_dir, dy_dir, dz_dir,
                 color=color_map_sorted[i], alpha=0.05, shade=False)

    # Step through each brick
    step = [0]

    def on_key(event):
        if event.key == ' ':
            step[0] += 1

    fig.canvas.mpl_connect('key_press_event', on_key)

    current_step = 0
    while current_step < len(building_list):
        if step[0] > current_step:
            current_step = step[0]

            # Highlight the newly added brick (solid)
            if current_step <= len(building_list):
                brick = building_list[current_step - 1]
                x_root, y_root, z_root = brick[:3]
                dx_dir, dy_dir, dz_dir = brick[3:6]
                ax.bar3d(x_root, y_root, z_root, dx_dir, dy_dir, dz_dir,
                         color=color_map_sorted[current_step - 1], alpha=1.0, shade=True, edgecolor='black',linewidth=0.5)

                ax.set_title(f"Brick {current_step}/{len(building_list)} - Press SPACE to continue")

        plt.draw()
        plt.pause(0.01)

    plt.show()
    plt.close(fig)



