interview_practice
==================

Question pool:

Hackbright questions

1. Write a function "rev_str" that takes string and reverse. (not possible in place?)
1b. Takes string of words, reverse order or words 


2. Take a number n, return a list of fibbonacci numbers up to n. 
    value -> index
2b. index -> value

3. Given a number, return its factorial value. Do it recursively and nonrecursively

4. Given 2 lists of values of any kind, return list that contains all common values

5. 
5b. Given a class Linked_list(), define a method that adds a new node to the end of a linked list. Assume there are no loops in the list

6. Given a class Linked_list(), inserting node at position after i
6b. delete a node
6c. print as list

7. Define a method on linked list return True if list is circular.

8. Write function that takes one number and two lists, find if two items from the lists can add up to that number. Three items? 

9. write a function that does dfs, print out nodes in order

10. write a function that takes in two nodes, return first common ancestry

11. given a list of numbers from 1 to n randomly placed, there is one missing number. find the missing number without sort and with O(n)

12. 2 classes necessary to build a tree and all the attributes

13. Traverse through a binary tree and print out pre, in and post order

14. Reverse a linked list


Women who code questions

15. Write a method that converts an integer to its Roman numeral equivalent, i.e., 476 => 'CDLXXVI'. For reference, these are the building blocks for how we encode numbers with Roman numerals: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000 Choose Between Old-school Roman numerals (no subtraction of 4s and 9s) 4 = IIII, 9 = VIIII etc. Modern Roman numerals (subtraction) 4 = IV, 9 = IX, 14 = XIV, 40 = XL, 44 = XLIV, 90 = XC, 944 = CMXLIV

16.Write a method the takes in a string and returns the pig latin equivalent. Pig Latin takes the first consonant, moves it to the end of the word and places “ay” at the end. If the string starts with a consonant do nothing. “pig” = “igpay”, “banana” = “ananabay”

17.Without using a shuffle or sort write your own shuffle method for an array. The method will take an array and returns a new array with all of the elements in a random order. One important property of a good shuffle method is that every permutation is equally likely.

18. An anagram is a word formed by rearranging the letters of another word, e.g., iceman is an anagram of cinema. We're going to write a method called anagrams_for that takes as its input a word and an array of words, representing a dictionary, and returns an array consisting of all the anagrams of the input word. anagrams_for should return an empty array ([]) if no anagrams are found in the dictionary. You don't have to worry about the order of the returned Array.

19. Write a recursive and iterative solution for a finding the factorial of a number. If you don't remember, the factorial of a non-negative integer n, denoted n! is the product of all positive integers less than . For example, 5! = 5 * 4 * 3 * 2 * 1

20.Write an example demonstrating Binary Search. Write an example demonstrating Linear Search. Hint: A linear search looks down a list, one item at a time, without jumping. In complexity terms this is an O(n) search - the time taken to search the list gets bigger at the same rate as the list does. A binary search is when you start with the middle of a sorted list, and see whether that's greater than or less than the value you're looking for, which determines whether the value is in the first or second half of the list.

21. Implement an iterative version of the Fibonacci sequence which take an integer n as input and returns the nth Fibonacci number. Implement a recursive version of the Fibonacci sequence which take an integer n as input and returns the nth Fibonacci number. In mathematics, the Fibonacci numbers or Fibonacci series or Fibonacci sequence are the numbers in the following integer sequence:[1][2] 0,1,1,2,3,5,8,13,21,34,55,89,144 By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation F_n = F_{n-1} + F_{n-2}

22.I have an array stockPricesYesterday where the keys are the number of minutes into the day (starting with midnight) and the values are the price of Apple stock at that time. For example, the stock cost $500 at 1am, so stockPricesYesterday[60] = 500. 
Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of an Apple stock yesterday.

23.Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

24.Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)

25. Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not. Write the test cases for this method.
Write a method to decide if two strings are anagrams or not.

26.Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node. EXAMPLE Input: the node ‘c’ from the linked list a->b->c->d->e Result: nothing is returned, but the new linked list looks like a->b->d->e

27. You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1’s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. EXAMPLE Input: (3 -> 1 -> 5) + (5 -> 9 -> 2) Output: 8 -> 0 -> 8

28.Given a circular linked list, implement an algorithm which returns node at the beginning of the loop. Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list. EXAMPLE input: A -> B -> C -> D -> E -> C [the same C as earlier] output: C

29. Given two different lists of objects, come up with an efficient solution to find the intersection of the two lists.

30.Implement a function to check if a tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.

31.Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

32. Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.

33. Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (i.e., if you have a tree with depth D, you’ll have D linked lists).

34.In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (e.g., each disk sits on top of an even larger one). You have the following constraints: (A) Only one disk can be moved at a time. (B) A disk is slid off the top of one rod onto the next rod. (C) A disk can only be placed on top of a larger disk.


35.Write a program to move the disks from the first rod to the last using Stacks.

36. Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.

Christine's questions

37.Given a list of elements, write a function to determine whether some element k is in the list.

38. Once you have your first solution, try going about it another way. Aim for three different ways to solve this question, and think to yourself about what the pros and cons are of each. -> Come up with two different solutions. One should assume that speed is the priority; the other should assume that minimal storage is the priority.

39. Implement division without using the / division operator.
-> This seems like a really simple question at first, but leaves you open to lots of questions and things to watch out for. This is a good example of "watch out for edge cases and boundary conditions" -- if you wrote a naive solution to this, how could a malicious programmer crash your program?

Ketaki's questions

40. find max number of repetitions in an array.like {2,3,4,5,2,3,2} max repeat is 2. optimize it for space then in time.

41. Write a function that accepts two or more strings and returns the longest common substring in all of them.

42.Design an Class Structure for a Car


43. Design a OO system for furniture where there are wooden chairs and tables, metal chairs and tables. There are stress and fire tests for each products.

Week 2 questions

44. Sort. select or bubble (stupid), merge(best) (cant be done in place), quick (edge cases) 

45.Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas

46. Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates

47.Given the string s, split it into two strings, s2 and s3, s2 containing 
the first 5 letters of the string, and s3 containing the remaining letters.

48.Given the string s, excise characters 6 through 12, inclusive

49.Given the string s, produce a list composed of all the 
single characters from the original string

50.Given the list l composed of tuples, sort the list by the second item in the tuple l = [(1,3), (3,2), (5,1)] becomes l = [(5,1), (3,2), (1,3)]

51. Given 2 dictionaries, d1 and d2, update the contents of d1 with the contents of d2, overwriting any existing keys

52. Given two dictionaries, d1 and d2, merge the contents of d1 with the contents of d2, adding to the values of existing keys

53. Given a multiline string 's', print each line along with the line number

54. Write a function with the following signature:
    title(str) -> str 
    It should take a string and capitalize it according to book title rules

55. Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

Ouya progaramming test:

56.Write a function LongestRun that returns the length of the longest run of consecutive identical values in an integer array of unknown length. 

public static int LongestRun(int[] values)

LongestRun(new int[] {1,5,5,5,4,3,3}) should return 3
LongestRun(new int[] {}) should return 0
LongestRun(new int[] {2,8,8,7,2,2,2,2}) should return 4

57.Write a function CrazySort that takes an array of strings as input, and prints the strings to standard out, sorted by the following rules:
- ignore words beginning with #, and do not print them to standard out
- sort the remaining words in order of increasing length (shortest words first)
- for words of the same length, sort them in alphabetical order but going from right-to-left (so "CBA" would come before "ABC")

public static void CrazySort(String[] values)

CrazySort(new String[] {"#comment", "ouya", "foo", "bar", "help"}) should print:
foo
bar
ouya
help

58. A DNA strand may be described as a variable-length array, where each element has one of four possible values: G, C, A, or T.

3a. Write a class DNAStrand that represents a strand of DNA. The class should have a constructor that initializes a DNAStrand from a string, and a toString() function that returns the DNAStrand as a string. Show the implementations of the constructor and toString().

public class DNAStrand 
{
    DNAStrand(String s) { // implement me }
    public String toString() { // implement me }
}

59. Write a function IsComplementary that takes two DNAStrands as input, and returns true if N consecutive elements beginning at index x1 of DNAStrand s1 are complementary to N consecutive elements beginning at index x2 of DNAStrand s2, where "complementary" elements are defined as:
- G is complementary to C
- C is complementary to G
- A is complementary to T
- T is complementary to A  

public static boolean IsComplementary(DNAStrand s1, int x1, DNAStrand s2, int x2, int n)

DNAStrand.IsComplementary(new DNAStrand("GTTACA"), 3, new DNAStrand("TGTCGAGG"), 0, 3) should return true
because the sequence "ACA" at index 3 of s1 is complementary to the sequence "TGT" at index 0 of s2.

60. Write a function CanBond that takes two DNAStrands as input, and returns true if the strands can be overlapped such that all the overlapping elements are complementary and the size of the overlap region is three or greater. For example:
 
CanBond should return true (end-to-end bond):
GTTACA
   TGTCGAGG

CanBond should return true (center bond):
   GTTACA
TGTCAATGTCC

CanBond should return false - complementary overlap region size is less than 3:
GTTACA
    GTCGAGGT

CanBond should return false - no complementary overlap region:
GTTACA
      GAGCGAA


Technical/Logic questions

61. Problem: you have two jars, 50 red marbles, 50 blue marbles. you need to place all the marbles into the jars such that when you blindly pick one marble out of one jar, you maximize the chances that it will be red. (when picking, you’ll first randomly pick a jar, and then randomly pick a marble out of that jar) you can arrange the marbles however you like, but each marble must be in a jar.

62. You have three jars that are all mislabeled. one contains peanut butter jelly beans, another grape jelly jelly beans, and the third has a mix of both (not necessarily a 50/50 mix, could be a 1/99 mix or a 399/22 mix). how many jelly beans would you have to pull out, and out of which jars, to find out how to fix the labels on the jars?

63. What is the most efficient way, memory-wise, to store 1 million phone numbers?
How do you find the minimum number in a stack of unordered integers?

64. You have 100 doors in a row that are all initially closed. you make 100 passes by the doors starting with the first door every time. the first time through you visit every door and toggle the door (if the door is closed, you open it, if its open, you close it). the second time you only visit every 2nd door (door #2, #4, #6). the third time, every 3rd door (door #3, #6, #9), etc, until you only visit the 100th door. Question: what state are the doors in after the last pass? which are open which are closed?

65.What is the difference between binary search and linear search? Is one always faster than the other? What are the advantages to one over the other?

Base Knowledge questions (technical)

66. What is clean code?

67. What development tools have you used?

68. What source control tools have you used?

69. Tell me about the project you are most proud of, and what your contribution was.

70. What is MVC?

71. What is OO? - give an example

72. What is an object?

73. What is a class?

74. What is the relationship between an object and a class?

75. What is the difference between arrays and collection?

76. What is the difference between a symbol and a string?

Causes interview sample:

77. Given a list of words, return list of [word, count] pairs, ordered by count

78. Given set of rows, return string that renders it in an html table.
problem_3([["one", "uno"], ["two", "dos"]])
"<table>" +
    "<tbody>" +
        "<tr><td>one</td><td>uno</td></tr>" +
        "<tr><td>two</td><td>dos</td></tr>" +
    "</tbody>" +
"</table>"

79. Sort a list of file sizes. "K", "M", and "G" are abbreviations for kilobytes, megabytes, gigabytes; a number without a suffix is in bytes.
["1m", "20g", "5012"] -> ["5012", "1m", "20g"] 

80. Print all the prime numbers up to and including the value passed in.

81. Given a target word and list of words, return words from the list that are anagrams of the target word.

82. Test if two deeply nested arrays hold the same values.

83. Given a string of parentheses, test if it is balanced.

84. Given a year and month, render the calendar month as strin, sunday through saturday.

Euler

85. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

86. Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz instead of the number and for the multiples of five print Buzz. For numbers which are multiples of both three and five print FizzBuzz

87. Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. 


88. The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?

89.A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

90. 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

91.The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

92. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

93.Find the greatest product of five consecutive digits in the 1000-digit number.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

94.A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

95. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


Faceook interview

96. Given a binary tree, write code to print the tree out line by line. BFS

97. How would you implement division without +, - or multiplication

98. Given 10,000 servers containing a Billion integers each how would you find how to find the median?

99. Given a List structure where each node contains a Next node and optionally a pointer to another list, flatten that list
e.g.

L1 --> L2 --> L3 --> L7 --> L8
                      |
                      v
                     L4 --> L5-->L6

WIll be flattened to
L1 --> L2 --> L3 -->L4 -->L5-->L6-->L7-->L8

100. Write a function which given two binary numbers as strings returns the sum of them in binary.

101. Given a list of strings, return a list of lists, where each list consists of words that are anagrams." Example: Given ["cab", "cz", "abc", "bca", "zc"] the output should be: [ [ "abc", "bca", "cab"] , [ "zc", cz"]].

102. Write a function which returns the nth number of Fibonacci (iterative and recursive)

103.  Given a string write a function which prints all the subsets of the string. Now make the function to return only unique solutions.

104. Reverse a linked list dynamically. So also, delete the nodes.  

105. Given an array of numbers, they are arranged so that the a[0] is in the 1st bucket, a[1]a[2] are in the 2nd bucket, a[3]a[4]a[5] is in the 3rd bucket and so on. The question is then: given a number, you need to return if it is in any bucket or not.  

106.  Given a list of 4 billion integers, find an integer not in the list using 4MB of memory.

107. checking if a string is palindrome the second one is to print out all the subsets, multiply numbers in string. 

108. Program "atof", which means convert a string float (e.g. "345.44E-10") to an actual float without using any existing Parse Float functions.

109. tree traversal, print the tree by level (asked alot)

110.  Function to check if 2 words are anagrams

111. Function to check if any 3 numbers sum to x.

112. You are given 2 streams of data, representing very sparse vectors
you are guaranteed that the 2 incoming streams are of same size
give a data structure which is optimized for producing the dot product of those sparse vectors
analyze your runtime/space complexity,
b) what if you are now told that v1, is much more sparse than v2
give another (or the same) data structure optimized for the dot product of any such 2 vectors (where 1 is more sparse than the other)
analyze your runtime/space complexity,

113. merge two sorted arrays together

114. given a m * n grids, and one is allowed to move up or right, find the number of paths between two grids.

115. write an algorithm such that if an element in a M*N matrix is 0, its entire row and column are set to 0.

116. find combinations of a sequence of numbers, which are produced by a six-side dice.

117. Given an array of integers, find the sub array with the largest sum. (must be done in linear time)

118. Implement a very basic regular expression checker which given a string and a regex, returns true or false. Should consider 'a'-'z','.', and '*'.   

119. putting the largest prime factorization in a given pattern

120. write a function to check if a binary tree was valid

121. implement strstr() 

122. convert sorted array to bst, print level by level

123. Given a bipartite graph, separate the vertices into two sets.  

124. Given two strings representing integer numbers ("123" , "30") return a string representing the sum of the two numbers ("153") 

125. Write a code to find the maximum and minimum number in an array. Now can you improve the code to use minimum number of comparison operaton. Less than n was the objective.


126. list out all the paths in a binary tree 

127. checking if a string was a palindrome for strings with symbols and spaces in them 

128. Levenshtein Distance, Sum of 1's in a submatrix, Print all paths of a binary tree, Palindrome 

129. Given two string representations of binary numbers (e.g. "1001", "10") write a function that adds them and returns the result as a string as well (e.g. "1011").

130. a) first, write a function to calculate the hamming distance between two binary numbers

(b) write a function that takes a list of binary numbers and returns the sum of the hamming distances for each pair

(c) the answer I gave for b was O(n^2), I was then tasked with finding a more efficient solution. I struggled mightily, and was eventually helped to the solution by many hints from the interviewer.


131.  Calculate the square root of a double

132. Given n intervals [si, fi], find the maximum number of overlapping intervals.

133. Print all the paths from root to every leaf in a binary tree.

134. Print the sum of all the numbers at every vertical level in a binary tree

135. Given a set of n jobs with [start time, end time, cost] find a subset so that no 2 jobs overlap and the cost is maximum ?

136. Given 1 trillion messages on fb and each message has at max 10 words, how do you build the index table and how many machines do you need on the cluster to store the index table ?

137. Given a set of n jobs with [start time, end time, cost] find a subset so that no 2 jobs overlap and the cost is maximum ?

138. Given an input array and another array that describes a new index for each element, mutate the input array so that each element ends up in their new index. Discuss the runtime of the algorithm and how you can be sure there won't be any infinite loops. 


139. finding all the anagrams in an array of strings

140. finding the number of ways a given score could be reached for a game with 3 different ways of scoring (e.g. 3, 5 and 10 points).

141.  Implement a square root function using only +,-,*,/ 

142.  Given a binary search tree, write an algorithm to find the kth smallest element

143. Given a vector of Nodes, each of which contain the start and end time of a meeting, find the maximum number of rooms one would have to book for the day

144. Reverse a linked list destructively

145.  Identify if the words in a given sentence are in a built in dictionary.  

146. Given a string, return true if it's a palindrome. Only alphanumeric characters considered. Do this in one pass through the string.  

147. 1.1. given a list of words, group anagrams.
1.2. find all 3 items that sum to 0 in an array.
2.1. Write a function that calculates input strings with operators +,-,*,/ eg. "5+5*6" should output 35 


148. Print matrix as list of lists.


149. Write a function that helps cashier to give change back with as few coins as possible. Input is change need to be given back, output is minimum number of coins needed.

































