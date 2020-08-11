number = int(input())
for i in range(number + 1):
    print(('#' * (i * 2 - 1)).center(number * 2 - 1) for i in range(number + 1))
