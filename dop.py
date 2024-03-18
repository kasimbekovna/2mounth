import random
import time


def bet(b, g):
    print("Пожалуйста подождите...")
    time.sleep(2)

    choice = random.randint(1, 31)
    if choice == b:
        print(choice)
        print('Поздравляю вы выиграли!')
        return g * 2
    else:
        print(choice)
        print(f'-{g}$')
        print('Попробуйте еще раз!')

        return 0