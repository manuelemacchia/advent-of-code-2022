# first star
with open("input/forest.txt", "r") as f:
    forest = [list(map(int, list(row.strip()))) for row in list(f)]

visible = []

for y in range(0, len(forest[0])):
    for x in range(0, len(forest)):
        tree = (x, y)
        height = forest[y][x]

        top = [h for h in (forest[yt][x] for yt in range(0, y))]  # trees from {direction} towards tree
        bottom = [h for h in (forest[yt][x] for yt in reversed(range(y+1, len(forest))))]
        left = [h for h in (forest[y][xt] for xt in range(0, x))]
        right = [h for h in (forest[y][xt] for xt in reversed(range(x+1, len(forest[0]))))]

        for direction in [top, bottom, left, right]:
            if not direction or all((height > h for h in direction)):
                visible.append(tree)
                break

print(len(visible))

# second star
from math import prod

scenic_scores = []

def viewing_distance(tree_height, line_heights):
    distance = 0
    for h in line_heights:
        distance += 1
        if h >= tree_height:
            break

    return distance

for y in range(0, len(forest[0])):
    for x in range(0, len(forest)):
        tree = (x, y)
        height = forest[y][x]

        top_heights = (h for h in (forest[yt][x] for yt in reversed(range(0, y))))  # trees from tree towards {direction}
        bottom_heights = (h for h in (forest[yt][x] for yt in range(y+1, len(forest))))
        left_heights = (h for h in (forest[y][xt] for xt in reversed(range(0, x))))
        right_heights = (h for h in (forest[y][xt] for xt in range(x+1, len(forest[0]))))

        viewing_distances = [
            viewing_distance(height, line_heights)
            for line_heights in [top_heights, bottom_heights, left_heights, right_heights]
        ]

        scenic_scores.append(prod(viewing_distances))

print(max(scenic_scores))