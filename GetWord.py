#This simple code can extract words from text and output it in a specified directory
#Train translation model from Vietnamese to English.

with open (r"Path to sentences data","r") as VNeseReader, \
     open (r"Path to sentences data","r") as EngReader, \
     open (r"Path to word","w") as WordWriter:
    WordList = []

#get words from one language sentences

    for index,lines in enumerate(VNeseReader):
        TempWordList1 = []
        for strings in lines:
            if strings==" " or strings=="\\":
                TempWord = "".join(TempWordList1)
                if TempWord in WordList:
                    pass
                else:
                    WordList.append(TempWord)
                TempWordList1 = []
            else:
                TempWordList1.append(strings)
                    
 #get words from another language sentences, as same as above

    for index,lines in enumerate(EngReader):
        TempWordList2 = []
        for strings in lines:
            if strings==" " or strings=="\\":
                TempWord = "".join(TempWordList2)
                TempWordList2 = []
                if TempWord not in WordList:
                    WordList.append(TempWord)
            else:
                TempWordList2.append(strings)
                    
#output the words

    for word in WordList:
        WordWriter.write(word)
        WordWriter.write("\n")
