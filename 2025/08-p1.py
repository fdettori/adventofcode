"""
--- Day 8: Playground ---

Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. 
Through careful rigging, they have suspended a large number of small electrical junction boxes.

Their plan is to connect the junction boxes with long strings of lights. 
Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, 
electricity can pass between those two junction boxes.

The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. 
They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

For example:

162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689

This list describes the position of 20 junction boxes, one per line. 
Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.

To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible 
according to straight-line distance. In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.

By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. 
After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.

Now, the two junction boxes which are closest together but aren't already directly connected are 162,817,812 and 431,825,988. 
After connecting them, since 162,817,812 is already connected to another junction box, 
there is now a single circuit which contains three junction boxes and an additional 17 circuits which contain one junction box each.

The next two junction boxes to connect are 906,360,560 and 805,96,715. 
After connecting them, there is a circuit containing 3 junction boxes, 
a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.

The next two junction boxes are 431,825,988 and 425,690,689. 
Because these two junction boxes were already in the same circuit, nothing happens!

This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. 
They would like to know how big the circuits will be.

After making the ten shortest connections, there are 11 circuits: one circuit which contains 5 junction boxes, 
one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, 
and seven circuits which each contain a single junction box. 
Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.


Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together. 
Afterward, what do you get if you multiply together the sizes of the three largest circuits?
"""

import math
from itertools import combinations

# Union-Find / Disjoint Set
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        # merge smaller set into larger
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]
        return True

# Read input
with open("2025/08.txt") as f:
    boxes = [tuple(map(int, line.strip().split(','))) for line in f]

n = len(boxes)

# Compute all pairwise distances
pairs = []
for i, j in combinations(range(n), 2):
    x1, y1, z1 = boxes[i]
    x2, y2, z2 = boxes[j]
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    pairs.append((dist, i, j))

# Sort pairs by distance
pairs.sort()

# Union-Find initialization
uf = UnionFind(n)

# Connect the 1000 closest pairs
for k in range(min(1000, len(pairs))):
    _, i, j = pairs[k]
    uf.union(i, j)

# Count sizes of each circuit
circuit_sizes = {}
for i in range(n):
    root = uf.find(i)
    circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

# Take three largest
largest_sizes = sorted(circuit_sizes.values(), reverse=True)[:3]

# Result
result = largest_sizes[0] * largest_sizes[1] * largest_sizes[2]
print("Product of three largest circuits:", result)
