class Card:
    strToInt = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 1}
    for i in range(2, 10):
        strToInt[str(i)] = i
    intToStr = {10: 'T', 11: 'J', 12 : 'Q', 13: 'K', 1: 'A'}
    for i in range(2, 10):
        intToStr[i] = str(i)

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = Card.strToInt[rank]

    def __str__(self):
        return f"{self.suit}{Card.intToStr[self.rank]}"
    
    def isLess(self, temp):
        return self.rank == temp.rank-1
    
    def isGreater(self, temp):
        return self.rank == temp.rank+1
    
class cardsOnTable:
    def __init__(self, cardList):
        self.LSCard = Card(cardList[0][0], cardList[0][1])
        self.USCard = Card(cardList[0][3], cardList[0][4])
        self.LHCard = Card(cardList[1][0], cardList[1][1])
        self.UHCard = Card(cardList[1][3], cardList[1][4])
        self.LDCard = Card(cardList[2][0], cardList[2][1])
        self.UDCard = Card(cardList[2][3], cardList[2][4])
        self.LCCard = Card(cardList[3][0], cardList[3][1])
        self.UCCard = Card(cardList[3][3], cardList[3][4])

    def TryPlay(self, card):
        if card.suit == 'S':
            if card.isLess(self.LSCard):
                print(f"{self.LSCard},L")
                return
            elif card.isGreater(self.USCard):
                print(f"{self.USCard},U")
                return
        elif card.suit == 'H':
            if card.isLess(self.LHCard):
                print(f"{self.LHCard},L")
                return
            elif card.isGreater(self.UHCard):
                print(f"{self.UHCard},U")
                return
        elif card.suit == 'C':
            if card.isLess(self.LCCard):
                print(f"{self.LCCard},L")
                return
            elif card.isGreater(self.UCCard):
                print(f"{self.UCCard},U")
                return
        elif card.suit == 'D':
            if card.isLess(self.LDCard):
                print(f"{self.LDCard},L")
                return
            elif card.isGreater(self.UDCard):
                print(f"{self.UDCard},U")
                return
            
        print('0')
        return


temp = input()
cardList = temp.split(';')

player = Card(cardList[0][0] , cardList[0][1])
cardList.pop(0)

CardOnTable = cardsOnTable(cardList)

CardOnTable.TryPlay(player)