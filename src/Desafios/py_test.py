def soma_1(x):
    return x + 1

def test_soma_1():
    assert soma_1(4) == 5

def fat(n):
    if n < 0:
        return 0
    fat = 1
    for c in range(1, n+1):
        fat *= c
    return fat

def test_fat0():
    assert fat(0) == 1

def test_fat1():
    assert fat(1) == 1

def test_fat5():
    assert fat(5) == 120

def test_fatneg():
    assert fat(-3) == 0