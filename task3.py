# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings
# from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
# that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)

# Поєднання слів
# Створіть програму, яка зчитує вхідний рядок, а потім створює та друкує 5 випадкових рядків із символів вхідного рядка.
# Наприклад, програма отримала слово "привіт", тому вона повинна надрукувати 5 випадкових рядків (слів),
# які поєднують символи "h", "e", "l", "l", "o" -> "hlelo", «олель», «лоле»…
# Поради: використовуйте модуль random, щоб отримати випадковий символ із рядка)
import random


user_word = "hello"
count_words = 5
new_word = []
while count_words > 0:
    count_words -= 1
    user_word_in_list = list(user_word)
    while len(user_word_in_list) > 0:
        index = random.randint(0, len(user_word_in_list)-1)
        char = user_word_in_list.pop(index)
        new_word.append(char)
    print(new_word)
    new_word.clear()
