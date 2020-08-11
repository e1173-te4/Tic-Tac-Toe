read_string = input()
print([(int(read_string[x]) + int(read_string[x + 1])) / 2 for x in range(len(read_string) - 1)])