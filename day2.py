from typing import List, Literal, Optional


def parse_input(file_path, split_char='\n') -> List[List[int]]:
    reports = []

    with open(file_path, 'r') as file:
        lines = file.read().split(split_char)
        for line in lines:
            if line == '':
                continue

            report = [int(x) for x in line.split(' ')]
            reports.append(report)
    return reports

def is_report_safe(report: List[int], dampen_problem: bool = False) -> bool:
    assert len(report) >= 2

    increasing = report[1] > report[0]
    for prev, cur in zip(report, report[1:]):
        diff = cur - prev
        problem = (increasing and not (diff >= 1 and diff <= 3)) or ((not increasing) and not (diff <= -1 and diff >= -3))
        if problem and not dampen_problem:
            return False
        elif problem and dampen_problem:
            return any(is_report_safe(report[:i] + report[i+1:]) for i in range(len(report)))

    return True

def count_safe_reports(reports: List[List[int]]) -> int:
    return sum([1 if is_report_safe(report) else 0 for report in reports])

def count_safe_reports_dampened(reports: List[List[int]]) -> int:
    return sum([1 if is_report_safe(report, True) else 0 for report in reports])

if __name__ == '__main__':
    reports = parse_input("./inputs/day2.txt")
    safe_reports = count_safe_reports(reports)
    safe_reports_dampened = count_safe_reports_dampened(reports)

    print("Number of safe reports:", safe_reports)
    print("Number of safe reports (dampened):", safe_reports_dampened)
