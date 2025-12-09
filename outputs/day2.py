import os
from pathlib import Path

def calculate_day_2_answers():
    data_path = Path(__file__,"..", "..", "data", "day2.txt").resolve()

    def is_irregular_id_part_1(id_str):
        return len(id_str) % 2 == 0 and id_str[:len(id_str)//2] == id_str[len(id_str)//2:]

    def is_invalid_id_part_2(id_str):
        return any(id_str == id_str[:i] * (len(id_str) // i) for i in range(1, len(id_str) // 2 + 1) if len(id_str) % i == 0)
    
    def calculate_total(id_ranges, is_invalid_id):
        total = 0
        for r in id_ranges:
            minr, maxr = r.split('-')
            for i in range(int(minr), int(maxr) + 1):
                id_str = str(i)
                if is_invalid_id(id_str):
                    total += int(id_str)
        return total

    with open(data_path, 'r') as file:
        id_ranges = file.readline().split(',')
        print("Part 1 answer:", calculate_total(id_ranges, is_irregular_id_part_1))
        print("Part 2 answer:", calculate_total(id_ranges, is_invalid_id_part_2))

if __name__ == "__main__":
    calculate_day_2_answers()