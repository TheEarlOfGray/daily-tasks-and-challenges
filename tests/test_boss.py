from programs.boss.boss import good_boss, bad_boss, not_a_boss


def test_good_boss():
    assert good_boss("dave") == "dave is a good boss!"


def test_bad_boss():
    assert bad_boss("dave") == "dave is a bad boss!"


def test_not_a_boss():
    assert not_a_boss("dave") == "dave is not even a boss!"
