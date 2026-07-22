class Card:
    strToInt = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 1}
    for i in range(2, 10):
        strToInt[str(i)] = i
    intToStr = {10: 'T', 11: 'J', 12: 'Q', 13: 'K', 1: 'A'}
    for i in range(2, 10):
        intToStr[i] = str(i)

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = Card.strToInt[rank]

    def __str__(self):
        return f"{self.suit}{Card.intToStr[self.rank]}"
    
    def isLess(self, temp):
        return self.rank == temp.rank - 1
    
    def isGreater(self, temp):
        return self.rank == temp.rank + 1


class cardsOnTable:
    def __init__(self, cardList):
        s_l, s_u = cardList[0].split(',')
        h_l, h_u = cardList[1].split(',')
        d_l, d_u = cardList[2].split(',')
        c_l, c_u = cardList[3].split(',')

        self.cards = {
            'S': {'L': Card(s_l[0], s_l[1]), 'U': Card(s_u[0], s_u[1])},
            'H': {'L': Card(h_l[0], h_l[1]), 'U': Card(h_u[0], h_u[1])},
            'D': {'L': Card(d_l[0], d_l[1]), 'U': Card(d_u[0], d_u[1])},
            'C': {'L': Card(c_l[0], c_l[1]), 'U': Card(c_u[0], c_u[1])},
        }

    def TryPlay(self, card):
        if card.isLess(self.cards[card.suit]['L']):
            self.cards[card.suit]['L'] = card
            return True
        elif card.isGreater(self.cards[card.suit]['U']):
            self.cards[card.suit]['U'] = card
            return True
        return False

    def __str__(self):
        pairs = []
        for s in ['S', 'H', 'D', 'C']:
            l_card = str(self.cards[s]['L'])
            u_card = str(self.cards[s]['U'])
            pairs.append(f"{l_card},{u_card}")
        return ";".join(pairs)


first_line = input().strip()
suit_pairs = first_line.split(';')
table = cardsOnTable(suit_pairs)

second_line = input().strip()
hand_cards = [Card(card[0], card[1]) for card in second_line.split(',')]

played_any = True
while played_any:
    played_any = False
    remaining_hand = []
    for card in hand_cards:
        if table.TryPlay(card):
            played_any = True
        else:
            remaining_hand.append(card)
    hand_cards = remaining_hand

print(table)