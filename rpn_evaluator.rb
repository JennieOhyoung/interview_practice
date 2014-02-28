
# Implement a RPN evaluator. It should be able to evaluate the following strings and answer with the corresponding numbers: 
# "1 2 +" = 3 
# "4 2 /" = 2 
# "2 3 4 + *" = 14 
# "3 4 + 5 6 + *" = 77 
# "13 4 -" = 9
# And should provide an error message for the following types of errors
# "1 +" (not enough arguments)
# "a b +" (invalid number)

# We should be able to evaluate a string from the command line in the following way:
# $ ruby rpn.rb "1 2 +"

# In addition, implement your own string to number conversion function and use it in your RPN evaluator. Do not use the following: send, eval, to_i, to_f, Integer(str), Float(str), or any similar method to convert your strings to numbers in your RPN evaluator.

#  RUNNING ruby 2.0.0



# custome string to number conversion. takes array, modify according to place in base 10 system and reassemble as integer by addition.
def str_to_num(string)
    int_list = []
    final_num = 0
    string_list = string.split("")
    for char in string_list
        if 48 <= char.ord && char.ord <= 57
            int_list.push(char.ord - 48)
        else
            return false
        end
    end
    for i in 0...int_list.length
        value = int_list[-i-1]
        place = 10**i
        final_num += value*place
    end
    final_num
end

# takes operator (string) and 2 integers and perform basic math operations and returns single integer as result. if used individually, remember to pass in first_num and second_num as integers instead of strings.
def math(operator, first_num, second_num)
    if operator =="*"
        first_num*second_num
    elsif operator == "/"
        first_num/second_num
    elsif operator == "+"
        first_num+second_num
    else
        first_num-second_num
    end
end


# main function that iterates through equation passed in through argv, if item is number, push to stack until we have an operator to perform the operation. Call math function on previous 3 items and repeat until end of equation. Raises error for invalid number and insufficient arguments.
def postfix_evaluator(equation)
    stack = []
    for i in equation do
      if str_to_num(i)
        stack.push(str_to_num(i))
        puts stack
      elsif ("+-*/").include?(i)
          second_num = stack.pop
          if stack != []
            first_num = stack.pop
            result = math(i, first_num, second_num)
            stack.push(result)
          else
            raise "Not enough arguments"
          end
      else
        raise "Invalid number"
      end
    end
    stack.pop()
end


raw = ARGV
equation = raw.join.split
puts postfix_evaluator equation




