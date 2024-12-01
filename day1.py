from typing import List, Tuple


def parse_input(file_path, split_char='\n') -> Tuple[List[int], List[int]]:
    list_left = []
    list_right = []

    with open(file_path, 'r') as file:
        lines = file.read().split(split_char)
        for line in lines:
            if line == '':
                continue

            [left, right] = line.split('   ')
            list_left.append(int(left))
            list_right.append(int(right))
    return list_left, list_right
            
def sum_diff(left: List[int], right: List[int]) -> int:
    sum = 0
    for [x, y] in zip(left, right):
        sum += abs(x - y)
    return sum

def frequency(arr: List[int]) -> dict[int, int]:
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

def similarity_score(left: List[int], right: List[int]) -> int:
    right_freq = frequency(right)

    sum = 0
    for x in left:
        sum += x * right_freq.get(x, 0)
    return sum
    

if __name__ == '__main__':
    [left, right] = parse_input("inputs/day1.txt")

    # Part 1:
    left_sorted = sorted(left)
    right_sorted = sorted(right)

    sum_diffs = sum_diff(left_sorted, right_sorted)
    print("Sum of differences:", sum_diffs)

    # Part 2:
    similarity = similarity_score(left, right)
    print("Similarity score:", similarity)
