import random
import itertools


def dice_roller(m, d, a):

    sides = 0
    for _ in itertools.repeat(d, m):
        side = random.randint(1, d)
        sides += side
    roll = str(m) + "d" + str(d) + "+" + str(a)
    value = sides + a
    print('rzucasz', roll, 'otrzymujesz', value)
    return value


times = int(input('Ile rzutów? '))
roll_set = {}

while times > 0:
    roll = input('\nNazwa rzutu: ')
    m = int(input('Ile kostek? '))
    d = int(input('Typ kostki? '))
    a = int(input('Do wyniku dodaj '))
    roll_set[roll] = dice_roller(m, d, a)
    times -= 1
