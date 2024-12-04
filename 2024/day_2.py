"""https://adventofcode.com/2024/day/2"""

with open("day_2_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    split_lines = [str_nums.split() for str_nums in lines]

    reports = [[int(int_nums) for int_nums in str_nums] for str_nums in split_lines]


def is_safe(report):
    n = len(report)
    return (all(1 <= report[i + 1] - report[i] <= 3 for i in range(n - 1))) or (
        all(1 <= report[i] - report[i + 1] <= 3 for i in range(n - 1))
    )


# part 1
safe_count = sum(map(is_safe, reports))
print(f"Safe reports: {safe_count}")  # 463

# part 2
dampened_safe_count = 0
for report in reports:
    dampened_safe_count += is_safe(report) or any(
        is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))
    )
print(f"Dampened safe reports: {dampened_safe_count}")  # 514
