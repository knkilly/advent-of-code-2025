from typing import List

def read_lines_to_list(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')  # Remove trailing newline character
            lines.append(line)
    return lines
