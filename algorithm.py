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


solution_list = [(2, '5s5d7s4dQd'), (2, '3cKs4cKdJs'), (3, '4s4hTsTh9h'),
                 (5, '7h6h8d9cTc'), (6, '2hAhKh4hKh'), (7, 'QcQd7c7c7d'), (9, '6c2c3c4c5c')]



def solution_sort(hands):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(hands) - 1):
            if hands[i][0] > hands[i + 1][0]:
                # Меняем элементы
                hands[i], hands[i + 1] = hands[i + 1], hands[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
            elif hands[i][0] == hands[i + 1][0]:
                if equal_sort(hands[i],hands[i + 1], hands[i][0]):
                    hands[i], hands[i + 1] = hands[i + 1], hands[i]
                    swapped = True



# def equal_sort(first_hand, other_hand, hand_rating):
#     if hand_rating == 1:
#         if high_card_equal(first_hand, other_hand):



#     elif hand_rating == 2:
#         if True:
#             return True
#         else:
#             return False
#     elif hand_rating == 3:
#         if True:
#             return True
#         else:
#             return False
#     elif hand_rating == 4:
#         if True:
#             return True
#         else:
#             return False
#     elif hand_rating == 5:
#         if True:
#             return True
#         else:
#             return False
#     elif hand_rating == 6:
#         if True:
#             return True
#         else:
#             return False
#     elif hand_rating == 7:
#         if True:
#             return True
#         else:
#             return False
#     elif hand_rating == 8:
#         if True:
#             return True
#         else:
#             return False
#     elif hand_rating == 9:
#         if True:
#             return True
#         else:
#             return False

hand1 ='QsJd7s4dQd'
hand2 = '3cQs4cQdTs'

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key

def separator(hand, value):
    if value == 2:
        counted_card = counter(hand)
        card = get_key(2, counted_card[0])
        pair = []
        cards = []
        for i in hand:
            if i[0] == card:
                pair.append(i)
            else:
                cards.append(i)
        separate_card = (pair,cards)
        return separate_card




def high_card_equal(hand1,hand2):
    hand1_list = [i[2] for i in sorted_cards(hand=hand1)]
    hand2_list = [i[2] for i in sorted_cards(hand=hand2)]
    n = -1
    for i in range(len(hand1_list)-1):
        if hand1_list[n] > hand2_list[n]:
            print(hand1_list)
            return True
        elif hand1_list[n] == hand2_list[n]:
            n -= 1
        else:
            print(hand2_list)
            return False


def pair_equal(hand1, hand2):
    pass



def two_pair_equal(hand1, hand2):
    pass


def three_of_a_kind_equal(hand1, hand2):
    pass


def four_of_a_kind(hand1, hand2):
    pass


def full_house_equal(hand1,hand2):
    pass



print(separator('7hQsQh8c9h', 2))






























