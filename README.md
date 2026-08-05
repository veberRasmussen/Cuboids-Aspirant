**Setup:**
- Required packages: 
  - `pysat`
  - `networkx` 
- Optional packages: 
  - `numpy` (used by legacy format builders and translation), 
  - `pulp` (used for alternative to the standard graph coloring functions)

 
**Config:**

All global configuration lives in `config.py`. Overview of the key configurable options:

- **`CANONICAL_DIRECTION`** — the base brick shape (e.g. `(2, 1, 1)`), given as a tuple
  of side lengths. `DIMENSION` (number of axes) is derived automatically from its length,
  so switching to a 2D or 4D+ setup just means using a shorter/longer tuple here.
- **`CHI`** — the number of axes that are permuted to generate brick orientations
  (used together with `CANONICAL_DIRECTION` in `MY_DIRECTIONS`, see below).
- **`DEFAULT_GRID_SIZE`**, **`DEFAULT_NUM_BRICKS`**, **`DEFAULT_NUM_RANDOM_INIT`** —
  default parameters for building generation (grid size, total number of bricks,
  and number of initial randomly-placed bricks).
- **`STORAGE_PATH`** — folder used to store/load buildings on disk.
- **`COLORS`** — palette used when visualising/colouring buildings.
- **`ALL_DIRECTIONS`** / **`MY_DIRECTIONS`** — derived sets of legal brick orientations:
  - `ALL_DIRECTIONS` contains *every* permutation of `CANONICAL_DIRECTION`.
  - `MY_DIRECTIONS` contains only the permutations of the first `CHI` axes
    (via `limited_permutations`), which is the direction set used by default
    throughout the project.

Additionally, `active_builder_config.py` controls **which builder implementation** is
used when `create_building(...)` is called — set the `ACTIVE_BUILDER` variable there to
switch between available builders (e.g. `empire_strikes_builder`).

**Note on `active_builder_config.py`:** its `create_building(...)` wrapper only forwards
the fixed parameter set `(number_of_bricks, number_random_bricks, grid_size, directions,
dimension)`. It is entirely possible to write a sensible builder that takes additional or
different parameters - but such a builder cannot be plugged in through `ACTIVE_BUILDER`
without modification *(you can still use it if you leave out one or more of the parameters)*. Do not rely on `active_builder_config.py` to support arbitrary
builder signatures; instead, call/wire up such builders directly wherever they are used.

**Local configuration overrides:**

For local experimentation (e.g. testing a different brick shape, grid size, or builder),
either:

1. Edit the relevant constants directly in `config.py` / `active_builder_config.py`, or
2. Override values at the call site — it is the preferred pattern:
   when writing new builders or utility functions, favour accepting these kinds of
   parameters explicitly (with sensible defaults from `config.py`) rather than reading
   global config values directly, so that callers can always override behaviour locally
   without needing to modify shared configuration.

**Visualization:**
The visualization tool `draw_building`only support **3D**
buildings — attempting to visualize a building created with a `dimension` other than 3
will raise an error. The tool `draw_graph` works for other dimensions as well. 

**Legacy Formats:**
Earlier versions of this project represented buildings as NumPy arrays of **corners**,
while the current implementation represents buildings as **sets of tuples** using a
**root + direction** encoding. In *Cuboids/common/legacy/translation.py* there is a
converter from the old format to the new.
\
Nb. the translator only applies to 3D buildings.



**TO DO:**
- Refractor legacy code into this repo (including but not restricted to)
  - Dimers 5 clique program (make clear distinction from colouruing issues, consider using other REPO)
  - Make inherited coloring in this repo
  - Make finite grid coloring in this repo

- make more robust colour map solution, I am thinking a dictionary for the colourmap, to avoid potential ordering issues
- implement Eilers way of building (trying to break coloring, not reliant on amount of naigbours)
- Create Ldraw interpreter




