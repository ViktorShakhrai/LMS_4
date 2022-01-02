import random
status = False
while status == False:
    x = random.randint(0, 30)
    wht_f = random.randint(0, 2)
    if wht_f == 0:
        print("y=2x+3", "\nx={0}\ny=?".format(x))
        y = 2 * x + 3
        user_y = str(input('Enter your answer'))
        if y == user_y:
            status = True
    elif wht_f == 1:
        print("y=3x+15", "\nx={0}\ny=?".format(x))
        y = 3 * x + 15
        user_y = str(input('Enter your answer'))
        if y == user_y:
            status = True
    print("y=x+7", "\nx={0}\ny=?".format(x))
y = x + 7
user_y = str(input('Enter your answer'))
if y == user_y:
    status = True





