def solve(lines):
    max_calories = 0
    cur_calories = 0
    for line in lines:
        if line == "":  # Blank line indicates end of an Elf's inventory
            max_calories = max(max_calories, cur_calories)
            cur_calories = 0
        else:
            cur_calories += int(line)
    return max_calories

with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    print(solve(lines))
