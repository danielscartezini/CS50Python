from bank import value

def test_value_zero():
    assert value("hello") == 0
    assert value("Hello, World!") == 0
    assert value("hElLo ThErE") == 0

def test_value_twenty():
    assert value("h") == 20
    assert value("Hi") == 20
    assert value("How are you?") == 20
    assert value("Heeey") == 20

def test_value_one_hundred():
    assert value("G'day") == 100
    assert value("What's up?") == 100
    assert value("Welcome") == 100
    assert value("") == 100
    assert value("T") == 100
