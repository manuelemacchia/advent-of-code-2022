# first star
rps = {  # list of ways to win if key is opponent and value is response
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}

with open("input/strategy.txt", "r") as f:
    strategy = [(r[0], r[1]) for r in (line.strip().split(" ") for line in list(f))]

code = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

strategy_decoded = [(code[r[0]], code[r[1]]) for r in strategy]

score_map = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

def play(opponent, response):
    if opponent == response:
        return 3  # draw
    elif (opponent, response) in rps.items():
        return 6  # win
    else:
        return 0  # loss

shape_score = [score_map[r[1]] for r in strategy_decoded]
outcome_score = [play(r[0], r[1]) for r in strategy_decoded]

print(sum(shape_score) + sum(outcome_score))

# second star
code = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}

def choice(opponent, result):
    if result == "draw":
        return opponent
    elif result == "win":
        return rps[opponent]
    elif result == "loss":
        inv_rps = {v: k for k, v in rps.items()}
        return inv_rps[opponent]

strategy_decoded = [(code[r[0]], choice(code[r[0]], code[r[1]])) for r in strategy]

shape_score = [score_map[r[1]] for r in strategy_decoded]
outcome_score = [play(r[0], r[1]) for r in strategy_decoded]

print(sum(shape_score) + sum(outcome_score))

# the elf is trying to trick you!