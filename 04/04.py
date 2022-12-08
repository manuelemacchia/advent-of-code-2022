# first star
with open("input/pairs.txt") as f:
    pairs = [line.strip().split(",") for line in list(f)]

ranges = [(a.split("-"), b.split("-")) for a, b in pairs]
sections = [(set(range(int(a[0]), int(a[1])+1)), set(range(int(b[0]), int(b[1])+1))) for a, b in ranges]

fully_contains_other_count = 0
for section in sections:
    all_sections = section[0].union(section[1])
    if len(all_sections) == len(section[0]) or len(all_sections) == len(section[1]):
        fully_contains_other_count += 1

print(fully_contains_other_count)

# second star
any_overlap_count = 0
for section in sections:
    overlap = section[0].intersection(section[1])
    if overlap:
        any_overlap_count += 1

print(any_overlap_count)