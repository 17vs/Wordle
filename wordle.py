import random

word_list = ["maybe", "radio", "water", "three", "hello"]

f = open("wordle_5_letter_dictionary.txt", "r")
all_answers = f.read().split()
f.close()

def userInput():
    while True:
        try:
            user = (input("Enter your guess: ")).lower()
            if not(user in all_answers):
                raise ValueError
        except ValueError:
            print("Error, please enter a valid 5 letter word")
            continue
        return user

def chooseWord(l):
    index = 3 #random.randint(0, (len(l) - 1))
    word = l[index]
    return word

def letterCount(word):
    count = {}
    for s in word:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    return count

def letterIndex(word, count):
    ind = {}
    for i in word:
        if count[i] > 1:
            if i in ind.keys():
                ind[i].append(word.index(i, (ind[i][-1]+1)))
            else:
                ind[i] = [word.index(i)]
        else:
            ind[i] = word.index(i)
    return ind

def isMoreThanOne(count):
    more_than_one = []
    for key in count:
        if count[key] > 1:
            more_than_one.append(key)
    return more_than_one

def answerCompare(word, answer, count_word, count_answer):
    index_word = letterIndex(word, count_word)
    index_answer = letterIndex(answer, count_answer)
    more_than_one_word = isMoreThanOne(count_word)
    more_than_one_answer = isMoreThanOne(count_answer)
    
    color_code = {}
    
    for i in answer:
        counter = 0
        if i in word:
            if i in more_than_one_answer or i in more_than_one_word:
                if i in more_than_one_answer and i in more_than_one_word:
                    for x in index_answer[i]:
                        if x in index_word[i]:
                            color_code[x] = "green"
                        else:
                            color_code[x] = "yellow"
                elif i in more_than_one_answer:
                    for x in index_answer[i]:
                        if x == index_word[i]:
                            color_code[x] = "green"
                        elif counter == 0:
                            color_code[x] = "yellow"
                            counter += 1
                        else:
                            color_code[x] = "grey"
                    
                elif i in more_than_one_word:
                    if index_answer[i] in index_word[i]:
                        color_code[index_answer[i]] = "green"

                    else:
                        color_code[index_answer[i]] = "yellow"


                        
            else:
                if index_answer[i] == index_word[i]:
                    color_code[index_answer[i]] = "green"
                else:
                    color_code[index_answer[i]] = "yellow"
        else:
            color_code[index_answer[i]] = "grey"
    return color_code


word = chooseWord(word_list)
count_word = letterCount(word)
answer = userInput()
count_answer = letterCount(answer)

print("")
print("Guess: {}".format(answer))
final = [i for i in answerCompare(word, answer, count_word, count_answer).values()]
print(final)
print("")

while final != ["green" for i in range(5)]:
    answer = userInput()
    count_answer = letterCount(answer)
    print("Guess: {}".format(answer))
    final = [i for i in answerCompare(word, answer, count_word, count_answer).values()]
    print(final)
    print("")


print("Answer: {}".format(word))


# for key in count:
#   if count[key] > 1:
#     print("{}, {}".format(key, count[key]))
