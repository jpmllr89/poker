

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def discard():
        return hand.pop()
    
    def draw_card(card):
        hand.append(card)
        return hand

    def show_hand():
        for i in hand:
            print(i)
        return hand