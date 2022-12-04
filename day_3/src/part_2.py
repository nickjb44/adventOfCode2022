def letter_to_priority(letter):
    if letter.isupper():
        return ord(letter) - ord("A") + 27
    elif letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        raise Exception(f"cannot recognize letter {letter}")


def find_badge(triplet):
    return triplet[0].intersection(triplet[1]).intersection(triplet[2])

rucksacks_file = "data/input.txt"
sum_of_priorities = 0

with open(rucksacks_file) as rucksacks:
    triplet = []
    for rucksack in rucksacks:
        triplet.append(set(rucksack.rstrip()))
        if len(triplet) == 3:
            badge = find_badge(triplet)
            triplet = []
            for letter in badge:
                sum_of_priorities += letter_to_priority(letter)

print(f"sum of priorities is {sum_of_priorities}")
