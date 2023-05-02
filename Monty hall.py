import random

listchoice = [1,2,3]
win_ds = []
win_s = []

for i in range(100001):
    random_win = random.choice(listchoice)
    random_choose = random.choice(listchoice)
    if random_win == random_choose:
        win_ds.append("win")

for i in range(100001):
    random_win = random.choice(listchoice)
    random_choose = random.choice(listchoice)
    newlist = [x for x in listchoice if x != random_win and x != random_choose]
    if len(newlist) == 1:
        win_s.append("win")

Dontswitch = (len(win_ds)/100000)*100
Switch = (len(win_s)/100000)*100

print(f"{Dontswitch} % chance of winning the game when you don't switch")
print(f"{Switch} % chance of winning the game when you switch")
