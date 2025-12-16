import numpy as np
from pathlib import Path

def calculate_day_6_answers():
    def separate_by_specific_lengths(str_line, lengths):
        output = []
        curr_index = 0
        prev_index = 0
        for i in lengths:
            curr_index += i
            curr_str = str_line[prev_index:curr_index].replace(" ", "X")
            prev_index = curr_index + 1
            curr_index += 1
            output.append(curr_str)
        return output

    def solve_part_1(vals, symb):
        out = 0
        for ind in range(len(symb)):
            nums = [int(vals[i][ind]) for i in range(len(vals))]
            sol = symb[ind].join([str(n) for n in nums])
            esol = eval(sol)
            out += esol
        print("Part 1:", out)

    def solve_part_2(lines, arrs):
        len_count_for_separators = [max([len(str(x)) for x in row]) for row in np.array(arrs[:-1]).transpose()]
        out_arr = np.array([separate_by_specific_lengths(line, len_count_for_separators) for line in lines[:-1]]).transpose()
        symb = arrs[-1]
        new_arr = []
        for row in out_arr:
            curr_arr = np.array([[char for char in word] for word in row]).transpose()
            new_arr.append([''.join([j for j in i if j != "X"]) for i in curr_arr])
        final_output = sum([eval(symb[i].join(new_arr[i])) for i in range(len(symb))])
        print("Part 2:", final_output)

    data_path = Path(__file__,"..", "..", "data", "day6.txt").resolve()
    arrs = []
    lines = []
    with open(data_path, 'r') as file:
        for line in file:
            lines.append(line.rstrip('\n'))
            arrs.append([l for l in line.rstrip('\n').split(' ') if l != ''])
    vals = arrs[:-1]
    symb = arrs[-1]

    solve_part_1(vals, symb)
    solve_part_2(lines, arrs)

if __name__ == "__main__":
    calculate_day_6_answers()