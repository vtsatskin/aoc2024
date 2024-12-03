import re
from typing import List, Tuple


def parse_input(file_path, split_char='\n') -> List[Tuple[int, int]]:
    result = []

    with open(file_path, 'r') as file:
        contents = file.read()
        matches = re.findall('mul\((\d+),(\d+)\)', contents)
        for x,y in matches:
            result.append((int(x), int(y)))
    return result

def mul_sum(nums: List[Tuple[int, int]]) -> int:
    return 

if __name__ == '__main__':
    nums = parse_input("./inputs/day3.txt")
    mul_sum = sum([x * y for x, y in nums])
    print("Sum of muls:", mul_sum)
