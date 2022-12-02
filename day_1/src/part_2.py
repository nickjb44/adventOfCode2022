from queue import PriorityQueue

file_path = "data/input.txt"

elf_calorie_heap = PriorityQueue()
with open(file_path) as calorie_journal:
    current_calories = 0
    for calorie_count in calorie_journal:
        calorie_count = calorie_count.rstrip()
        if calorie_count == "":
            elf_calorie_heap.put(-current_calories)
            current_calories = 0
        else:
            current_calories += int(calorie_count)

elf_calorie_heap.put(-current_calories)

top_three_calories_summed = elf_calorie_heap.get() \
                            + elf_calorie_heap.get() \
                            + elf_calorie_heap.get()

print(f"together the top three elves have {-top_three_calories_summed} calories")
