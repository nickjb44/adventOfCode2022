def score_round(opponent_move, your_move):
    opponent_mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    }
    your_mapping = {
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }
    rock_points = 1
    paper_points = 2
    scissors_points = 3
    loss_points = 0
    draw_points = 3
    win_points = 6

    if opponent_mapping[opponent_move] == "rock":
        if your_mapping[your_move] == "rock":
            return draw_points + rock_points
        elif your_mapping[your_move] == "paper":
            return win_points + paper_points
        elif your_mapping[your_move] == "scissors":
            return loss_points + scissors_points

    if opponent_mapping[opponent_move] == "paper":
        if your_mapping[your_move] == "rock":
            return loss_points + rock_points
        elif your_mapping[your_move] == "paper":
            return draw_points + paper_points
        elif your_mapping[your_move] == "scissors":
            return win_points + scissors_points

    if opponent_mapping[opponent_move] == "scissors":
        if your_mapping[your_move] == "rock":
            return win_points + rock_points
        elif your_mapping[your_move] == "paper":
            return loss_points + paper_points
        elif your_mapping[your_move] == "scissors":
            return draw_points + scissors_points


playbook_file = "data/input.txt"
score = 0
with open(playbook_file) as playbook:
    for game_round in playbook:
        opponent, you = game_round.rstrip().split()
        score += score_round(opponent, you)
print(f"your final score is {score}")
