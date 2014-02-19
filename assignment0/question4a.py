# Write a Python function that simulates this approach to the Look Away minigame, assuming that Luigi always 
# looks forward and that Mario, Wario, and Peach each randomly choose to look either forward, up, down, left, 
# or right with uniform probability. Your function should take a number of trials to run as input and return 
# the fraction of trials on which Luigi won. You will probably find the random module
# <http://docs.python.org/library/random.html> useful.

import random

def lookaway(trials):
  luigi_wins = 0.0 
  for num in range(int(trials)):
    string1 = []
    string2 = []
    string3 = []
    for num in range(5):
      string1.append(random.randint(1,5))
      string2.append(random.randint(1,5))
      string3.append(random.randint(1,5))
    random_int = random.randint(1,5)
    if random_int in string1:
      if random_int in string2:
        if random_int in string3:
          luigi_wins += 1.0
  return (luigi_wins/trials)

print lookaway(5.0) 