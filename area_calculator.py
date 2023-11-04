from math import pi
while True:
    figure = input("Задайте фигурата, на която искате да изчислите лицето.(квадрат/правоъгълник/кръг/триъгълник): ").lower()

    if figure == 'квадрат':
        first_digit = float(input("Колко е дълга страната? : "))
        sides = first_digit * first_digit
        print(f"Ето ви лицето на квадрата! : {sides: .3f}")

    elif figure == 'правоъгълник':
        first_digit = float(input("Колко е дълга първата страна? : "))
        second_digit = float(input("Колко е дълга втората страна? : "))
        sides = first_digit * second_digit
        print(f"Ето ви лицето на правоъгълника! : {sides: .3f}")
        break
    elif figure == 'кръг':
        first_digit = float(input("Какъв е радиуса на кръга? : "))
        sides = first_digit ** 2 * pi  # С 2 звездички степенуваме
        print(f"Ето ви и лицето на кръга! : {sides: .3f}")
        break
    elif figure == 'триъгълник':
        first_digit = float(input("Колко е дълга първата страна? : "))
        second_digit = float(input("Колко е дълга втората страна? : "))
        sides = (first_digit * second_digit) / 2
        print(f"Ето ви лицето на триъгълника! : {sides: .3f}")
        break
    else:
        print("Невалидна фигура. Моля, опитайте отново.")
