
#1.5 Implement a method to perform basic string compression using counts of repeated characters. aabcccccaaa => a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string.
s1 = "aaabbcccaa"
s2 = "abcdefg"

def compression(s):
    last = ''
    count = 0
    l = []

    for i in s:
        if i == last:
            count += 1
        else:
            if last != '':
                l.append(last + str(count))
            count = 1
        last = i

    l.append(last + str(count))
    l = "".join(l)
    if len(l) < len(s):
        return l
    else:
        return s

# print compression(s1)
# print compression(s2)

# counts all repeats in string
def repeats(s):
    l = []
    for i in s:
        if i not in l:
            l.append(i)
            if s.count(i) != 1:
                l.append(str(s.count(i)))
    return ''.join(l)

# print repeats(s1)
# print repeats(s2)
