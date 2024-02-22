from NSD import find_gcd


def test_find_gcd_positive_numbers():
    assert find_gcd(10, 5) == 5  # НСД(10, 5) = 5
    assert find_gcd(14, 28) == 14  # НСД(14, 28) = 14
    assert find_gcd(21, 14) == 7  # НСД(21, 14) = 7
    assert find_gcd(8, 12) == 4  # НСД(8, 12) = 4
    assert find_gcd(18, 27) == 9  # НСД(18, 27) = 9


def test_find_gcd_negative_numbers():
    assert find_gcd(-10, 5) == 5  # НСД(-10, 5) = 5
    assert find_gcd(10, -5) == 5  # НСД(10, -5) = 5
    assert find_gcd(-10, -5) == 5  # НСД(-10, -5) = 5


def test_find_gcd_zero():
    assert find_gcd(0, 5) == 5  # НСД(0, 5) = 5
    assert find_gcd(10, 0) == 10  # НСД(10, 0) = 10
    assert find_gcd(0, 0) == 0  # НСД(0, 0) = 0


def test_find_gcd_same_number():
    assert find_gcd(10, 10) == 10  # НСД(10, 10) = 10
    assert find_gcd(15, 15) == 15  # НСД(15, 15) = 15
    assert find_gcd(0, 0) == 0  # НСД(0, 0) = 0
