def is_overlapped(section_1, section_2):
    section_1_start = int(section_1[0])
    section_1_end = int(section_1[1])

    section_2_start = int(section_2[0])
    section_2_end = int(section_2[1])

    if not (section_1_end < section_2_start or section_2_end < section_1_start):
        return True

    else:
        return False


section_file = "data/input.txt"
number_contained = 0
with open(section_file) as sections:
    for section in sections:
        section = section.rstrip()
        section_1_range, section_2_range = section.split(",")
        if is_overlapped(
                section_1_range.split('-'),
                section_2_range.split('-')
        ):
            number_contained += 1
print(f"{number_contained} assignments are fully contained by the other elf's work")
