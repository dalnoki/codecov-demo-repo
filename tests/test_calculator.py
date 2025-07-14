from src.calculator import add, subtract, multiply, divide, power, power2, power3, power4, power5

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -3) == -8

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 1) == -1
    assert subtract(10, 10) == 0
    assert subtract(-3, -2) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3
    assert divide(0, 5) == 0
    
    # Test division by zero error
    try:
        divide(5, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5
    assert power(0, 5) == 0

def test_power2():
    assert power2(2, 3) == 8
    assert power2(5, 0) == 1
    assert power2(2, -1) == 0.5
    assert power2(0, 5) == 0

def test_power3():
    assert power3(2, 3) == 8
    assert power3(5, 0) == 1
    assert power3(2, -1) == 0.5
    assert power3(0, 5) == 0

def test_power4():
    assert power4(2, 3) == 8
    assert power4(5, 0) == 1
    assert power4(2, -1) == 0.5
    assert power4(0, 5) == 0

def test_power5():
    assert power5(2, 3) == 8
    assert power5(5, 0) == 1
    assert power5(2, -1) == 0.5
    assert power5(0, 5) == 0
