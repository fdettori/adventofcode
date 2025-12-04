"""
--- Day 4: Printing Department ---

You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, 
and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. 
"We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, 
you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. 
If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
"""

import numpy as np

with open('2025/04.txt') as f:
    lines = [line.strip() for line in f]

matrix_list = [list(line) for line in lines]

matrix = np.array(matrix_list)
matrix[matrix == '.'] = 0
matrix[matrix == '@'] = 1

matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)

filter = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

total_sum = 0

for i in range(1, matrix.shape[0] - 1):
    for j in range(1, matrix.shape[1] - 1):

        if matrix[i, j] == '1':
        
            local = np.array(matrix[i-1:i+2, j-1:j+2], dtype='int64')

            product = np.sum(local * filter)
            if product < 4:
                total_sum +=1

print(total_sum)