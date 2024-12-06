"""https://adventofcode.com/2024/day/3"""

import re

# TODO: Answer for part 2 is too high, fix.
# INFO: All matches after the last instance of "don't()" are ignored
# INFO: There are no instances of "do()" that come after the last instance of "don't()"


def multiply(a: int, b: int) -> int:
    return a * b


with open("day_3_input.txt", "r") as f:
    text = f.read()

pattern = r"mul\((\d+),\s*(\d+)\)"

dont_pattern = r"don't\(\)"

# Find all positions of "don't()"
don_positions = [m.start() for m in re.finditer(dont_pattern, text)]

if don_positions:
    last_dont_pos = don_positions[-1]

# Find all matches
matches = re.finditer(pattern, text)

num_pairs = []
for match in matches:
    # Extract the start position of the match
    match_start = match.start()

    # Skip match if preceded by the last instance of "don't()"
    if last_dont_pos != -1 and match_start > last_dont_pos:
        # Check if the match starts after the last "don't()"
        preceding_text = text[last_dont_pos:match_start]

        # Skips match if preceding "don't()"
        if preceding_text.startswith("don't()"):
            continue

    num1 = int(match.group(1))
    num2 = int(match.group(2))
    print(num1, num2)

    num_pairs.append(multiply(num1, num2))

# print(f"Part 1 answer: {sum(num_pairs)}")  # 173517243
print(f"Part 2 answer: {sum(num_pairs)}")
