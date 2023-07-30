from random import choice
import random

# coin = choice(['heads', 'tails'])
coin = random.choice(['heads', 'tails'])

print(coin)

number = random.randint(1, 10)
print(number)

cards = ['JAck', 'Queen', 'King']
random.shuffle(cards)
for card in cards:
    print(card)