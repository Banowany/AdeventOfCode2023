class Card:
    def __init__(self, label) -> None:
            self.strength = 0
            match label:
                case 'A':
                    self.strength = 13
                case 'K':
                    self.strength = 12
                case 'Q':
                    self.strength = 11
                case 'J':
                    self.strength = 10
                case 'T':
                    self.strength = 9
                case '9':
                    self.strength = 8
                case '8':
                    self.strength = 7
                case '7':
                    self.strength = 6
                case '6':
                    self.strength = 5
                case '5':
                    self.strength = 4
                case '4':
                    self.strength = 3
                case '3':
                    self.strength = 2
                case '2':
                    self.strength = 1

class Hand:
    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = bid
        sorted_cards = sorted(cards, key=lambda x: x.strength)
        count_list = []
        count = 1
        counting_card = sorted_cards[0]
        for card in sorted_cards[1:]:
            if counting_card.strength == card.strength:
                count += 1
            else:
                counting_card = card
                count_list.append(count)
                count = 1
        count_list.append(count)

        count_list.sort()
        if count_list == [5]:
            self.type = 7
        elif count_list == [1, 4]:
            self.type = 6
        elif count_list == [2, 3]:
            self.type = 5
        elif count_list == [1, 1, 3]:
            self.type = 4
        elif count_list == [1, 2, 2]:
            self.type = 3
        elif count_list == [1, 1, 1, 2]:
            self.type = 2
        else:
            self.type = 1
            
def hand_sort_key(hand):
    return (hand.type, hand.cards[0].strength, hand.cards[1].strength, hand.cards[2].strength, hand.cards[3].strength, hand.cards[4].strength)

with open('Day07/input.in', 'r') as file:
    lines = file.read().splitlines()

hands = []
for line in lines:
    hand_and_dip_as_string = line.split()
    cards = [Card(x) for x in hand_and_dip_as_string[0]]
    bid = int(hand_and_dip_as_string[1])
    hand = Hand(cards, bid)
    hands.append(hand)

hands.sort(key=hand_sort_key)

result = 0
for i, v in enumerate(hands):
    result += (i+1)*v.bid
print(result)