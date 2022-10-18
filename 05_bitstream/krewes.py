'''
Sebastian Ching, Yat Long Chan
SoftDev
K05 -- Random devo from .txt file
2022-09-28
time spent: 0.5 hour(s)
DISCO: 
- Map a key to a list if you want to store multiple values to a single key
- dictionary.keys() returns a dict_keys obj rather than a list
-
QCC:
- Why is the K05 named bitstream?
- How else can we parse krewes.txt?
'''
import random

krewes_list = open('krewes.txt','r') #open krewes.txt file
krewes_list = krewes_list.read().strip() #turn file obj to str and remove trailing/leading whitespaces
krewes_list = krewes_list.split('@@@') #split str into list of period$$$devo$$$ducky
krewes = {} #init dict

#txt file -> dictionary
for i in krewes_list:
    if len(i) != 0: #ignore last item
        tmp = i.split('$$$') #split each item into [period, devo, ducky]
        period = (int) (tmp[0]) #period always first item in list
        devo_duck_pair = (tmp[1], tmp[2]) #devo and duck in a tuple. Always 2nd and 3rd item 
        if period not in krewes:
            krewes[period] = [devo_duck_pair] #list with tuple in it
        else:
            krewes[period].append(devo_duck_pair)

#prints random devo name, period, and ducky, but also returns devo + duck tuple 
def choose_devo(d):
    period = random.choice(list(d)) #random period
    devo_duck_pair = select_devo_period(period, d) #random devo + ducky
    return'period ' + (str) (period) + ', devo ' + devo_duck_pair[0] + ', ducky ' + devo_duck_pair[1]

# select_devo_period goes through a specific period and finds a random devo
def select_devo_period(period, d):
    if period in list(d):
        return random.choice(d[period])
    return None




print(choose_devo(krewes))


