## Tasks

### Modifying `naive_builder`

1. **Stack → side-by-side placement**
   Modify `naive_builder` so that instead of stacking bricks vertically (along the
   z-axis), it places them side by side along the x- or y-axis.

2. **"I forbandt" wall building**
   Modify `naive_builder` to build a wall using a running-bond pattern, where each row
   is offset from the row below it. Use nested loops (outer loop over rows, inner loop
   over bricks within a row). Think about how to break out of both loops once
   `number_of_bricks` has been reached.

3. **Generalize `naive_builder` to more dimensions**
   Modify `naive_builder` so it works for any `dimension`, not just 3D. Look at how
   `CANONICAL_BRICK` is constructed in `config.py` for inspiration on how to build a
   `Brick` tuple generically, regardless of dimension.

### Modifying `random_builder`

4. **Guarantee requested brick count**
   Modify `random_builder` so it reaches exactly the `number_of_bricks` input, even when
   the grid is nearly full. One approach could be to start with a small local grid size
   and successively grow it if placement attempts keep failing, rather than using a
   single fixed `grid_size` throughout.

5. **Speed up overlap checking with a hash map**
   `random_builder` currently checks each new candidate brick against every existing
   brick individually — an O(n) operation per candidate (look up Big-O notation if
   you're unfamiliar). Improve this by maintaining a set or hash map of occupied cells
   instead, so overlap checks become O(1). Hint: look at
   `place_random_non_touching_bricks.py` for inspiration.

### Connectivity and post-processing

6. **Pass the connectivity test using `extract_critical`**
   Run `extract_critical` on the output of one of your builders, and verify that the
   resulting building passes the tests in `connected.py`.

7. **Remove lonely bricks**
   Write a function that removes all "lonely" bricks - bricks with no touching
   neighbours, i.e., isolated nodes in the building's graph.

   a. Could there still be multiple disconnected *clusters* of more than one brick
      each, which this approach would miss? Would `connected.py` still pass?

   b. Consider approaches to remove entire disconnected components instead of just
      single bricks. 

   c. If you keep only the largest component, could this reduce the building's
      chromatic number? Look at what `extract_critical` does, describe an algorithm that do es not risk reducing the chromatic number, only doing one colouring.

   **Task:** Decide on your own approach, balancing cost against the risk of losing
   structure. Implement it, and justify your choice.

### Improving the greedy builder

8. **Speed up the greedy builder with hash maps**
   Apply the same idea as in the `random_builder` overlap-checking task above: replace
   direct overlap/touching comparisons with hash map or set-based lookups, and measure
   the speedup.

9. **Prioritize high connectivity**
   Modify the greedy builder so that, when choosing the next brick to place, it
   prioritizes candidates that will maximize the building's connectivity (e.g. number of
   touching neighbours), rather than picking arbitrarily among valid candidates.

### Working with the wider pipeline

10. **Wire your builder into the test suite and execution scripts**
    Try running your builder through the existing tests and execution scripts. If your
    builder uses a different parameter signature than the ones supported by
    `active_builder_config.py`, you will need to adapt the tests/scripts accordingly
    rather than relying on the config as-is (see the note on its
    limitations in the README).

11. **Add reproducible randomness via a seed**
    Add a `seed` parameter to a builder that uses randomness, and verify that running it
    twice with the same seed produces an identical building. Take a moment to think
    about why this works — computers are ultimately deterministic, even AI models like
    GPT.

### Coloring algorithms

12. **Implement a greedy coloring algorithm**
   Implement a function that takes a building (or its contact graph) and returns a
   valid coloring using the greedy strategy: process the bricks/nodes in some order,
   and assign each one the lowest-numbered color not already used by an
   already-colored neighbour. Verify on a few small buildings that the resulting
   coloring is valid (no two touching bricks share a color), and compare the number
   of colors used against the building's known chromatic number, use the provided colouring algorithm.


13. **Implement an exact (minimal) coloring algorithm**
   Implement a function that is *guaranteed* to return a coloring using exactly
   $\chi(G)$ colors. Test its efficiency on small buildings. 

### Open-ended

14. **Design your own builder**
    Come up with your own builder idea. Extra credit for ideas that go beyond what's
    already been discussed - for example, but not limited to: colour-aware building,
    e.g., try to "break" a coloruing, enforcing symmetry, or combining
    multiple builders together.

15. **Challenge: find a high-chromatic-number `4x2x1`, `chi=2` building**
    Using a builder of your own design, try to find a building made of `4x2x1` bricks
    (with `chi=2`) whose chromatic number is 6. The smallest such *critical* building
    wins. You can also try optimizing performance for an already working approach, e.g., by introducing caching for `touching_bricks` and `overlapping_bricks`.

16. **Bonus: find any `AxBxC`, `chiX` building requiring 7 or more colours**
    I have not found such a building myself, nor do I know if one exists. I lean towards
    thinking it does not - but prove me wrong!
