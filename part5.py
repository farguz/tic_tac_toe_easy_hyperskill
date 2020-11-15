# https://hyperskill.org/projects/73/stages/403/implement
#  TIC TAC TOE GAME silly solution since you're doing it stage by stage


def print_field(user_input):
    print('---------')
    print('| {} {} {} |'.format(user_input[0], user_input[1], user_input[2]))
    print('| {} {} {} |'.format(user_input[3], user_input[4], user_input[5]))
    print('| {} {} {} |'.format(user_input[6], user_input[7], user_input[8]))
    print('---------')


def three_in_row(xlist, user_input):
    global flag
    win_list = ['XXX', 'OOO']
    count = 0
    for item in xlist:
        if item in win_list:
            count += 1
    # fair game
    if count == 1 or count == 2:
        flag = False
        print_field(user_input)
        if win_list[0] in xlist:
            print('X wins')
        else:
            print('O wins')
        return
    # no duplicate winning positions
    # no too much x's or o's
    count_o, count_x = user_input.count('O'), user_input.count('X')
    if (count_x + count_o) == 9:
        flag = False
        print_field(user_input)
        print('Draw')
    return


def analyze_field(user_input):
    # create lists of lists with all possible winning combinations (entire row/column or diagonal)
    position_list_rows = [user_input[i:i + 3] for i in range(0, 9, 3)]
    position_list_columns = [user_input[i::3] for i in range(0, 3)]
    position_list_diag = [user_input[0::4], user_input[2:7:2]]
    return position_list_columns + position_list_rows + position_list_diag


def take_and_check_coordinates(user_input):
    # field STR [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
    field = [[str(x), str(y)] for x in range(1, 4) for y in range(1, 4)]
    while True:
        coordinates = input('Enter the coordinates: ').split(' ')
        for numb in coordinates:
            if numb not in '0123456789':
                print('You should enter numbers!')
        if coordinates not in field:
            print('Coordinates should be from 1 to 3!')
        #  later better convert both coordinates (coordinates and user_input) to same grid
        elif coordinates == field[0] and user_input[6] in ['O', 'X'] \
                or coordinates == field[1] and user_input[3] in ['O', 'X'] \
                or coordinates == field[2] and user_input[0] in ['O', 'X'] \
                or coordinates == field[3] and user_input[7] in ['O', 'X'] \
                or coordinates == field[4] and user_input[4] in ['O', 'X'] \
                or coordinates == field[5] and user_input[1] in ['O', 'X'] \
                or coordinates == field[6] and user_input[8] in ['O', 'X'] \
                or coordinates == field[7] and user_input[5] in ['O', 'X'] \
                or coordinates == field[8] and user_input[2] in ['O', 'X']:
            print('This cell is occupied! Choose another one!')
        else:
            for i in range(9):  # search where to put X (odd moves) or O (even moves) in user_input
                if i in [1, 3, 5, 7, 9]:
                    symb = 'O'
                else:
                    symb = 'X'
                if coordinates == field[i]:
                    if i == 0:
                        user_input = ''.join([symb if j == 6 else user_input[j] for j in range(9)])
                    if i == 1:
                        user_input = ''.join([symb if j == 3 else user_input[j] for j in range(9)])
                    if i == 2:
                        user_input = ''.join([symb if j == 0 else user_input[j] for j in range(9)])
                    if i == 3:
                        user_input = ''.join([symb if j == 7 else user_input[j] for j in range(9)])
                    if i == 4:
                        user_input = ''.join([symb if j == 4 else user_input[j] for j in range(9)])
                    if i == 5:
                        user_input = ''.join([symb if j == 1 else user_input[j] for j in range(9)])
                    if i == 6:
                        user_input = ''.join([symb if j == 8 else user_input[j] for j in range(9)])
                    if i == 7:
                        user_input = ''.join([symb if j == 5 else user_input[j] for j in range(9)])
                    if i == 8:
                        user_input = ''.join([symb if j == 2 else user_input[j] for j in range(9)])
            break
    #  return updated user_input
    return user_input


user_input = '         '
flag = True
while flag:
    print_field(user_input)
    user_input = take_and_check_coordinates(user_input)
    three_in_row(analyze_field(user_input), user_input)
