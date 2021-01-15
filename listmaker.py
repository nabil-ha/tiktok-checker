from random import choice

usersCount = input('how many users?\n')
lettersCount = input('how many letters?\n')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


for i in range(int(usersCount)):
    user = ''
    for i in range(int(lettersCount)):
        user = user + choice(letters)
    print(user)
