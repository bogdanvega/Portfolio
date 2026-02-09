import pytest
from main import count_word_matches

def test_count_word_matches_basic():
    assert count_word_matches(text="The cat sat on the mat", target="cat") == 1

def test_count_word_matches_case_insensitive():
    assert count_word_matches(text="Dog dog DOG dOg", target="dog") == 4

pytest.main()