# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

# Програма привітання з днем народження.
# Напишіть програму, яка бере ваше ім'я як вхідні дані, а потім ваш вік як вхідні дані і вітає вас таким:
# «Привіт, <ім’я>, у твій наступний день народження тобі буде <вік+1> рік»
name = input('Enter your name: ')
age = int(input('Enter your age: '))
print("Hello {0}, on your next birthday you’ll be {1} years".format(name, age+1))
