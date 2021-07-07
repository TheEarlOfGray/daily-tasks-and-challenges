def print_grades(grade_m, grade_c, grade_p):
    result = (grade_m + grade_c + grade_p) / 3

    print(f"Your percentage score is: {result}%")

    if result < 40:
        return "YOU ARE A FAILURE!!!"
    elif result >= 40 and result < 50:
        return "Your grade is: D"
    elif result >= 50 and result < 60:
        return "Your grade is: C"
    elif result >= 60 and result < 70:
        return "Your grade is: B"
    else:
        return "Your grade is: A"


if __name__ == "__main__":
    print("Welcome to grade calculator")
    grade_m = int(input("Please enter your maths mark: "))
    grade_c = int(input("Please enter your chemistry mark: "))
    grade_p = int(input("Please enter your physics mark: "))
    print(print_grades(grade_m, grade_c, grade_p))
