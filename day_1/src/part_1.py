file_path = "data/input.txt"

calories_per_elf = []
with open(file_path) as calorie_journal:
    current_calories = 0
    for calorie_count in calorie_journal:
        calorie_count = calorie_count.rstrip()
        if calorie_count == "":
            calories_per_elf.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(calorie_count)

calories_per_elf.append(current_calories)

print(f"most calories an elf is carrying is {max(calories_per_elf)}")
