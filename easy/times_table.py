print("Welcome to the times table calculator")
req = int(input("Please provide a number: "))

for i in range(1, req + 1):
    for j in range(1, 11):
        print(j * i, end=" ")
    print("\n")