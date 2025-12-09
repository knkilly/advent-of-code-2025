from pathlib import Path

def read_lines_to_list(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')  # Remove trailing newline character
            lines.append(line)
    return lines

def calculate_day_1_answers():
    data_path = Path(__file__,"..", "..", "data", "day1.txt").resolve()
    rotations = read_lines_to_list(file_path=data_path)

    def calculate_password_part1(rotations):
        dial = 50
        count_zero = 0
        for rotation in rotations:
            direction, distance = rotation[0], int(rotation[1:])
            dial = (dial + distance if direction == 'R' else dial - distance) % 100
            count_zero += (dial == 0)
        return count_zero

    def calculate_password_part2(rotations):
        dial = 50
        count_zero = 0
        for rotation in rotations:
            direction, distance = rotation[0], int(rotation[1:])
            for _ in range(distance):
                dial = (dial + 1 if direction == 'R' else dial - 1) % 100
                count_zero += (dial == 0)
        return count_zero

    password_part1 = calculate_password_part1(rotations)
    password_part2 = calculate_password_part2(rotations)

    print("Password for part 1:", password_part1)
    print("Password for part 2:", password_part2)

if __name__ == "__main__":
    calculate_day_1_answers()