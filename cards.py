from random import shuffle
card = [
    {'value':2, 'suit':'Diamond'},
    {'value':3, 'suit':'Diamond'},
    {'value':4, 'suit':'Diamond'},
    {'value':5, 'suit':'Diamond'},
    {'value':6, 'suit':'Diamond'},
    {'value':7, 'suit':'Diamond'},
    {'value':8, 'suit':'Diamond'},
        {'value':9, 'suit':'Diamond'},
        {'value':10, 'suit':'Diamond'},
        {'value':'J', 'suit':'Diamond'},
        {'value':'Q', 'suit':'Diamond'},
        {'value':'K', 'suit':'Diamond'},
        {'value':'A', 'suit':'Diamond'},
        {'value':2, 'suit':'Heart'},
        {'value':3, 'suit':'Heart'},
        {'value':4, 'suit':'Heart'},
        {'value':5, 'suit':'Heart'},
        {'value':6, 'suit':'Heart'},
        {'value':7, 'suit':'Heart'},
        {'value':8, 'suit':'Heart'},
        {'value':9, 'suit':'Heart'},
        {'value':10, 'suit':'Heart'},
        {'value':'J', 'suit':'Heart'},
        {'value':'Q', 'suit':'Heart'},
        {'value':'K', 'suit':'Heart'},
        {'value':'A', 'suit':'Heart'},
        {'value':2, 'suit':'Spade'},
        {'value':3, 'suit':'Spade'},
        {'value':4, 'suit':'Spade'},
        {'value':5, 'suit':'Spade'},
        {'value':6, 'suit':'Spade'},
        {'value':7, 'suit':'Spade'},
        {'value':8, 'suit':'Spade'},
        {'value':9, 'suit':'Spade'},
        {'value':10, 'suit':'Spade'},
        {'value':'J', 'suit':'Spade'},
        {'value':'Q', 'suit':'Spade'},
        {'value':'K', 'suit':'Spade'},
        {'value':'A', 'suit':'Spade'},
        {'value':2, 'suit':'Club'},
        {'value':3, 'suit':'Club'},
        {'value':4, 'suit':'Club'},
        {'value':5, 'suit':'Club'},
        {'value':6, 'suit':'Club'},
        {'value':7, 'suit':'Club'},
        {'value':8, 'suit':'Club'},
        {'value':9, 'suit':'Club'},
        {'value':10, 'suit':'Club'},
        {'value':'J', 'suit':'Club'},
        {'value':'Q', 'suit':'Club'},
        {'value':'K', 'suit':'Club'},
        {'value':'A', 'suit':'Club'}
    ]



class Card():

    def __init__(self):
        shuffle(card)
        self.card = card.pop()


    def __repr__(self):
        print(f"{self.card['value']} of {self.card['suit']}")



a_card = Card()
another_card = Card()
a_card.__repr__()
another_card.__repr__()