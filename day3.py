import re
from typing import List, Literal, Tuple, Union

Command = Union[Tuple[int, int], Literal["enable", "disable"]]

def parse_input(file_path, split_char='\n') -> List[Command]:
    result = []

    with open(file_path, 'r') as file:
        contents = file.read()
        matches = re.findall("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", contents)
        for x,y,do,dont in matches:
            if do:
                result.append("enable")
            elif dont:
                result.append("disable")
            else:
                result.append((int(x), int(y)))
    return result

def mul_sum_cmds(cmds: List[Command]) -> int:
    enabled = True
    result = 0
    for cmd in cmds:
        if cmd == 'enable':
            enabled = True
        elif cmd == 'disable':
            enabled = False
        elif enabled and isinstance(cmd, tuple):
            result += cmd[0] * cmd[1]
        elif not enabled:
            continue
        else:
            print("Encountered unknown command:", cmd)
    return result



if __name__ == '__main__':
    cmds = parse_input("./inputs/day3.txt")

    mul_sum = sum([cmd[0] * cmd[1] for cmd in cmds if isinstance(cmd, tuple)])
    print("Sum of muls:", mul_sum)
    
    mul_sum_2 = mul_sum_cmds(cmds)
    print("Sum of muls (toggled):", mul_sum_2)
