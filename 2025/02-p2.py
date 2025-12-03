"""
--- Part Two ---

The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

    11-22 still has two invalid IDs, 11 and 22.
    95-115 now has two invalid IDs, 99 and 111.
    998-1012 now has two invalid IDs, 999 and 1010.
    1188511880-1188511890 still has one invalid ID, 1188511885.
    222220-222224 still has one invalid ID, 222222.
    1698522-1698528 still contains no invalid IDs.
    446443-446449 still has one invalid ID, 446446.
    38593856-38593862 still has one invalid ID, 38593859.
    565653-565659 now has one invalid ID, 565656.
    824824821-824824827 now has one invalid ID, 824824824.
    2121212118-2121212124 now has one invalid ID, 2121212121.

Adding up all the invalid IDs in this example produces 4174379265.

What do you get if you add up all of the invalid IDs using these new rules?
"""

def is_repeated(i, n):

    i_str = str(i)
    n_str = str(n)

    length_n = len(n_str)
    length_i = len(i_str)
    # print(f'i: {i}, n: {n}, len_i: {length_i}, len_n: {length_n}')

    k = 0

    for k in range(0, length_n, length_i):
        # print(f'k: {k}')
        # print(f'{i_str} compared to {n_str[k:k+length_i]}')

        if int(i_str) != int(n_str[k:k+length_i]):
            # print("Sono diversi")
            return False
        
        k += length_i

    return True

def is_invalid(n):
    
    n_str = str(n)
    length_n = len(n_str)

    for i in range(1, length_n // 2 + 1):
        string_to_check = n_str[:i]
        # print(f'checking {string_to_check} in {n}')
        if is_repeated(string_to_check, n):
            # print("invalid ID")
            return True
        
    return False
        

with open('2025/02.txt', 'r') as f:
    file_string = f.read()

ranges = file_string.split(",")
invalid_ids_sum = 0

z = 0
print(f'Ci sono {len(ranges)} ranges')

for single_range in ranges:

    print(f'range {z}')
    bounds = single_range.split("-")
    start = int(bounds[0])
    end = int(bounds[1])

    for i in range(start, end + 1):

        if is_invalid(i):
            invalid_ids_sum += i

    z += 1


print(invalid_ids_sum)