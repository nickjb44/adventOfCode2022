def is_contained(section_1, section_2):
    section_1_start = int(section_1[0])
    section_1_end = int(section_1[1])

    section_2_start = int(section_2[0])
    section_2_end = int(section_2[1])

    # section 1 contains section 2
    if section_1_start <= section_2_start and section_1_end >= section_2_end:
        print("-----------------------------")
        print(f"section 1 is {section_1} and section 2 is {section_2}")
        print(f"section 1 contains section 2 because:")
        print(f"    {section_1_start} <= {section_2_start}")
        print(f"    {section_1_end} >= {section_2_end}")
        print("-----------------------------")
        return True

    # section 2 contains section 1
    elif section_2_start <= section_1_start and section_2_end >= section_1_end:
        print("-----------------------------")
        print(f"section 2 is {section_2} and section 1 is {section_1}")
        print(f"section 2 contains section 1 because:")
        print(f"    {section_2_start} <= {section_1_start}")
        print(f"    {section_2_end} >= {section_1_end}")
        print("-----------------------------")
        return True

    else:
        return False


section_file = "data/input.txt"
number_contained = 0
with open(section_file) as sections:
    for section in sections:
        section = section.rstrip()
        section_1_range, section_2_range = section.split(",")
        if is_contained(
                section_1_range.split('-'),
                section_2_range.split('-')
        ):
            number_contained += 1
print(f"{number_contained} assignments are fully contained by the other elf's work")
