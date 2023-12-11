from aocd.models import Puzzle

YEAR = 2023
DAY = 7
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
print(data)
data = data.split("\n")

#Split by space and convert second element to int
data = [x.split(" ") for x in data]
print(data)
data = [[x[0], int(x[1])] for x in data]

def evalute_hand(hand):
    #Count number of J
    J_count = hand.count("J")
    original_hand = hand
    hand = hand.replace("J", "")
    #Five cards of the same suit, in sequence
    if hand == "":
        return 9*(10**20) + add_card_value(original_hand)
    if (any(hand.count(char) == 5-J_count for char in set(hand))):
        return 9*(10**20) + add_card_value(original_hand)
    #Four cards of the same value
    if (any(hand.count(char) == 4-J_count for char in set(hand))):
        return 8*(10**20) + add_card_value(original_hand)
    #Full House: Three of a kind and a pair
    for char in set(hand):
        if (hand.count(char) == 3 - J_count):
            for other_char in set(set(hand) - {char}):
                if (hand.count(other_char) == 2):
                    return 7*(10**20) + add_card_value(original_hand)
    #Three cards of the same value
    if (any(hand.count(char) == 3 - J_count for char in set(hand))):
        return 6*(10**20) + add_card_value(original_hand)
    #Two pairs
    for char in set(hand):
        if (hand.count(char) == 2 - J_count):
            for other_char in set(set(hand) - {char}):
                if (hand.count(other_char) == 2):
                    return 5*(10**20) + add_card_value(original_hand)
    #One pair
    if (any(hand.count(char) == 2 - J_count for char in set(hand))):
        return 4*(10**20) + add_card_value(original_hand)
    return add_card_value(original_hand)

def add_card_value(hand):
    char_value = {"A": "14","K": "13","Q": "12","J": "01","T": "10","9": "09","8": "08","7": "07","6": "06","5": "05","4": "04","3": "03","2": "02"}
    value_list = [char_value[card] for card in hand]
    return int(''.join(map(str, value_list)))


"""
def compare_hands(hand1, hand2):
    char_value = {"A": 14,"K": 13,"Q": 12,"J": 11,"T": 10,"9": 9,"8": 8,"7": 7,"6": 6,"5": 5,"4": 4,"3": 3,"2": 2}

    if (evalute_hand(hand1) > evalute_hand(hand2)):
        return 1
    if (evalute_hand(hand1) < evalute_hand(hand2)):
        return -1
    for card_1, card_2 in zip(hand1, hand2):
        if (char_value[card_1] > char_value[card_2]):
            return 1
        if (char_value[card_1] < char_value[card_2]):
            return -1
    return 0
"""

#compare_hands("KK677","KTJJT")

data = sorted(data, key=lambda x: evalute_hand(x[0]))
print(data)
score = 0
for idx, _hand in enumerate(data):
    print(_hand, idx+1)
    score += (idx+1)*_hand[1]

print(score)
puzzle.answer_b = score