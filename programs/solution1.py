def alphasort(var1):
    answer = sorted(set(list(var1.split(" "))))
    return answer


if __name__ == "__main__":
    result = input("Gimme a sentance: ")
    print(alphasort(result))
