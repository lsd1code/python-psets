from bank import value

def test_hello():
    assert value('Hello, customer') == 0
    
def test_h_greeting():
    assert value('Hi customer') == 20

def test_no_hello():
    assert value('Good evening') == 100

def test_no_greeting():
    assert value('') == 100