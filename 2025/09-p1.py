"""
--- Day 9: Movie Theater ---

You slide down the firepole in the corner of the playground and land in the North Pole base movie theater!

The movie theater has a big tile floor with an interesting pattern. 
Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. 
Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. 
They even have a list of where the red tiles are located in the grid (your puzzle input).

For example:

7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3

Showing red tiles as # and other tiles as ., the above arrangement of red tiles would look like this:

..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............

You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

For example, you could make a rectangle (shown as O) with an area of 24 between 2,5 and 9,7:

..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO.#..
..............

Or, you could make a rectangle with area 35 between 7,1 and 11,7:

..............
.......OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOOO..
..............

You could even make a thin rectangle with an area of only 6 between 7,3 and 2,3:

..............
.......#...#..
..............
..OOOOOO......
..............
..#......#....
..............
.........#.#..
..............

Ultimately, the largest rectangle you can make in this example has area 50. One way to do this is between 2,5 and 11,1:

..............
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..............
.........#.#..
..............

Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?
"""


import itertools # itertools is more efficient for pairs, but your loop works too

with open('2025/09.txt', 'r') as f:
    # Parsing logic looks good
    red_tiles_input = [line.strip() for line in f]

# Convert to list of tuples for easier iteration
coords = []
for line in red_tiles_input:
    values = line.split(',')
    coords.append((int(values[0]), int(values[1])))

# No need for a set for lookup anymore, since we don't check the other corners
# But we can keep it unique just in case there are duplicates in input

max_area = 0

# Iterate over all pairs
# itertools.combinations is cleaner to avoid checking the same pair twice or self-pairs
for p1, p2 in itertools.combinations(coords, 2):
    x1, y1 = p1
    x2, y2 = p2
    
    # 1. REMOVED: check for other corners (puzzle doesn't require them to be red)
    # 2. REMOVED: check for straight lines (puzzle allows 1-tile wide rectangles)
    
    # 3. CHANGED: Add +1 to include the tiles themselves
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    
    area = width * height
    
    if area > max_area:
        max_area = area

print("Largest rectangle area:", max_area)