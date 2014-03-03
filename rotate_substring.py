


#1.8 Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings s1 s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring ( waterbottle is rotation of erbottlewat)

s1 = "waterbottle"
s2 = "bottlewater"

def is_substring(s1, s2):
    return s1.find(s2) > -1

def rotatedStringHasSubstring(s1,s2):
    #doubling the string ensures a complete substring regardless of rotation
    if len(s2)!=len(s1):
        return False
    doubles1 = 2*(s1)
    return is_substring(doubles1,s2)

# print is_substring(s1,s2)
# print rotatedStringHasSubstring(s1, s2)
