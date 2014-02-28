
def str_to_num(string):
    int_list = []
    final_num = 0
    string_list = list(string)
    for char in string_list:
        if 48 <= ord(char) <= 57:
            int_list.append(ord(char)-48)
        else:
            return False
    for i in range(len(int_list)):
        value = int_list[-i-1]
        place = 10**i
        final_num += value*place
    return final_num


print str_to_num("89")