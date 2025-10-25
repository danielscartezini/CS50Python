from jar import Jar

global_jar = Jar()

def main():
    #test_Jar_cookies()
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    print("You have passed all your tests!")

def test_init():
    assert global_jar.capacity == 12
    assert global_jar._size == 0

def test_str():
    global_jar.deposit(5)
    assert str(global_jar) == '🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3

def test_withdraw():
    global_jar.withdraw(2)
    assert global_jar.size == 3

"""
def test_Jar_cookies():
    assert Jar(capacity=10).deposit(5) == None
    assert Jar(capacity=10).withdraw(2) == None
"""

if __name__ == "__main__":
    main()
