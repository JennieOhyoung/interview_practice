
#151  Given an array of strings containing three types of braces: round (), square [] and curly {} Your task is to write a function that checks whether the braces in each string are correctly matched prints 1 to standard output (stdout) if the braces in each string are matched and 0 if they're not (one result per line) Note that your function will receive the following arguments: expressions which is an array of strings containing braces. expressions: [ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ] => 0 1 1 1 0


expressions = [")(){}","[]({})","([])","{()[]}","([)]"]

# def check_braces(expressions):
#     for j in expressions:
#         for i in range(len(j)/2):
#             if j[i] == "[":
#                 if j[-1-i] != "]":
#                     pass
#             if j[i] == "(":
#                 if j[-1-i] != ")":
#                     pass
#             if j[i] == "{":
#                 if j[-1-i] != "}":
#                     pass
#             else:
#                 print 0
#     print 1

def check_braces(expressions):
    for j in expressions:
        if len(j)%2 != 0:
            print 0
        for i in range(len(j)):
            if j[i] == "[":
                if "]" not in j:
                    print 0 
                else:
                    print 1
                    break
            if j[i] == "(":
                if ")" not in j:
                    print 0
                else:
                    print 1
                    break
            if j[i] == "{":
                if "" not in j:
                    print 0
                else:
                    print 1
                    break
            if j[i] == "]":
                if "[" not in j:
                    print 0 
                else:
                    print 1
                    break
            if j[i] == ")":
                if "(" not in j:
                    print 0
                else:
                    print 1
                    break
            if j[i] == "}":
                if "{" not in j:
                    print 0
                else:
                    print 1
                    break
            # else:
            #     print 1
        # print 1
    

check_braces(expressions)


