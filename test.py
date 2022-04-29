import itertools


for dice in itertools.product(range(1, 7), repeat=2):
    print(sum(dice))

