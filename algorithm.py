from collections import Counter
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
          'Q': 12, 'K': 13, 'A': 14,
          }
straight_string = '23456789TJQKA'


def sorted_cards(board='', hand=''):
    cards = board+hand
    card_list = list(zip(cards[::2], cards[1::2]))
    sorted_card_list = []
    for card in card_list:
        if card[0] in values.keys():
            card_values = (card[0], card[1], values[card[0]])
            sorted_card_list.append(card_values)
        else:
            print('Card not found')
    return sorted(sorted_card_list, key=lambda x: x[2])


def counter(board='', hand=''):
    cards = sorted_cards(board, hand)
    card = [i[0] for i in cards]
    suit = [i[1] for i in cards]
    card_counter = dict(Counter(card))
    suit_counter = dict(Counter(suit))
    result = [card_counter, suit_counter]
    return result


def separator(hand, value):
    if value == 2:
        counted_card = counter(hand)
        card = get_key(2, counted_card[0])
        hand_list = [hand[x: x+2] for x in range(0, len(hand), 2)]
        pair_one = []
        cards = []
        for i in hand_list:
            if i[0] == card:
                pair_one.append(i)
            else:
                cards.append(i)
        separate_card = (''.join(pair_one), ''.join(cards))
        return separate_card

    elif value == 3:
        counted_card = counter(hand)
        card_one = get_key(2, counted_card[0])
        card_two = get_key(1, counted_card[0])
        hand_list = [hand[x: x+2] for x in range(0, len(hand), 2)]
        pair_one = []
        pair_two = []
        card = []
        for i in hand_list:
            if i[0] == card_one:
                pair_one.append(i)
            elif i[0] == card_two:
                card.append(i)
            else:
                pair_two.append(i)
        separate_card = (''.join(pair_one), ''.join(pair_two), card[0])
        return separate_card

    elif value == 4:
        counted_card = counter(hand)
        card = get_key(3, counted_card[0])
        hand_list = [hand[x: x + 2] for x in range(0, len(hand), 2)]
        three = []
        cards = []
        for i in hand_list:
            if i[0] == card:
                three.append(i)
            else:
                cards.append(i)
        separate_card = (''.join(three), ''.join(cards))
        return separate_card

    elif value == 8:
        counted_card = counter(hand)
        card = get_key(4, counted_card[0])
        hand_list = [hand[x: x + 2] for x in range(0, len(hand), 2)]
        four = []
        cards = []
        for i in hand_list:
            if i[0] == card:
                four.append(i)
            else:
                cards.append(i)
        separate_card = (''.join(four), cards[0])
        return separate_card

    elif value == 7:
        counted_card = counter(hand)
        card_one = get_key(2, counted_card[0])
        card_two = get_key(3, counted_card[0])
        hand_list = [hand[x: x + 2] for x in range(0, len(hand), 2)]
        three = []
        two = []
        for i in hand_list:
            if i[0] == card_one:
                two.append(i)
            elif i[0] == card_two:
                three.append(i)
        separate_card = (''.join(three), ''.join(two))
        return separate_card


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


def check_straight(board='', hand=''):
    cards = sorted_cards(board, hand)
    card_list = ''.join([i[0] for i in cards])
    if card_list in straight_string and len(card_list) == 5:
        return True
    elif '2345A' in card_list:
        return True
    else:
        return False


def check_flush(board='', hand=''):
    counted_card = counter(board, hand)
    if len(set([i for i in counted_card[1].values()])) == 1:
        return True
    else:
        return False


def check_straight_flush(board='', hand=''):
    if check_flush(board, hand) and check_straight(board, hand):
        return True
    else:
        return False


def pair(board='', hand=''):
    counted_card = counter(board, hand)
    if 2 in list(counted_card[0].values()):
        return True
    else:
        return False


def two_pairs(board='', hand=''):
    counted_card = counter(board, hand)
    pair_list = [i for i in counted_card[0].values()]
    if pair_list.count(2) == 2:
        return True
    else:
        return False


def three_of_a_kind(board='', hand=''):
    counted_card = counter(board, hand)
    if 3 in list(counted_card[0].values()):
        return True
    else:
        return False


def four_of_a_kind(board='', hand=''):
    counted_card = counter(board, hand)
    for i in counted_card[0].values():
        if i == 4:
            return True
        else:
            return False


def full_house(board='', hand=''):
    counted_card = counter(board, hand)
    full_house_list = [i for i in counted_card[0].values()]
    if 3 in full_house_list and 2 in full_house_list:
        return True
    else:
        return False


def check_hand(board='', hand=''):
    card_rating = []
    if pair(board, hand):
        card_rating.append(2)
    if two_pairs(board, hand):
        card_rating.append(3)
    if three_of_a_kind(board, hand):
        card_rating.append(4)
    if check_straight(board, hand):
        card_rating.append(5)
    if check_flush(board, hand):
        card_rating.append(6)
    if full_house(board, hand):
        card_rating.append(7)
    if four_of_a_kind(board, hand):
        card_rating.append(8)
    if check_straight_flush(board, hand):
        card_rating.append(9)
    else:
        card_rating.append(1)
    result = (max(card_rating), hand)
    return result

def solution_sort(hands):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(hands) - 1):
            if hands[i][0] > hands[i + 1][0]:
                hands[i], hands[i + 1] = hands[i + 1], hands[i]
                swapped = True
            elif hands[i][0] == hands[i + 1][0]:
                if equal_sort(hands[i][1], hands[i + 1][1], hands[i][0]):
                    hands[i], hands[i + 1] = hands[i + 1], hands[i]
                    swapped = True


def equal_sort(first_hand, other_hand, hand_rating):
    if hand_rating == 1 and high_card_equal(first_hand, other_hand):
        return True
    elif hand_rating == 2 and pair_equal(first_hand, other_hand):
        return True
    elif hand_rating == 3 and two_pairs_equal(first_hand, other_hand):
        return True
    elif hand_rating == 4 and three_of_a_kind_equal(first_hand, other_hand):
        return True
    elif hand_rating == 5 and straight_equal(first_hand, other_hand):
        return True
    elif hand_rating == 6 and high_card_equal(first_hand, other_hand):
        return True
    elif hand_rating == 7 and full_house_equal(first_hand, other_hand):
        return True
    elif hand_rating == 8 and four_of_a_kind_equal(first_hand, other_hand):
        return True
    elif hand_rating == 9 and straight_equal(first_hand, other_hand):
        return True
    else:
        return False


def high_card(card1, card2):
    if values[card1[0]] > values[card2[0]]:
        return True
    else:
        return False


def high_card_equal(hand1, hand2):
    hand1_list = [i[2] for i in sorted_cards(hand=hand1)]
    hand2_list = [i[2] for i in sorted_cards(hand=hand2)]
    n = -1
    if hand1_list == hand2_list:
        flag = 'Equal'
        return flag

    else:
        for i in range(len(hand1_list)-1):
            if hand1_list[n] > hand2_list[n]:
                return True
            elif hand1_list[n] == hand2_list[n]:
                n -= 1
            else:
                return False


def pair_equal(hand1, hand2):
    hand_one_list = separator(hand1, 2)
    hand_two_list = separator(hand2, 2)
    if high_card_equal(hand_one_list[0], hand_two_list[0]) == 'Equal':
        if high_card_equal(hand_one_list[1], hand_two_list[1]):
            return True
        else:
            return False
    elif high_card_equal(hand_one_list[0], hand_two_list[0]):
        return True

    else:
        return False


def two_pairs_equal(hand1, hand2):
    hand_one_list = separator(hand1, 3)
    hand_two_list = separator(hand2, 3)
    if high_card_equal(hand_one_list[0], hand_two_list[0]) == 'Equal':
        print('sa')
        if high_card_equal(hand_one_list[1], hand_two_list[1]) == 'Equal':
            print('wqqe')
            if high_card(hand_one_list[2], hand_two_list[2]):
                print('adc')
                return True
            else:
                return False
        elif high_card_equal(hand_one_list[0], hand_two_list[0]):
            return True
        else:
            return False
    elif high_card_equal(hand_one_list[0], hand_two_list[0]):
        return True
    else:
        return False


def three_of_a_kind_equal(hand1, hand2):
    hand_one_list = separator(hand1, 4)
    hand_two_list = separator(hand2, 4)
    if high_card_equal(hand_one_list[0], hand_two_list[0]) == 'Equal':
        if high_card_equal(hand_one_list[1], hand_two_list[1]):
            return True
        else:
            return False
    elif high_card_equal(hand_one_list[0], hand_two_list[0]):
        return True

    else:
        return False


def four_of_a_kind_equal(hand1, hand2):
    hand_one_list = separator(hand1, 8)
    hand_two_list = separator(hand2, 8)
    if high_card_equal(hand_one_list[0], hand_two_list[0]) == 'Equal':
        if high_card(hand_one_list[1], hand_two_list[1]):
            return True
        else:
            return False
    elif high_card_equal(hand_one_list[0], hand_two_list[0]):
        return True

    else:
        return False


def full_house_equal(hand1, hand2):
    hand_one_list = separator(hand1, 7)
    hand_two_list = separator(hand2, 7)
    if high_card_equal(hand_one_list[0], hand_two_list[0]) == 'Equal':
        if high_card_equal(hand_one_list[1], hand_two_list[1]):
            return True
        else:
            return False
    elif high_card_equal(hand_one_list[0], hand_two_list[0]):
        return True

    else:
        return False


def straight_equal(hand1, hand2):
    hand1_list = ''.join([i[0] for i in sorted_cards(hand=hand1)])
    print(hand1_list)
    if hand1_list =='2345A':
        return False
    elif high_card_equal(hand1, hand2) and hand1_list!='2345A':
        return True
    else:
        return False


def output(hands):
    solution = []
    for hand in hands:
        solution.append(check_hand(hand=hand))
    solution_sort(solution)
    return ' '.join([x[1] for x in solution])


with open('test.txt', 'r') as file:
    for line in file.readlines():
        card = line.rstrip().split(' ')
        if card[0] == 'texas-holdem':
            print('Not ready yet')
        elif card[0] == 'omaha-holdem':
            print('Not ready yet')
        elif card[0] == 'five-card-draw':
            hands = card[1:]
            with open('solution.txt', 'a') as file:
                file.writelines(output(hands)+'\n')

        else:
            print('Error')































