from pathlib import Path

def calculate_day_5_answers():
    def merge_ranges(ranges):
        sorted_ranges = sorted(ranges, key=lambda x: x[0])
        merged = []
        for current in sorted_ranges:
            if not merged or merged[-1][1] < current[0]:
                merged.append(current)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
        return merged

    def solve_part_1(rows, ids_to_check):
        c = 0
        for id in ids_to_check:
            for check_range in rows:
                if check_range[0] <= id <= check_range[1]:
                    c += 1
                    break
        print("Part 1:", c)

    def solve_part_2(rows):
        merge_rows = merge_ranges(rows)
        print("Part 2:", sum([r[1] - r[0] + 1 for r in merge_rows]))

    data_path = Path(__file__,"..", "..", "data", "day5.txt").resolve()
    arrs = [[], []]
    arr_ind = 0
    with open(data_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if line == "":
                arr_ind = 1
            arrs[arr_ind].append(line)
    rows = [ [int(x) for x in rg.split('-')] for rg in arrs[0]]
    ids_to_check = [int(i) for i in arrs[1][1:]]

    solve_part_1(rows, ids_to_check)
    solve_part_2(rows)

if __name__ == "__main__":
    calculate_day_5_answers()