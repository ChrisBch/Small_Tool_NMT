#This simple code can output the words, sorted by the number of them, that are included in sentences.
#Train translation model from Vietnamese to English.

with open (r"Path to language sentences","r") as VNeseReader, \
     open (r"Path to language sentences","r") as EngReader, \
     open (r"Path to words","w") as WordWriter:
    WordDic = {}
    
#get words from one language sentences

    for index,lines in enumerate(VNeseReader):
        TempWordList1 = []
        for strings in lines:
            if strings==" " or strings=="\\":
                TempWord = "".join(TempWordList1)
                if TempWord in WordDic.keys():
                    WordDic[TempWord] = WordDic[TempWord] + 1
                else:
                    WordDic[TempWord] = 1
                TempWordList1 = []
            else:
                TempWordList1.append(strings)
                
#get words from another language sentences, as same as above

    for index,lines in enumerate(EngReader):
        TempWordList2 = []
        for strings in lines:
            if strings==" " or strings=="\\":
                TempWord = "".join(TempWordList2)
                if TempWord not in WordDic.keys():
                    WordDic[TempWord] = 1
                else:
                    WordDic[TempWord] = WordDic[TempWord] + 1
                TempWordList2 = []
            else:
                TempWordList2.append(strings)
                
#output the words with the number of them (Format: "character1:  number1")

    for word in sorted(WordDic.items(), key = lambda item:item[1], reverse=True):
        word = list(word)
        word[1] = str(word[1])
        WordWriter.write(str(":   ".join(word)))
        WordWriter.write("\n")
