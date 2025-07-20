import pytest
from python_solution import find_longest_substring


@pytest.mark.parametrize('input, expected_result', [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3)
])
def test_solution(input: str, expected_result: int):
    actual_result = find_longest_substring(input)
    assert actual_result == expected_result
