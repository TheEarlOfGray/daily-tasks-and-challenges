def even_numbers(num1, num2):
    for i in range(num1, num2 + 1):
        for j in str(i):
            if (int(j) % 2) == 0:
                continue
            elif (int(j) % 2) == 0 and i.index(j) == len(i) - 1:
                print(i)


numb1 = int(input("First number: "))
numb2 = int(input("Secong number: "))

even_numbers(numb1, numb2)
