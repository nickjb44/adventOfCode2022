def choose_move(opponent_move, outcome):
    if opponent_move == "rock":
        if outcome == "lose":
            return "scissors"
        elif outcome == "draw":
            return "rock"
        elif outcome == "win":
            return "paper"
        else:
            raise Exception(f"cannot recognize outcome {outcome}")

    elif opponent_move == "paper":
        if outcome == "lose":
            return "rock"
        elif outcome == "draw":
            return "paper"
        elif outcome == "win":
            return "scissors"
        else:
            raise Exception(f"cannot recognize outcome {outcome}")

    elif opponent_move == "scissors":
        if outcome == "lose":
            return "paper"
        elif outcome == "draw":
            return "scissors"
        elif outcome == "win":
            return "rock"
        else:
            raise Exception(f"cannot recognize outcome {outcome}")

    else:
        raise Exception(f"cannot recognize move {opponent_move}")


def score_round(opponent_move, outcome):
    opponent_mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    }
    outcome_mapping = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }
    move_points = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }
    loss_points = 0
    draw_points = 3
    win_points = 6

    mapped_move = opponent_mapping[opponent_move]
    mapped_outcome = outcome_mapping[outcome]
    if mapped_move == "rock":
        if mapped_outcome == "lose":
            return loss_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]
        elif mapped_outcome == "draw":
            return draw_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]
        elif mapped_outcome == "win":
            return win_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]

    if mapped_move == "paper":
        if mapped_outcome == "lose":
            return loss_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]
        elif mapped_outcome == "draw":
            return draw_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]
        elif mapped_outcome == "win":
            return win_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]

    if mapped_move == "scissors":
        if mapped_outcome == "lose":
            return loss_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]
        elif mapped_outcome == "draw":
            return draw_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]
        elif mapped_outcome == "win":
            return win_points + move_points[
                choose_move(mapped_move, mapped_outcome)
            ]


playbook_file = "data/input.txt"
score = 0
with open(playbook_file) as playbook:
    for game_round in playbook:
        opponent, outcome = game_round.rstrip().split()
        score += score_round(opponent, outcome)
print(f"your final score is {score}")
