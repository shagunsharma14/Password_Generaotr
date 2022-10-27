import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters=int(input("Enter the number of letters you want: "))
num_number=int(input("Enter the number of numbers you want: "))
num_symbols=int(input("Enter the number of symbols you want: "))

password=[]

for char in range(1,num_letters+1):
    password.append(random.choice(letters))
for char in range(1,num_number+1):
    password.append(random.choice(numbers))
for char in range(1,num_symbols+1):
    password.append(random.choice(symbols))

f_password=""
for char in password:
    f_password+=char

print(f"your password is : {f_password}")
    