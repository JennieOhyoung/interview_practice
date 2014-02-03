# 16.Write a method the takes in a string and returns the pig latin equivalent. Pig Latin takes the first consonant, moves it to the end of the word and places "ay" at the end. If the string starts with a vowel do nothing. 


def pig_latin():
    user_input = raw_input("What would you like to translate: ")
    input_list = user_input.split() # splits by space into input_list
    vowel = ["a", "e", "i", "o", "u"]
    translated = []
    if len(input_list) == 0:
        return "Nothing to interpret, goodbye!"
    else:
        for i in input_list:
            # if word is 1 letter long, append directly to list
            if len(i) == 1:
                translated.append(i)
            # if the first letter is a consonant, modify word according to rule
            if i[0] not in vowel:
                l = i[1:] + i[0] + "ay"
                translated.append(l)

    print " ".join(translated)


pig_latin()