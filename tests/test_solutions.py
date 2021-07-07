from programs.solution1 import alphasort
from programs.solution2 import fibonacci


def test_alphasort():
    assert alphasort("hello and hello again") == ['again', 'and', 'hello']


def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(9) == 34
