from random import sample

#You can use the following codes in comment lines to generate ten sets randomly 
#each set contains all lines' numbers that will be used as a test set.
#all sets are saved in TempList.

#for i in range(1,11):
#    list2 = sample(list1,34)
#    list1 = list(set(list1)-set(list2))
#    TempList[i-1] = list2

list1 = [x for x in range(0,344)]
#you need to change the number in Templist[] to get different sets that are saved in TempList
ListDev= list(set(list1)-set(TempList[9]))
ListDev = sample(ListDev,30)

#we will generate development set, train set and test set.
#the development set are generated randomly 
#Note that: the data in test set and development set are all in the train set

with open(r"path to corpus1","r",encoding="utf-8") as Reader1, open(r"path to test set 1","w",encoding="utf-8") as Writer1Test,\
     open(r"path to train set 1","w",encoding="utf-8") as Writer1Train,open(r"path to development set 1","w",encoding="utf-8") as Writer1Dev,\
     open(r"path to test set 2","w",encoding="utf-8") as Writer2Test,open(r"path to train set 2","w",encoding="utf-8") as Writer2Train,\
     open(r"path to development set 2","w",encoding="utf-8") as Writer2Dev,open(r"path to corpus2","r",encoding="utf-8") as Reader2:
    for index,line in enumerate(Reader1):
    #you need to change the number in Templist[] to get different sets that are saved in TempList
        if index in TempList[9]:
            Writer1Test.write(line)
        elif index in ListDev:
            Writer1Dev.write(line)
        Writer1Train.write(line)
    for index,line in enumerate(Reader2):
     #you need to change the number in Templist[] to get different sets that are saved in TempList
        if index in TempList[9]:
            Writer2Test.write(line)
        elif index in ListDev:
            Writer2Dev.write(line)
        Writer2Train.write(line)    




