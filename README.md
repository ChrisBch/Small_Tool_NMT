# Small_Tool_NMT

Author: ChenHan Yuan (Chris Yuan)

this project includes some codes that may be useful for people who want to prepare corpus and train models in NMT.
********************************************************************************************************************
if you have any question about this project or want to do some interesting things with me, please contact with me :)

Email: 

chris.yuan.ece@gmail.com  
yuanchenhan.ece@qq.com (if you want to contact me immediately)
*********************************************************************************************************************

10-fold_crossValidation.py can  generate the number of rows of the input text randomly which are required for 10-fold cross-validation.

GetWord.py can extract all words from the input text without repeating.

GetTag.py can use Stanford Tagger to generate all POS in the input text without repeating

Word@Tag.py can number all words and tags and replace the sentences in the input text with the form "word@tag".(this program need the data which is generated from GetWord.py and GetTag.py).
