from mierz_czas import mierz_czas
from random import randint


@mierz_czas
def testowa_funkcja(iter_num, divisor):
    for _ in range(0, iter_num):
        rand_num = randint(1, 100000)
        if rand_num % divisor == 0:
            print(f"{_}. {rand_num}")


testowa_funkcja(20000000, 47833)
