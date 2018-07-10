# -*- coding: UTF-8 -*-

from nltk.tag import StanfordPOSTagger
import os

#you can chose your own environment path 
#e.g. os.environ["JAVA_HOME"] = "C:\Program Files\Java\jre1.8.0_171" 
#os.environ["CLASSPATH"] = "D:\StanfordNLP\jars"
#os.environ["STANFORD_MODELS"] = "D:\StanfordNLP\models"

os.environ["JAVA_HOME"] = "path to java" 
os.environ["CLASSPATH"] = "path to StanfordTools\jars"
os.environ["STANFORD_MODELS"] = "path to StanfordTools\models"

eng_tagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')
chn_tagger = StanfordPOSTagger('chinese-distsim.tagger')

#enter the path to your corpus that you want to tag
#e.g. r"F:\AllTag\chn_eng_train.zh.txt"
#r"F:\AllTag\chn_eng_train.en.txt"

with open (r"path to chinese corpus","r",encoding="utf-8_sig") as ChnReader,open (r"path to english corpus","r",encoding="utf-8_sig") as EngReader:
    ChnTag = []
    EngTag = []
    for index,line in enumerate(ChnReader):
        print(index)
        list1 = chn_tagger.tag(line.split())
        for _, word_and_tag in  list1:
            word, tag = word_and_tag.split('#')
            if tag not in ChnTag:
                ChnTag.append(tag)
    for index,line in enumerate(EngReader):
        print(index)
        list2 = eng_tagger.tag(line.split())
        for sets in  list1:
            if sets[0]==',' or sets[0]==':' or sets[0]=='(' or sets[0]==')' or sets[0]=='/' or sets[0]=='-':
                if "PU" not in EngTag:
                    EngTag.append("PU")
            else:
                if sets[1] not in EngTag:
                    EngTag.append(sets[1])
    print(ChnTag)
    print(EngTag)
