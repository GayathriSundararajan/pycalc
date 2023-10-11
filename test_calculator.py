
from Calculator import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(3, 1) == 2
    assert subtract(5, 7) == -2
    assert subtract(0, 0) == 0
