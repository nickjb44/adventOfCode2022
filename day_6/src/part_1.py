file = "data/input_1.txt"
with open(file) as input:
    for i, line in enumerate(input):
        left = 0
        right = left + 4
        while right <= len(line):
            if len(set(line[left: right])) == 4:
                print(f"line {i}'s first marker is after character {right}")
                break
            else:
                left += 1
                right = left + 4


