"""
--- Part Two ---

The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

Consider again the example from before:

987654321111111
811111111111119
234234234234278
818181911112111

Now, the joltages are much larger:

    In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

What is the new total output joltage?
"""

def find_highest(vector):
    max = 0

    for index, number in enumerate(vector):
        if int(number) > max:
            index_max = index
            max = int(number)
        
        if int(number) == 9:
            return 9,index
    
    return max, index_max


def find_joltage(bank):

    k = 11
    z = 0
    joltage = 0

    while k >= 0:
        # for i, number in enumerate(bank[z:]):

        print(f"k = {k}")
    
        # find highest in bank[z:]
        max, index = find_highest(bank[z:len(bank)-k])
        print(f"bank: {bank}, max: {max}, index: {index}")


        # new bank is bank[index+1:]
        bank = bank[index+1:]
            
        joltage += max * 10**k
        k -= 1

    return joltage

text_path = '2025/03.txt'

with open(text_path, 'r') as f:
    banks = [line.strip() for line in f]

print(f"There are {len(banks)} banks")
print(f"Example: {banks[0]}")

total_j = 0

for bank in banks:
    total_j += find_joltage(bank)

print(total_j)