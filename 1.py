
# 1. Write a function "rev_str" that takes string and reverse.
# 1b. Takes string of words, reverse order or words 

string = "christmas"

def reverse(string):
    l = list(string)
    temp = 0
    for i in range(len(l)/2):
        temp = l[-1-i]
        l[-1-i] = l[i]
        l[i] = temp
        print l
    "".join(l)
    return l

def reverse(string):
    txt = []
    for i in range(len(string)-1, -1, -1):
        # for i in range(-1,-len(string)-1, -1):
        txt.append(string[i])
    return ''.join(txt)

def reverse(string):
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]

def reverse(string):
    s = list(string)
    l = []
    for i in range(len(s)):
        l.append(s(-1-i))
    return l # this returns a list

# print reverse(string)

sentence = "she loves chocolate"

def rev_sen(sentence):
    sentence = sentence.split()
    l = []
    for i in range(len(sentence)):
        l.append(sentence[-1-i])
    print l #returns list

def rev_sen(sentence):
    sentence = sentence.split()
    l = []
    for i in range(len(sentence)-1, -1, -1):
        l.append(sentence[i])
    print l

# rev_sen(sentence)














