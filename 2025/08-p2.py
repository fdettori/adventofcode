"""
--- Part Two ---

The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?
"""

import math
from itertools import combinations

# Union-Find / Disjoint Set
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n  # Track number of circuits

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
        self.num_components -= 1
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

last_pair = None

# Connect until only one circuit remains
for _, i, j in pairs:
    if uf.union(i, j):
        last_pair = (i, j)
        if uf.num_components == 1:
            break

# Multiply X coordinates of the last pair
x1, _, _ = boxes[last_pair[0]]
x2, _, _ = boxes[last_pair[1]]
result = x1 * x2

print("Product of X coordinates of last connection:", result)
