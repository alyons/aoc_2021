from typing import Dict, List, Set, Tuple
from numpy import ndarray
import re


def parse_file(file: str) -> List[str]:
    data = []

    with open(file) as f:
        for line in f:
            data.append(line.strip())

    return data


def parse_int_file(file: str) -> List[int]:
    data = []

    with open(file) as f:
        for line in f:
            data.append(int(line))

    return data


def parse_bingo_file(file: str) -> Tuple[List[int], List[ndarray]]:
    numbers = []
    boards = []
    temp_board = []
    
    with open(file) as f:
        for line in f:
            if len(numbers) == 0:
                numbers = list(map(int, line.split(',')))
            elif not line == '\n':
                temp_board.append(list(map(int, list(filter(None, line.strip().split(' '))))))
                if len(temp_board) == 5:
                    boards.append(temp_board.copy())
                    temp_board.clear()

    return (numbers, boards)


def parse_int_count(file: str) -> dict:
    values = {}

    with open(file) as f:
        for line in f:
            array = [int(item) for item in line.split(',')]
            for item in array:
                if item in values:
                    values[item] += 1
                else:
                    values[item] = 1

    return values


def parse_octopus_grid(file: str) -> List[List[int]]:
    grid = []

    with open(file) as f:
        for line in f:
            row = [int(x) for x in line.strip()]
            if row: grid.append(row)
    
    return sum(grid, [])


def parse_cave_graph(file: str) -> List[str]:
    edges = []

    with open(file) as f:
        for line in f:
            edge = line.strip().split('-')
            edges.append(edge)

    return edges


def parse_manual(file: str) -> Tuple:
    points = []
    folds = []

    fold_ptn = re.compile(r'fold along (?P<axis>[xy])=(?P<number>\d+)')

    with open(file) as f:
        for line in f:
            if ',' in line:
                point = [int(d) for d in line.strip().split(',')]
                points.append(point)
            else:
                m = fold_ptn.match(line.strip())
                if m:
                    fold = (m.group(1), int(m.group(2)))
                    folds.append(fold)

    return (points, folds)


def parse_polymer_formula(file: str) -> Tuple[str, Dict, Dict]:
    template = ''
    rules = {}
    elements = {}

    with open(file) as f:
        for line in f:
            if not template and not '->' in line:
                template = line.strip()
                for t in template:
                    elements[t] = 0
            elif '->' in line:
                pair = line.strip().split('->')
                rules[pair[0].strip()] = pair[1].strip()
                for p in pair:
                    for i in p.strip():
                        elements[i] = 0

    return (template, rules, elements)


def parse_chiton_cave(file: str) -> Tuple[List[int], int]:
    grid = []
    row_len = 0

    with open(file) as f:
        for line in f:
            if not row_len: row_len = len(line.strip())
            row = [int(x) for x in line.strip()]
            if row: grid.append(row)
    
    return (sum(grid, []), row_len)


def sort_string(value: str) -> str:
    _l = sorted(value)
    return ''.join(_l)


def replace_character_at_index(string: str, character: str, index: int) -> str:
    


    return string
