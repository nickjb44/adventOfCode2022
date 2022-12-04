def letter_to_priority(letter):
    if letter.isupper():
        return ord(letter) - ord("A") + 27
    elif letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        raise Exception(f"cannot recognize letter {letter}")


def rucksack_to_intersection(rucksack):
    midpoint = len(rucksack) // 2
    left_side = set(rucksack[:midpoint])
    right_side = set(rucksack[midpoint:])
    return left_side.intersection(right_side)


rucksacks_file = "data/input.txt"
sum_of_priorities = 0

with open(rucksacks_file) as rucksacks:
    for rucksack in rucksacks:
        common_contents = rucksack_to_intersection(rucksack)
        for letter in common_contents:
            sum_of_priorities += letter_to_priority(letter)

print(f"sum of priorities is {sum_of_priorities}")
