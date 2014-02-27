
# Write a function that deletes an element in a linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = str(index.value)
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return " ".join(nodestore)

    def add(self, value):
        node = Node(value)
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
            cureent.next = node

    def insert(self, value, i):
        node = Node(value)
        position = 0
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                counter += 1
                if counter == i:
                    node.next = current.next
                    current.next = node

    def delete(self, value, i):
        node = Node(value)
        position = 0
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                counter += 1
                if counter == i-1: #remember off 1
                    node.next = current.next.next

def main():
    linkedlist = LinkedList()
    for x in range(1,101):
        linkedlist.add(x)
    print linkedlist

# if __name__ == '__main__':
#     main()

# Write a function that deletes every other element in a linked list.
# def delete_alternate(linkedlist):
#     if self.head != None:
#         node= self.head.next


# Write a function that reverses the bits in an integer.
def reverse_bits(num):
    binary = bin(num)[2:]
    # return binary[::-1]
    reverse_binary = []
    for i in range(len(binary)):
        reverse_binary.append(binary[-1-i])
    return ''.join(reverse_binary)

# print reverse_bits(35)


# Write a function that counts the number of one bits in an integer.

def bit_count(num):
    binary = bin(num)[2:]
    count = 0
    for i in binary:
        if i == "1":
            count += 1
    return count

# print bit_count(25)


# Write a function that reverses the characters in a string in-place.

"CANNOT BE SOLVED IN PYTHON! STRINGS ARE IMMUTABLE"

# Write a function that outputs the elements stored in a binary search tree.

# def traverse_bintree(tree):
#     to_visit = []
#     to_visit.append(tree)
#     while len(to_visit)> 0:
#         x = to_visit.pop()
#         if x.

# Write a function that determines if an element is stored in a binary search tree.


# Given an array of ints, sum up all the even numbers and print it. Then return true if any number in the array is evenly divisible by 7, false otherwise.

array = [1,2,3,4,5,6,7]
def sum_and_div(array):
    even_sum = 0
    div = False
    for i in array:
        if i%2 == 0:
            even_sum += i
        if i%7 == 0:
            div = True
    print even_sum
    return div

# print sum_and_div(array)

# Given a two words, write a function/method to determine if they are anagrams
w1 = "poodle"
w2 = "looped"
w3 = "hello"
w4 = "ellah"

def anagrams(word1, word2):
    word1_sorted = ''.join(sorted(word1))
    word2_sorted = ''.join(sorted(word2))
    if word1_sorted != word2_sorted:
        return False
    return True

# print anagrams(w1,w2)
# print anagrams(w3,w4)

# Given a singly linked list, split that into two lists one containing just the elements in odd position and another containing just the elements in even position. 


# Merge 2 sorted arrays without having duplicates.
l1 = sorted(list("helloworld"))
l2 = sorted(list("beautifulday"))
def merge_nondup(l1, l2):
    merge = set(l1+l2)
    return sorted(list(merge))

# print merge_nondup(l1, l2)

# Find all the possible permutations of a given string.
import itertools
string = "big"
def all_permutations(string):
    result = list(itertools.permutations(string))
    return result

print all_permutations(string)





