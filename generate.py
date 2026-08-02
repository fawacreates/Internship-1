import random 
cards = ["Ace of Spades", "2 of Hearts", "3 of Diamonds", "4 of Clubs", "5 of Spades", "6 of Hearts", "7 of Diamonds", "8 of Clubs", "9 of Spades", "10 of Hearts", "Jack of Diamonds", "Queen of Clubs", "King of Spades"]
random.shuffle(cards)
for card in cards:
    print(card)
