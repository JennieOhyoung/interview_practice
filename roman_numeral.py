"""
Write a method that converts an integer to its Roman numeral equivalent, i.e., 476 => CD LXX VI. For reference, these are the building blocks for how we encode numbers with Roman numerals: 
I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000 Choose Between Old-school Roman numerals (no subtraction of 4s and 9s) 4 = IIII, 9 = VIIII etc. 
Modern Roman numerals (subtraction) 4 = IV, 9 = IX, 14 = XIV, 40 = XL, 44 = XLIV, 90 = XC, 944 = CMXLIV
"""


# def roman_numeral(num):
#     rn = []
#     int_str = str(num)
#     lookup =[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
#     final = ""

#     for i in range(len(int_str)):
#         place = (10**(len(int_str)-1-i)) #100
#         rn.append(num//place*place) #200
#         num = num - int(rn[i]) # 12
    
#     for i, val in enumerate(rn):
#         final += helper(val)

#     return final

lookup=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]



def int_to_roman(num):
    result=''

    for value in lookup:
        while num - value[1]>=0:
            num -= value[1]
            result += value[0]
    return result

print int_to_roman(212)



def roman_to_int(string):
    result = 0

    for pair in lookup:
        continueyes=True
        while continueyes:
            if len(string) >= len(pair[0]):
                if string[0:len(pair[0])]==pair[0]:
                    result += pair[1]
                    string = string[len(pair[0]):]

                else: continueyes=False
            else: continueyes=False
    return result 

print roman_to_int("CCXII")







