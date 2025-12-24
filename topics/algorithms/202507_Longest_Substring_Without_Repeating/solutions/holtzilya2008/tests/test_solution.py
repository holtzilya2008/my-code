import pytest
from typing import Any
from python_solution import find_longest_substring_length


@pytest.mark.parametrize('input, expected_result', [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('a', 1),
    ('', 0),
    ('ab', 2),
    ('aa', 1),
    ('abcdefghijklmnopqrstuvwxyz0123456789a1', 36)
])
def test_happy_flow(input: str, expected_result: int):
    actual_result = find_longest_substring_length(input)
    assert actual_result == expected_result


@pytest.mark.parametrize('input', [
        None,
        1,
        [],
        {}
    ])
def test_invalid_inputs(input: Any):
    with pytest.raises(TypeError):
        find_longest_substring_length(input)
