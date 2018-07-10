# -*- coding: UTF-8 -*-

from nltk.tag import StanfordPOSTagger
import os

#you can get English Tag and Chinese Tag from [GetTag.py] and just paste that below
#you can get Chinese Word and English Word from [GetWord.py] and just paste that below

EngTag = []
ChnTag = []
ChnWord = []
EngWord = []

os.environ["JAVA_HOME"] = "C:\Program Files\Java\jre1.8.0_171" 
os.environ["CLASSPATH"] = "D:\StanfordNLP\jars"
os.environ["STANFORD_MODELS"] = "D:\StanfordNLP\models"

eng_tagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')
chn_tagger = StanfordPOSTagger('chinese-distsim.tagger')

with open (r"F:\AllTag\chn_eng_train.zh.txt","r",encoding="utf-8_sig") as ChnReader,open (r"F:\AllTag\chn_eng_train.en.txt","r",encoding="utf-8_sig") as EngReader,\
     open (r"F:\AllTag\tage_tagc_train.tagc.txt","w",encoding="utf-8_sig") as ChnWriter,open (r"F:\AllTag\tage_tagc_train.tage.txt","w",encoding="utf-8_sig") as EngWriter :
     for index,line in enumerate(ChnReader):
          Temp = []
          list1 = chn_tagger.tag(line.split())
          print(index)
          print(line)
          for _, word_and_tag in  list1:
               word, tag = word_and_tag.split('#')
               string = str(ChnTag.index(tag))+"@"+str(ChnWord.index(word))
               Temp.append(string)
          String = " ".join(Temp)
          ChnWriter.write(String+'\n')
     for index,line in enumerate(EngReader):
          Temp = []
          list1 = eng_tagger.tag(line.split())
          print(index)
          print(line)
          for sets in  list1:
               if sets[0]==',' or sets[0]==':' or sets[0]=='(' or sets[0]==')' or sets[0]=='/' or sets[0]=='-':
                    string = str(EngTag.index('PU'))+"@"+str(EngWord.index(sets[0]))
               else:
                    string = str(EngTag.index(sets[1]))+"@"+str(EngWord.index(sets[0]))
               Temp.append(string)
          String = " ".join(Temp)
          EngWriter.write(String+'\n')
        
