from twttr import shorten

def test_shorten():
    # 1. Basic Functionality
    assert shorten("Daniel") == "Dnl", "Failed: Basic word (Daniel)"
    assert shorten("twitter") == "twttr", "Failed: Basic word (twitter)"

    # 2. Handling All Vowels and Consonants
    assert shorten("aeiouAEIOU") == "", "Failed: All Vowels"
    assert shorten("rhythm") == "rhythm", "Failed: No Vowels"

    # 3. Handling Case Sensitivity (using .lower())
    assert shorten("COMPUTER SCIENCE") == "CMPTR SCNC", "Failed: All Caps"
    assert shorten("America") == "mrc", "Failed: Mixed Case"

    # 4. Handling Non-Alphabetic Characters (The Fix for the Previous Error)
    assert shorten("What's 123 up?") == "Wht's 123 p?", "Failed: Numbers & Punctuation"
    assert shorten("CS50") == "CS50", "Failed: Alphanumeric"

    # 5. Handling Empty/Edge Cases
    assert shorten("") == "", "Failed: Empty String"
    assert shorten(" ") == " ", "Failed: Single Space"


if __name__ == "__main__":
    test_shorten()
