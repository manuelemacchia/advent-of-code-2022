# first star
with open("input/items.txt", "r") as f:
    items = [line.strip() for line in list(f)]

shared_items = []
for rucksack in items:
    mid = int(len(rucksack)/2)
    compartments = rucksack[:mid], rucksack[mid:]
    shared_item, = set(compartments[0]).intersection(set(compartments[1]))
    shared_items.append(shared_item)

import string
item_types = list(string.ascii_lowercase + string.ascii_uppercase)
priority_map = {c: p for c, p in zip(item_types, range(1, len(item_types)+1))}

priorities = [priority_map[item] for item in shared_items]
print(sum(priorities))

# second star
badges = []
for i in range(0, len(items), 3):
    rucksacks = items[i:i+3]
    badge, = set.intersection(*(set(r) for r in rucksacks))
    badges.append(badge)

priorities = [priority_map[badge] for badge in badges]
print(sum(priorities))