"""Day 2 solution."""
import functools


@functools.cache
def fetch_input():
    """Fetch and cache the input."""
    with open('day2/input', 'r') as f:
        content = f.read()

def part1():
    """Find a*b such that a+b = 2020 and both are in input."""
    with open('day1/input', 'r') as f:
        content = f.read()

    nums = {int(line) for line in content.splitlines()}
    for num in nums:
        if 2020 - num in nums:
            return (2020 - num) * num



def part2():
    """Find a*b*c such that a+b+c = 2020 and all are in input."""
    with open('day1/input', 'r') as f:
        content = f.read()

    nums = {int(line) for line in content.splitlines()}
    for i, a in enumerate(nums):
        for j, b in enumerate(itertools.islice(nums, i + 1, None)):
            c = 2020 - (a + b)
            if c in nums and c in list(nums)[j+1:]:
                return a * b * c


if __name__ == '__main__':
    print(part1())
    print(part2())
