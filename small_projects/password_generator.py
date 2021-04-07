#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


random_foo = random.SystemRandom()
generated_password = []
password = ''

# for i in range(nr_letters):
#     for letter in random_foo.choice(letters):
#         generated_password.append(letter)
# for i in range(nr_symbols):
#     for symbol in random_foo.choice(symbols):
#         generated_password.append(symbol)
# for i in range(nr_numbers):
#     for number in random_foo.choice(numbers):
#         generated_password.append(number)
# for i in range(len(generated_password)):
#     password += random_foo.choice(generated_password)

for i in range(1, nr_letters + 1):
    generated_password.append(random.choice(letters))

for i in range(1, nr_symbols + 1):
    generated_password.append(random.choice(symbols))

for i in range(1, nr_numbers + 1):
    generated_password.append(random.choice(numbers))
print(generated_password)
random.shuffle(generated_password)
print(generated_password)

for i in range(len(generated_password)):
    password += random.choice(generated_password)

print(password)
