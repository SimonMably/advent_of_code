"""https://adventofcode.com/2024/day/1"""

from pprint import pprint

# Part 1

left_list = []
right_list = []

with open("day_1_input.txt", "r", encoding="utf-8") as f:
    columns = list(zip(*(map(int, row.split("   ")) for row in f)))

left_list.extend(columns[0])
left_list.sort()
right_list.extend(columns[1])
right_list.sort()

distances = []
for left, right in zip(left_list, right_list):
    if left > right:
        distances.append(left % right)
    else:
        distances.append(right % left)

print(sum(distances))  # 936063

# Part 2

similarity_scores = []
similarity_score = 0

for num in left_list:
    similarity_score = (similarity_score + right_list.count(num)) * num
    similarity_scores.append(similarity_score)
    similarity_score = 0

print(sum(similarity_scores))  # 23150395
