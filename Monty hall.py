import random

listchoice = [1,2,3]
win_ds = []
win_s = []

for i in range(1001):
    random_win = random.choice(listchoice)
    random_choose = random.choice(listchoice)
    if random_win == random_choose:
        win_ds.append("win")

for i in range(1001):
    random_win = random.choice(listchoice)
    random_choose = random.choice(listchoice)
    newlist = [x for x in listchoice if x != random_win and x != random_choose]
    if len(newlist) == 1:
        win_s.append("win")

print((len(win_ds)/1000)*100)
print((len(win_s)/1000)*100)
