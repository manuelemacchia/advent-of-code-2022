# first star
def load():
    with open("input/plan.txt", "r") as f:
        config = []
        moves = []
        for line in list(f):
            if line.strip().startswith("["):  # part of initial config
                c = [line[i] for i in range(1, len(line), 4)]
                config.append(c)
            elif line.startswith("move"):  # part of moves
                tokens = line.strip().split(" ")
                move = int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1  # how many, from stack no., to stack no.
                moves.append(move)

    stacks = {
        stack: [config[level][stack] for level in reversed(range(len(config))) if config[level][stack] != " "]
        for stack in range(len(config[0]))
    }

    return moves, stacks

moves, stacks = load()

for move in moves:
    for i in range(move[0]):
        crate = stacks[move[1]].pop()
        stacks[move[2]].append(crate)

tops = "".join([stacks[i].pop() for i in range(len(stacks))])
print(tops)

# second star
moves, stacks = load()

for move in moves:
    crates = stacks[move[1]][-move[0]:]
    del stacks[move[1]][-move[0]:]
    stacks[move[2]].extend(crates)

tops = "".join([stacks[i][-1] for i in range(len(stacks))])
print(tops)