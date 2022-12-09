# first star
with open("input/stream.txt", "r") as f:
    stream = f.read().strip()

def detect_marker(marker_len):
    buffer = []
    elapsed_chars = 0
    for char in stream:
        elapsed_chars += 1

        if len(buffer) == marker_len:
            buffer.pop(0)

        buffer.append(char)

        if len(set(buffer)) == marker_len:  # set discards unique chars
            break

    return elapsed_chars

print(detect_marker(marker_len=4))

# second star
print(detect_marker(marker_len=14))