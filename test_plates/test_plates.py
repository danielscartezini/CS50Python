from plates import is_valid

def test_min_max_length():
    """Tests for minimum (2) and maximum (6) character lengths."""
    # Valid lengths
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    # Invalid lengths
    assert is_valid("A") == False      # Too short (Min 2)
    assert is_valid("AAAAAAA") == False # Too long (Max 6)

def test_start_with_two_letters():
    """Tests the rule that plates must start with at least two letters."""
    # Valid starts
    assert is_valid("CS50") == True
    assert is_valid("HA") == True
    # Invalid starts
    assert is_valid("C5") == False     # Letter/Number
    assert is_valid("50") == False     # Number/Number
    assert is_valid("5C") == False     # Number/Letter

def test_numbers_placement():
    """Tests that numbers are at the end and the first number is not '0'."""
    # Valid number placement
    assert is_valid("AAA222") == True
    assert is_valid("HI4") == True
    # Invalid placement: Number in the middle (followed by a letter)
    assert is_valid("AAA22A") == False
    assert is_valid("CS50P") == False
    # Invalid placement: First number is '0'
    assert is_valid("CS05") == False
    assert is_valid("AA0") == False

def test_zero_in_middle():
    """Tests plates where '0' is not the first number but appears later."""
    # The rule is ONLY about the *first* number being '0', not subsequent ones.
    # The logic in your provided code correctly handles this.
    assert is_valid("AAA500") == True

def test_punctuation_and_spaces():
    """Tests the rule against periods, spaces, and punctuation marks."""
    # Invalid characters
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS!0") == False
    assert is_valid("CS,") == False
