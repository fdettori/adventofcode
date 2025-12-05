"""
--- Part Two ---

The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18

The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
"""

def intersecano(start1, end1, start2, end2):
    # Ritorna True se due intervalli si sovrappongono
    return not (end1 < start2 or end2 < start1)

ranges = []

with open('2025/05.txt', 'r') as f:
    flag = 0
    for line in f:
        if line == '\n':
            flag = 1
        if flag == 0:
            line = line.strip()
            if line:
                bounds = line.split("-")
                ranges.append((int(bounds[0]), int(bounds[1])))

merged = True
while merged:
    merged = False
    new_ranges = []
    skip = set()
    for i in range(len(ranges)):
        if i in skip:
            continue
        r1 = ranges[i]
        merged_this_round = False
        for j in range(i + 1, len(ranges)):
            if j in skip:
                continue
            r2 = ranges[j]
            if intersecano(r1[0], r1[1], r2[0], r2[1]):
                r1 = (min(r1[0], r2[0]), max(r1[1], r2[1]))
                skip.add(j)
                merged = True
                merged_this_round = True
        new_ranges.append(r1)
    ranges = new_ranges

total_fresh_ids = sum(end - start + 1 for start, end in ranges)
print(total_fresh_ids)
