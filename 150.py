# 150. write a function that determines for each pair if its an anagram or not for each pair of words your function will print to standard output (stdout) the value 1 if the pair is an anagram or 0 otherwise (one result per line) Note that your function will receive the following arguments: firstWords which is an array of strings giving the first word for each of the pairs secondWords which is an array of strings giving the corresponding second word

first_words = ["cinema","host","aba","train"]
second_words = ["iceman","shot","bab","rain"]

def check_anagrams(first_words, second_words):
    result = []
    for i in range(len(first_words)):
        # if len(str(first_words[i]) != len(str(second_words[i])):
        #     result.append(0)
        first_list = list(first_words[i])
        first_list.sort()
        second_list = list(second_words[i])
        second_list.sort()
        if first_list != second_list:
            result.append(0)
        else:
            result.append(1)
    return result


print check_anagrams(first_words, second_words)