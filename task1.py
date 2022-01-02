# Гра у відгадки.
# Напишіть програму, яка генерує випадкове число від 1 до 10 і дозволяє користувачеві вгадати,
# яке число було згенеровано. Результат має бути надісланий назад користувачеві за допомогою оператора друку.
import random
pc_rand_num = random.randint(1, 10)
us_inp_num = int(input("Enter number from 1 to 10: "))
attempt = 0
while pc_rand_num == us_inp_num:
    attempt += 1
    us_inp_num = int(input("Enter number from 1 to 10: "))
    print("you didn't guess")

