import sys

dealt = sys.stdin.readlines(1)[0] +" "

suits = {
    "Clubs" : list(dealt[dealt.find("C")+1:dealt.find("D")]),
    "Diamonds" : list(dealt[dealt.find("D")+1:dealt.find("H")]),
    "Hearts" : list(dealt[dealt.find("H")+1:dealt.find("S")]),
    "Spades" : list(dealt[dealt.find("S")+1:].strip())
}

print("Cards Dealt              Points")
total = 0
for suit, cards in suits.items():
    card = " ".join(cards)
    points = card.count("A")*4 + card.count("K")*3 + card.count("Q")*2 + card.count("J") + max(0, 3-len(cards))
    space = 29 - len(suit) - len(card)
    print(f"{suit} {card} {points:{space}}")
    total += points

print(f"{'Total ' + str(total):>31} ")
