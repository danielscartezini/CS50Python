from seasons import main, validate_date_of_birth

def main():
    test_check_birthday()

def test_check_birthday():
    assert validate_date_of_birth("2006-12-01") == ('2006', '12', '01')

