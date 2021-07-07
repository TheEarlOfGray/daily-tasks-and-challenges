from programs.dice.dice import die_roll


def test_die_roll():
    assert die_roll() >= 1
    assert die_roll() <= 6
