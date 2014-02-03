# These methods are named to provide hints as to what they do.
# How many errors can you find in this code?
# Add test cases to main() to make sure that the code works as you'd expect.
# How many ways can you break this code? What do you have to protect against /
#   be able to handle, for this code to be production-ready?
 
def accumulate(array):
  sum = array[0]
  for item in array:
    sum = sum + item
  return sum
 
def average(array):
  return accumulate(array) / len(array)
 
def concatenate(array):
  return accumulate(array)
 
def main():
  numbers = [1, 2, 3, 4, 5]
  print average(numbers)
 
  strings = ['hello', ' ', 'world']
  print concatenate(strings)
 
main()



