def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        answer = fibonacci(n - 1) + fibonacci(n - 2)
        return answer


if __name__ == "__main__":
    n = int(input("Enter nth number: "))
    print(fibonacci(n))
