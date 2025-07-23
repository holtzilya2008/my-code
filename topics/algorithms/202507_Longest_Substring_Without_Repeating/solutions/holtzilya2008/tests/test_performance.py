import time
from python_solution import find_longest_substring_length

EXPECTED_LENGTH = 36
PREFIX_LENGTH = 1_000_000


def build_long_input():
    prefix = 'a' * PREFIX_LENGTH
    middle = 'abcdefghijklmnopqrstuvwxyz0123456789a1'
    suffix = 'k' * PREFIX_LENGTH
    return prefix + middle + suffix


LONG_INPUT = build_long_input()


def test_performance():
    start_time = time.perf_counter()
    result = find_longest_substring_length(LONG_INPUT)
    assert result == EXPECTED_LENGTH
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000 # Milliseconds
    print('Performance test:')
    print(f' Algorithm took {duration:.2f} ms | String length: {len(LONG_INPUT)} chars.')  