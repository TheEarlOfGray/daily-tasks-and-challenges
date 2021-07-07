from programs.solution1 import alphasort


def test_alphasort():
    assert alphasort("hello and hello again") == ['again', 'and', 'hello']
