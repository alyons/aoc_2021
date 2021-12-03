from AoC2021.day_01 import increase_count, sum_increase_count

from typing import List

def increase_count(array: List[int]) -> int:
    count = 0
    i = 1

    while i < len(array):
        if (array[i] > array[i - 1]):
            count += 1
        i += 1

    return count


def sum_increase_count(array: List[int]) -> int:
    count = 0
    sums = []

    for i in range(len(array) - 2):
        second = i + 1
        third = i + 2

        sums.append(array[i])
        sums[i] += array[second]
        sums[i] += array[third]

    return increase_count(sums)


def main():
    print('Welcome to Day 01 of Advent of Code 2021')

    test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    data = []
    with open('./data/day_01.txt') as f:
        for line in f:
            data.append(int(line))

    count = increase_count(data)

    print('Increase Count: %d' % count)

    sum_count = sum_increase_count(data)

    print('Sum Increase Count: %d' % sum_count)



if __name__ == '__main__':
    main()
