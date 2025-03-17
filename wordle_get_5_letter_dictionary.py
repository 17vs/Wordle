import pickle
from nltk.corpus import words
import os

def writeDict(wl):
    f = open("wordle_5_letter_dictionary.txt", "w")
    x = [i.lower() for i in wl if len(i) == 5]
    for i in x:
        f.write(i + "\n")
    f.close()

all_word_list = words.words()

file_path = "wordle_5_letter_dictionary.txt"
if os.stat(file_path).st_size == 0:
    writeDict(all_word_list)

else:
    f = open("wordle_5_letter_dictionary.txt", "w")
    f.close()
    writeDict(all_word_list)


def writeCom(wl):
    t = open("wordle_most_common_5_dictionary.txt", "w")
    x = [i.lower() for i in wl if len(i) == 5]
    for i in x:
        t.write(i + "\n")
    t.close()

c = open("commonWords.csv", "r")
common_word_list = c.read().split()
c.close()

file_path = "wordle_most_common_5_dictionary.txt"
if os.stat(file_path).st_size == 0:
    writeCom(common_word_list)

else:
    t = open("wordle_most_common_5_dictionary.txt", "w")
    t.close()
    writeCom(common_word_list)



# import pickle
# from nltk.corpus import words
# import os

# def writeDict(wl):
#     f = open("wordle_5_letter_dictionary.txt", "wb")
#     x = [i.lower() for i in wl if len(i) == 5]
#     pickle.dump(x, f)
#     f.close()

# all_word_list = words.words()

# file_path = "wordle_5_letter_dictionary.txt"
# if os.stat(file_path).st_size == 0:
#     writeDict(all_word_list)

# else:
#     f = open("wordle_5_letter_dictionary.txt", "wb")
#     f.close()
#     writeDict(all_word_list)


# def writeCom(wl):
#     t = open("wordle_most_common_5_dictionary.txt", "wb")
#     x = [i.lower() for i in wl if len(i) == 5]
#     pickle.dump(x, t)
#     t.close()

# c = open("commonWords.csv", "r")
# common_word_list = c.read().split()
# c.close()

# file_path = "wordle_most_common_5_dictionary.txt"
# if os.stat(file_path).st_size == 0:
#     writeCom(common_word_list)

# else:
#     t = open("wordle_most_common_5_dictionary.txt", "wb")
#     t.close()
#     writeCom(common_word_list)



