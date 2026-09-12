from config import ColourMap

import matplotlib.pyplot as plt


def draw_building(
        colour_map: ColourMap
):
    """Draw a coloured building with automatically scaled axes."""

    building = colour_map.keys()

    # Check that building is 3D
    if colour_map:
        first_brick = next(iter(building))
        brick_length = len(first_brick)

        if brick_length != 6:
            raise ValueError(
                f"draw_building only works for 3D buildings. "
                f"Expected brick length 6, got {brick_length}. "
                f"This corresponds to dimension {brick_length // 2}."
            )

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Calculate bounds with 10% slack
    if colour_map:
        min_coords = [
            min(brick[i] for brick in building)
            for i in range(3)
        ]

        max_coords = [
            max(brick[i] + brick[3 + i] for brick in building)
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

    ax.set_xlim(grid_min, grid_max)
    ax.set_ylim(grid_min, grid_max)
    ax.set_zlim(grid_min, grid_max)

    # Extract coordinates and colours
    x1, y1, z1 = [], [], []
    dx, dy, dz = [], [], []
    colours = []

    for brick, colour in colour_map.items():
        x_root, y_root, z_root = brick[:3]
        dx_dir, dy_dir, dz_dir = brick[3:6]

        x1.append(x_root)
        y1.append(y_root)
        z1.append(z_root)

        dx.append(dx_dir)
        dy.append(dy_dir)
        dz.append(dz_dir)

        colours.append(colour)

    ax.bar3d(
        x1, y1, z1,
        dx, dy, dz,
        color=colours,
        shade=True,
        edgecolor='black',
        linewidth=0.1
    )

    plt.show()