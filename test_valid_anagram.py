import pytest
from valid_anagram import is_anagram


test_cases = (
    ('srt', 'trs', True),
    ('hello', 'helloo', False),
    ('str', 'sta', False),
    ('str', 'str', True),
    ('a', 'b', False),
    ('a', 'a', True)
)


@pytest.mark.parametrize(('input_s', 'input_t', 'expected'), test_cases)
def test_is_anagram(input_s, input_t, expected):
    assert is_anagram(input_s, input_t) == expected
