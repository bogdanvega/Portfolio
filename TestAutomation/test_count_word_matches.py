import pytest
from main import count_word_matches

def test_count_word_matches_basic():
    assert count_word_matches(text="The cat sat on the mat", target="cat") == 1

pytest.main()