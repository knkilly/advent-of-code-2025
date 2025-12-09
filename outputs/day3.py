from pathlib import Path

def calculate_day_3_answers():
    data_path = Path(__file__,"..", "..", "data", "day3.txt").resolve()
    def calculate_part_1_answer(banks):
        total = 0
        for bank in banks:
            bank = [int(x) for x in bank]
            max_b = max(bank[:-1])
            next_max_b = max(bank[bank.index(max_b) + 1:])
            total += int(f"{max_b}{next_max_b}")
        return print(total)
    
    def calculate_part_2_answer(banks, num_digits):
        def find_max_joltage(bank, num_digits):
            joltage = []
            sub_bank = bank
            for i in range(num_digits - 1):
                max_digit = max(sub_bank[:-num_digits+i+1])
                max_index = sub_bank.index(max_digit)
                joltage.append(str(max_digit))
                sub_bank = sub_bank[max_index+1:]
            last_digit = max(sub_bank)
            joltage.append(str(last_digit))
            return int(''.join(joltage))
        total = 0
        for bank in banks:
            bank = [int(x) for x in bank]
            max_joltage = find_max_joltage(bank, num_digits)
            total += max_joltage
        return print(total)

    with open(data_path, 'r') as file:
        banks = [i.split('\n')[0] for i in file.readlines()]
        calculate_part_1_answer(banks)
        calculate_part_2_answer(banks, 12)

if __name__ == "__main__":
    calculate_day_3_answers()