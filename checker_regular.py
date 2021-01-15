import requests
import sys
from os import path, getcwd
from random import choice
from time import sleep

import datetime as dt
current_path = path.abspath(getcwd())
print('Contact on\nInstagram: @0nh2\nTwitter:@nh_ftw\n')


if path.isfile(f'{current_path}//usernames.txt'):
    pass
else:
    print('No file usernames.txt')
    sys.exit()

timeSleep = input('time sleep(default is 1): ')
if timeSleep == '':
    print('ok, default will be 1')
    sleep(0.4)
    timeSleep = 1
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
usersCounter = 0
availableNum = 0
takenNum = 0
timeOut = 7
availableUsers = list()
fileNum = 1
while path.isfile(f'{current_path}//Available Users {fileNum}.txt'):
    fileNum = fileNum + 1
proxyFileNum = 1


def getLines():
    theFile = f"{current_path}//usernames.txt"
    with open(theFile, 'r') as f:
        usersList = list()
        for user in f.readlines():
            usersList.append(user.strip('\n'))
        return usersList


usersList = getLines()
usersLen = len(usersList)


def saveAvailables(user):
    if path.isfile(f'{current_path}//Available Users {fileNum}.txt'):
        with open(f'Available Users {fileNum}.txt', 'r+') as f:
            if user not in f.read().splitlines():
                f.write(f'{user}\n')
            else:
                pass
            f.close()
    else:
        with open(f'Available Users {fileNum}.txt', 'a+') as f:
            f.write(f'{user}\n')
            f.close()


print(
    f'\n\nStart checking list of users\ntimesleep is set to:{timeSleep}\n')
for i in range(usersCounter, len(usersList)):
    username = usersList[i]
    sleep(float(timeSleep))
    if str(username).isdecimal():
        print(
            f'Warning! TikTok users can not be all numbers, like: {username} ')
        pass
    else:
        for attempt in range(3):
            try:
                url = f"https://www.tiktok.com/@{username}"
                headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "User-Agent": choice(user_agent_list),
                    "Connection": "close",
                    "Host": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Cache-Control": "max-age=0"
                }
                response = requests.get(url, headers=headers)

                
                if response.status_code==404:
                    print(f'{username} is available')
                    saveAvailables(user=username)
                    availableNum = availableNum + 1
                elif response.status_code == 200 or 204:
                    print(f'{username} is taken')
                    takenNum = takenNum + 1
                    
            except Exception as e:
                print(f'{username} got error\nretrying...')
            else:
                break
        else:
            print('Please Connect to the Internet!')
            try:
                usersCounter = usersCounter - 1
            except:
                pass
            break

        print(f'Done {i+1} out of {usersLen}')
        if i+1 == usersLen:
            print(f'Done, {availableNum} is available, {takenNum} is taken')

    usersCounter = usersCounter + 1
print('Done')
