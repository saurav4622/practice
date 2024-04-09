# # # # #This code is created on 15th july 2023 at 11:33PM.
# # # # #This code takes three values and find the greater once.
# # # def check_value(first, second, third):
# # #     if ((first>second) and (first>third)):
# # #         print(first)
# # #     elif ((second>first) and (second>third)):
# # #         print(second)
# # #     elif ((third>first) and (third>second)):
# # #         print(third)
        
# # #     else:
# # #         print("They are equal.")
        
# # # check_value(6,6,6)

# # # def hint_username(username):
# # #     if len(username) < 4:
# # #         print("INVALID FORMAT, the username must be of more than three digits.")
# # #     else:
# # #         print("Its a valid username.")

# # # # name=str(input("Enter you username here: "))       
# # # hint_username(str(input("Enter your username here: ")))

# # # #start and end number examples
# # # def count_down(start_number):
# # #   current = start_number
# # #   while (current > 0):
# # #     print(current)
# # #     current -= 1
# # #   print("Zero!")
# # # count_down(3)

# # # #Fibonicci series
# # # total_output = int(input("Enter total Number of outputs you require: "))
# # # first = 0
# # # second = 1
# # # print(first)
# # # print(second)
# # # i=1
# # # while (i <= total_output-2):
# # #   next_num = first + second
# # #   print(next_num)
# # #   first = second
# # #   second = next_num
# # #   i +=1


# # def is_power_of_two(number):
# #   # Check if the number is zero, if so, return False
# #   if number == 0:
# #     return False
  
# #   # This while loop checks if the "number" can be divided by two
# #   # without leaving a remainder.
# #   while number % 2 == 0:
# #     number = number / 2

# #   # Return the result of the comparison
# #   return number == 1
  

# # # Calls to the function
# # print(is_power_of_two(0)) # Should be False
# # print(is_power_of_two(1)) # Should be True
# # print(is_power_of_two(8)) # Should be True
# # print(is_power_of_two(9)) # Should be False 

# # Fill in the blanks so that the while loop continues to run while the
# # "divisor" variable is less than the "number" parameter.

# def sum_divisors(number):
#     # Initialize the appropriate variables
#     divisor = 1  # Set the initial divisor
#     total = 0  # Set the initial total sum

#     # Avoid dividing by 0 and negative numbers
#     # in the while loop by exiting the function
#     # if "number" is less than one
#     if number < 1:
#         return 0

#     # Complete the while loop
#     while divisor <= number:  # Loop until the divisor is equal to or exceeds the number
#         if number % divisor == 0:
#             total += divisor
#         # Increment the correct variable
#         divisor += 1

#     # Return the correct variable
#     return total


# print(sum_divisors(0))  # Should print 0
# print(sum_divisors(3))  # Should print 1 (only divisible by 1)
# print(sum_divisors(36))  # Should print 55 (1+2+3+4+6+9+12+18)
# print(sum_divisors(102))  # Should print 114 (1+2+3+6+17+34+51)

print(36%3)
