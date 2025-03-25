from palindrom import palindrom
from rover import Rover


def test_palindrom():
    assert palindrom('radar') == True
    assert palindrom('flower') == False


def test_rover():
    assert Rover().position(0, 0) == [0, 0]

