"""
--- Day 3: Lobby ---

You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

987654321111111
811111111111119
234234234234278
818181911112111

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce. In the above example:

    In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    In 818181911112111, the largest joltage you can produce is 92.

The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?
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

    k = 1
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