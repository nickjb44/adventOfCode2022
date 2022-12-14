def diagram_to_stacks(diagram, n_stacks, first_letter_index=1, letter_index_interval=4):
    """
    takes a list of strings formatted with letters enclosed in square brackets at regular intervals
    e.g.
    [Z] [M] [P]
     1   2   3
    transforms this into a list of stacks and returns that list
    :param diagram:
    :param first_letter_index:
    :param letter_index_interval:
    :param n_stacks:
    :return:
    """
    stack_list = [[] for _ in range(n_stacks)]
    for crate_level in reversed(diagram):
        for stack_index in range(n_stacks):
            letter_index = first_letter_index + (letter_index_interval * stack_index)
            if len(crate_level) >= letter_index:
                crate_letter = crate_level[letter_index]
                if crate_letter.isupper():
                    stack_list[stack_index].append(crate_letter)

    return stack_list


def shift_stack_top(stacks, n_moves, popped_stack_index, pushed_stack_index):
    """
    takes in our stack list, the index to take from, the index to push to, and the number of moves to make.
    Mutates the list of stacks in place
    :param stacks:
    :param n_moves:
    :param popped_stack_index:
    :param pushed_stack_index:
    :return:
    """
    for _ in range(n_moves):
        stacks[pushed_stack_index].append(stacks[popped_stack_index].pop())
    return


def parse_move_line(line):
    """
    parses a line of the form:
        move 1 from 2 to 1
    into a dictionary formed with:
    {
        "n_moves": int,
        "popped_stack_index": int,
        "pushed_stack_index": int
    }
    :param line:
    :return:
    """
    digits_in_string = [int(word) for word in line.split() if word.isdigit()]
    return {
        "n_moves": digits_in_string[0],
        "popped_stack_index": digits_in_string[1]-1,
        "pushed_stack_index": digits_in_string[2]-1
    }


with open("data/input_1.txt") as input_file:
    diagram = []
    instructions = []
    should_read_diagram = True
    should_read_instructions = False

    for line in input_file:
        if should_read_diagram:
            if "1" not in line:
                diagram.append(line.rstrip())
            else:
                should_read_diagram = False
                stacks = diagram_to_stacks(diagram, 9)
        elif line.rstrip() == "":
            should_read_instructions = True
        elif "move" in line.rstrip():
            move_params = parse_move_line(line)
            shift_stack_top(
                stacks,
                move_params["n_moves"],
                move_params["popped_stack_index"],
                move_params["pushed_stack_index"]
            )

answer = ""
for stack in stacks:
    answer += stack.pop()
print(f"The top container in each stack is as follows: {answer}")
