from algorithm import check_hand,counter

with open('test.txt', 'r') as file:
    for line in file.readlines():
        card = line.rstrip().split(' ')

        if card[0] == 'texas-holdem':
            print('Not ready yet')

        elif card[0] == 'omaha-holdem':
            print('Not ready yet')
        elif card[0] == 'five-card-draw':
            hands = card[1:]
            solution = []
            for hand in hands:
                solution.append(check_hand(hand=hand))
            solution = [i for i in sorted(solution, key=lambda x: x[0])]
            print(str(solution))
        else:
            print('Error')




