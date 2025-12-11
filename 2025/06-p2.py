"""
--- Part Two ---

The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Reading the problems right-to-left one column at a time, the problems are now quite different:

    The rightmost problem is 4 + 431 + 623 = 1058
    The second problem from the right is 175 * 581 * 32 = 3253600
    The third problem from the right is 8 + 248 + 369 = 625
    Finally, the leftmost problem is 356 * 24 * 1 = 8544

Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
"""

import numpy as np

def is_separator(vector):
    return all(ch == ' ' for ch in vector)

def find_operands(col_idx, lines):
    col = [line[col_idx] for line in lines]
    num_str = ''.join(ch for ch in col if ch != ' ')
    return int(num_str) if num_str else None

with open('2025/06.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

operations = [x for x in lines[-1].split()]
lines = lines[:-1]

max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) for line in lines]

n_cols = len(lines[0])
col_idx = n_cols - 1

results = []

while col_idx >= 0:
    if is_separator([line[col_idx] for line in lines]):
        col_idx -= 1
        continue
    
    current_numbers = []

    while col_idx >= 0 and not is_separator([line[col_idx] for line in lines]):
        val = find_operands(col_idx, lines)
        if val is not None:
            current_numbers.append(val)
        col_idx -= 1

    operation = operations.pop()
    if operation == '+':
        res = sum(current_numbers)
    elif operation == '*':
        res = np.prod(current_numbers)
    else:
        raise ValueError(f"Unknown operation {operation}")
    
    results.append(res)

grand_total = sum(results)
print(grand_total)
