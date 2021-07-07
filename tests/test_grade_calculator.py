from programs.easy.grade_calculator import print_grades


def test_print_grades():
    assert print_grades(50, 50, 50) == "Your grade is: C"
