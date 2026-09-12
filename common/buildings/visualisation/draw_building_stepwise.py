import matplotlib.pyplot as plt

from config import ColourMap


def draw_building_stepwise(
        colour_map: ColourMap
):
    """
    Draw a coloured building one brick at a time, ordered by z, then x, then y.
    Press SPACE to advance to the next brick.
    Bricks accumulate rather than being replaced.
    The axes automatically scale to fit the building with 10% slack.
    """

    building = colour_map.keys()

    # Check that building is 3D
    if colour_map:
        first_brick = next(iter(building))
        brick_length = len(first_brick)

        if brick_length != 6:
            raise ValueError(
                f"draw_building_stepwise only works for 3D buildings. "
                f"Expected brick length 6, got {brick_length}. "
                f"This corresponds to dimension {brick_length // 2}."
            )

    # Sort by z, then x, then y (root coordinates)
    building_list = sorted(
        building,
        key=lambda brick: (brick[2], brick[0], brick[1])
    )

    # Calculate grid bounds with 10% slack
    if building_list:
        min_coords = [
            min(brick[i] for brick in building_list)
            for i in range(3)
        ]

        max_coords = [
            max(brick[i] + brick[3 + i] for brick in building_list)
            for i in range(3)
        ]

        max_extent = max(
            max_coords[i] - min_coords[i]
            for i in range(3)
        )

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
    for brick in building_list:
        x_root, y_root, z_root = brick[:3]
        dx_dir, dy_dir, dz_dir = brick[3:6]

        ax.bar3d(
            x_root,
            y_root,
            z_root,
            dx_dir,
            dy_dir,
            dz_dir,
            color=colour_map[brick],
            alpha=0.05,
            shade=False
        )

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

            if current_step <= len(building_list):
                brick = building_list[current_step - 1]

                x_root, y_root, z_root = brick[:3]
                dx_dir, dy_dir, dz_dir = brick[3:6]

                ax.bar3d(
                    x_root,
                    y_root,
                    z_root,
                    dx_dir,
                    dy_dir,
                    dz_dir,
                    color=colour_map[brick],
                    alpha=1.0,
                    shade=True,
                    edgecolor='black',
                    linewidth=0.5
                )

                ax.set_title(
                    f"Brick {current_step}/{len(building_list)} "
                    f"- Press SPACE to continue"
                )

        plt.draw()
        plt.pause(0.01)

    plt.show()
    plt.close(fig)