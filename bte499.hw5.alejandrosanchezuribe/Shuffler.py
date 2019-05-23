# Author: Alejandro Sanchez Uribe
# Class: BTE 499
# Date: 22 March 2019
# Assignment: Assignment 5

import Deck
import random


def simple_shuffle(deck):
    stack1, stack2 = Deck.Deck(), Deck.Deck()

    for i in range(deck.size()//2):
        stack1.push(deck.top())
        deck.pop()

    for i in range(deck.size()):
        stack2.push(deck.top())
        deck.pop()

    for i in range(stack1.size() + stack2.size()):
        if i % 2 == 0:
            deck.push(stack2.top())
            stack2.pop()
        else:
            deck.push(stack1.top())
            stack1.pop()


def fisher_yates_shuffle(deck):
    temp_deck = []

    initial_size = deck.size()

    for i in range(initial_size - 1):
        node_picked = random.randint(0, deck.size()-1)
        temp_deck.append(deck.getInnerNode(node_picked))
        deck.deleteInnerNode(node_picked)

    for card in temp_deck:
        deck.push(card)
