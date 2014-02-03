#18. An anagram is a word formed by rearranging the letters of another word, e.g., iceman is an anagram of cinema. We're going to write a method called anagrams_for that takes as its input a word and an array of words, representing a dictionary, and returns an array consisting of all the anagrams of the input word. anagrams_for should return an empty array ([]) if no anagrams are found in the dictionary. You don't have to worry about the order of the returned Array.

array = ["icetea","iceman","icecream"]
word = "cinema"

def anagrams_for(word, array):
    dic = {}
    for i in array:
        if len(i) == len(word):
            list_i = i.split()
            list_i.sort()
            sorted_i = "".join(list_i)
            dic[sorted_i].append(i)
            word = word.split()
            list_word = word.sort()
            sorted_word = "".join(list_word)
            result = dic.get(sorted_word)
            if result != None:
                return result
            else:
                return []
        return False

def anagrams_for2(word, array):
    word_d = list(word)
    sorted_word = word_d.sort()
    print word_d
    print sorted_word




print anagrams_for2(word, array)




