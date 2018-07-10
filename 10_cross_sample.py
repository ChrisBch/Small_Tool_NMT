from random import sample


#for i in range(1,11):
#    list2 = sample(list1,34)
#    list1 = list(set(list1)-set(list2))
#    TempList[i-1] = list2
TempList = [[142, 134, 235, 225, 37, 86, 293, 314, 291, 107, 311, 294, 304, 113, 210, 185, 79, 150, 156, 342, 315, 111, 44, 238, 9, 269, 36, 151, 125, 46, 282, 286, 206, 272], [17, 297, 40, 70, 329, 271, 343, 241, 332, 167, 91, 85, 97, 267, 66, 128, 131, 15, 147, 245, 183, 158, 51, 56, 122, 276, 296, 123, 61, 52, 119, 262, 161, 108], [320, 216, 260, 22, 190, 223, 146, 189, 249, 324, 250, 27, 71, 215, 92, 266, 32, 83, 333, 187, 180, 14, 10, 104, 174, 307, 339, 140, 11, 254, 84, 112, 72, 239], [248, 35, 62, 226, 75, 69, 94, 145, 141, 252, 175, 93, 152, 57, 330, 181, 163, 275, 244, 229, 247, 237, 0, 200, 89, 312, 232, 319, 251, 30, 124, 212, 341, 284], [188, 255, 64, 58, 336, 148, 334, 16, 4, 33, 199, 257, 59, 43, 13, 309, 65, 24, 100, 327, 182, 5, 34, 47, 38, 31, 117, 49, 214, 243, 60, 202, 98, 99], [193, 228, 114, 224, 110, 203, 133, 154, 45, 29, 155, 288, 310, 116, 264, 302, 77, 295, 308, 208, 25, 230, 337, 139, 171, 169, 240, 220, 231, 321, 306, 170, 178, 299], [172, 328, 300, 109, 292, 41, 236, 28, 322, 217, 42, 338, 48, 205, 153, 129, 74, 176, 6, 323, 102, 184, 340, 120, 194, 164, 177, 198, 68, 78, 67, 277, 258, 21], [23, 283, 305, 132, 287, 87, 1, 144, 157, 331, 136, 227, 233, 281, 7, 101, 137, 313, 222, 274, 317, 196, 166, 2, 213, 82, 80, 19, 219, 55, 3, 18, 279, 96], [326, 273, 259, 149, 253, 268, 179, 50, 160, 143, 53, 173, 8, 209, 197, 115, 73, 204, 316, 246, 195, 118, 81, 88, 234, 289, 270, 168, 211, 335, 130, 280, 303, 242], [127, 63, 106, 218, 126, 162, 95, 90, 26, 201, 221, 318, 325, 263, 39, 121, 159, 138, 298, 192, 290, 165, 105, 54, 301, 135, 103, 12, 265, 76, 20, 186, 207, 191]]
list1 = [x for x in range(0,344)]
ListDev= list(set(list1)-set(TempList[9]))
ListDev = sample(ListDev,30)

with open(r"F:\NoTag\chn_eng_train.en.txt","r",encoding="utf-8") as Reader1, open(r"F:\NoTag\10\chn_eng_test.en.txt","w",encoding="utf-8") as Writer1Test,\
     open(r"F:\NoTag\10\chn_eng_train.en.txt","w",encoding="utf-8") as Writer1Train,open(r"F:\NoTag\10\chn_eng_dev.en.txt","w",encoding="utf-8") as Writer1Dev,\
     open(r"F:\NoTag\10\chn_eng_test.zh.txt","w",encoding="utf-8") as Writer2Test,open(r"F:\NoTag\10\chn_eng_train.zh.txt","w",encoding="utf-8") as Writer2Train,\
     open(r"F:\NoTag\10\chn_eng_dev.zh.txt","w",encoding="utf-8") as Writer2Dev,open(r"F:\NoTag\chn_eng_train.zh.txt","r",encoding="utf-8") as Reader2:
    for index,line in enumerate(Reader1):
        if index in TempList[9]:
            Writer1Test.write(line)
        elif index in ListDev:
            Writer1Dev.write(line)
        Writer1Train.write(line)
    for index,line in enumerate(Reader2):
        if index in TempList[9]:
            Writer2Test.write(line)
        elif index in ListDev:
            Writer2Dev.write(line)
        Writer2Train.write(line)    




