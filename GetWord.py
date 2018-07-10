# -*- coding: UTF-8 -*-
with open (r"F:\AllTag\chn_eng_train.zh.txt","r",encoding="utf-8_sig") as ChnReader,open (r"F:\AllTag\chn_eng_train.en.txt","r",encoding="utf-8_sig") as EngReader:
    ChnWord = []
    EngWord = []
    for index,line in enumerate(ChnReader):
        list1 = line.split()
        for word in list1:
            if word not in ChnWord:
                ChnWord.append(word)
    for index,line in enumerate(EngReader):
        list2 = line.split()
        for word in list2:
            if word not in EngWord:
                EngWord.append(word)
                
print(ChnWord)
print(EngWord)