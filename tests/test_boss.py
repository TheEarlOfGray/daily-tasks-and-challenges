import pytest
from programs.boss.boss import good_boss, bad_boss, not_a_boss


def test_good_boss():
    assert good_boss("dave") == "dave is a good boss!"
