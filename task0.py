import random
my_string = input("Введіть слово")
lenght_words = 4
num_words = 5
while num_words > 0:
    num_words -= 1
    copy_my_string = my_string
    word = ''
    while len(word) < lenght_words:
        index = random.randint(0,len(my_string))