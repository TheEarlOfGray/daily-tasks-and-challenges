print("Welcome to the ISBN check-digit calculator")
isbn = input("Please enter the ISBN: ")


def cd_calc(isbn):
    index = 0
    check_digit = 0
    for digit in isbn:
        if (index % 2) == 0:
            check_digit = check_digit + int(digit)
            index += 1
        else:
            check_digit = check_digit + (int(digit) * 3)
            index += 1
    check_digit = str((10 - (int(check_digit) % 10)))
    return check_digit


check_digit = cd_calc(isbn)

print(isbn, check_digit)
