#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:42:09 2022

@author: alanngungi
"""

empty_deck = []
n = 5
for i in range(n):
    empty_deck.append(i+1)

print(f'Original deck:{empty_deck}')


def reverse_deck(deck, n=1):
    unaltered_deck = deck
    descending = sorted(unaltered_deck, reverse=True)
    ascending = sorted(unaltered_deck, reverse=False)
    if unaltered_deck == descending:
        reversed_deck = sorted(unaltered_deck, reverse=False)
    elif unaltered_deck == ascending:
        reversed_deck = sorted(unaltered_deck, reverse=True)
    if n == 1:
        return reversed_deck
    else:
        return reverse_deck(reverse_deck(deck, n-1))




def weave_deck(deck, n=1):
    deck_copy = deck
    split = len(deck_copy)/2
    odd = (len(deck_copy)+1)/2
    weave = []
    if split%2 == 0:
        deck_1 = deck[:(split-1)]
        deck_2 = deck[split:]
        for i in range(len(deck)):
            weave[i] = deck_1[i]
            weave[i+1] = deck_2[i]
    elif split%2 != 0:
        deck_1 = deck[:int(odd)]
        deck_2 = deck[int(odd):]
        for k in range(len(deck_2)):
            v = deck_1[k]
            v1 = deck_2[k]
            weave.append(v)
            weave.append(v1)
        weave.append(deck_1[len(deck_1)-1])

    if n == 1:
        return weave
    else:
        return weave_deck(weave_deck(deck, n-1))




def shuffle_deck(deck, order):
    for i in range(len(order)):
        if order[i] == 'w':
            shuffle_deck = weave_deck(deck)
        elif order[i]== 'r':
            shuffle_deck = reverse_deck(deck)
        
    return shuffle_deck



shuffled_deck = shuffle_deck(empty_deck, 'wr')
print(f'Shuffled deck:{shuffled_deck}')



