def print_tic_tac():
    print(f'''---------
| {symbols[0]} {symbols[1]} {symbols[2]} |
| {symbols[3]} {symbols[4]} {symbols[5]} |
| {symbols[6]} {symbols[7]} {symbols[8]} |
---------''')


symbols = [' ' for x in range(9)]
cartesian = ['13', '23', '33', '12', '22', '32', '11', '21', '31']
win_state = ['012', '345', '678', '036', '147', '258', '048', '642']
print_tic_tac()
symbol = True

while True:
    coordinates = input('Enter the coordinates: > ').split()
    error_state = None
    if len(coordinates) < 2 or coordinates[0] not in '123' and coordinates[1] not in '123':
        error_state = 'You should enter numbers!'
    elif coordinates[0] in '123' and coordinates[1] in '123':
        number = cartesian.index(coordinates[0] + coordinates[1])
        if symbols[number] == ' ':
            symbols[number] = 'X' if symbol else 'O'
            symbol = not symbol
            print_tic_tac()
        else:
            error_state = 'This cell is occupied! Choose another one!'
    else:
        error_state = 'Coordinates should be from 1 to 3!'
    if error_state is not None:
        print(error_state)
        continue
    for i in win_state:
        if all(symbols[int(j)] == 'X' for j in i):
            print('X wins')
            exit()
        elif all(symbols[int(j)] == 'O' for j in i):
            print('O wins')
            exit()
    if ' ' not in symbols:
        print('Draw')
        exit()
