# Exercise 1 Product
# def product(a, b):
#     """Return product of a and b.
#         >>> product(2, 2) = 4 >>> product(2, -2) = -4
#     """
#     return a * b 
# print(product(2,2), ',', product(2,-2)) # 4 , -4

# Exercise 2 Weekday Name
# def weekday_name(day_of_week):
#     """Return name of weekday.    
#         >>> weekday_name(1) 'Sunday'    
#         >>> weekday_name(7) 'Saturday'
        
#     For days not between 1 and 7, return None
#         >>> weekday_name(9)
#         >>> weekday_name(0)
#     """
#     # day_list = {
#     # 1: 'Monday',
#     # 2: 'Tuesday',
#     # 3: 'Wednesday',
#     # 4: 'Thursday',
#     # 5: 'Friday',
#     # 6: 'Saturday',
#     # 7: 'Sunday'
#     #  }
    
#     if day_of_week == 1:
#         return 'Monday'
#     if day_of_week == 2:
#         return 'Tuesday'
#     if day_of_week == 3:
#         return 'Wednesday'
#     if day_of_week == 4:
#         return 'Thursday'
#     if day_of_week == 5:
#         return 'Friday'
#     if day_of_week == 6:
#         return 'Saturday'
#     if day_of_week == 7:
#         return 'Sunday'
#     else:
#         None

# print(weekday_name(1),',', weekday_name(3),',', weekday_name(5),',', weekday_name(9))
# # Monday , Wednesday , Friday , None

# Exercise 3 Last Element
# def last_element(lst):
#     """Return last item in list (None if list is empty.)
#         >>> last_element([1, 2, 3]) 3        
#         >>> last_element([]) is None
#         True
#     """

#     if lst:
#         return lst.pop()
#     else:
#         return "is None"

# print(last_element([1,2,3])) # 3
# print(last_element([1,2,3,4,5,6,7,8,9])) # 9
# print(last_element([])) # is None

# Exercise 4 Number Compare
# def number_compare(a, b):
#     """Report on whether a>b, b>a, or b==a
    
#         >>> number_compare(1, 1)
#         'Numbers are equal'
        
#         >>> number_compare(-1, 1)
#         'Second is greater'
        
#         >>> number_compare(1, -2)
#         'First is greater'
#     """
#     if a == b: # if variable 'a' has the same value as variable 'b' and outputs boolean True, do the following:
#         return "Numbers are equal"
#     if a < b: # if variable 'a' value is less than the value for variable 'b' and outputs boolean True, do the following:
#         return "Second is greater"
#     if a > b: # if variable 'a' value is greater than the value for variable 'b' and outputs boolean True, do the following:
#         return "First is greater"
    
# print(number_compare(1,1)) # Numbers are equal
# print(number_compare(-1,1)) # Second is greater
# print(number_compare(1,-2)) # First is greater

# Exercise 5 Reverse String
# def reverse_string(phrase):
#     """Reverse string,
#         >>> reverse_string('awesome')
#         'emosewa'
#         >>> reverse_string('sauce')
#         'ecuas'
#     """
#     # using string slicing 
#     rev_word = phrase[::-1]

#     # another way to do the same but first turning the string into a list then converting back into a string with join. 
#     # rev_word = "".join(list(reversed(phrase)))
#     return rev_word

# print(reverse_string('awesome')) # emosewa
# print(reverse_string('sauce')) # ecuas

# Exercise 6 Single Letter Count
# def single_letter_count(word, letter):
#     """How many times does letter appear in word (case-insensitively)?
#         >>> single_letter_count('Hello World', 'h')
#         1
#         >>> single_letter_count('Hello World', 'z')
#         0
#         >>> single_letter_count("Hello World", 'l')
#         3
#     """
#     # turing the variable input into a list after it has been lower cased
#     list_word = list(word.lower())
#     # return the number of times the variable 'letter' appears in the list 'list_word'
#     return list_word.count(letter)

# print(single_letter_count('Hello World', 'h'))
# print(single_letter_count('Hello World', 'z'))
# print(single_letter_count('Hello World', 'l'))

# Exercise 7 Multiple Letter Count
# def multiple_letter_count(phrase):
#     """Return dict of {ltr: frequency} from phrase.
#         >>> multiple_letter_count('yay')
#         {'y': 2, 'a': 1}
#         >>> multiple_letter_count('Yay')
#         {'Y': 1, 'a': 1, 'y': 1}
#     """
#     new_dic = {}
    
#     for letter in phrase:
#         if letter not in new_dic:
#             new_dic[letter] = phrase.count(letter)          
                
#     return new_dic


# print(multiple_letter_count('yayyyyy'))
# print(multiple_letter_count('Yaaay'))
# print(multiple_letter_count('hello world'))

# Exercise 8 List Manipulation
# def list_manipulation(lst, command, location, value=None):
#     """Mutate lst to add/remove from beginning or end.

#     - lst: list of values
#     - command: command, either "remove" or "add"
#     - location: location to remove/add, either "beginning" or "end"
#     - value: when adding, value to add

#     remove: remove item at beginning or end, and return item removed
#         >>> lst = [1, 2, 3]
#         >>> list_manipulation(lst, 'remove', 'end') 3
#         >>> list_manipulation(lst, 'remove', 'beginning') 1
#         >>> lst [2]

#     add: add item at beginning/end, and return list
#         >>> lst = [1, 2, 3]
#         >>> list_manipulation(lst, 'add', 'beginning', 20) [20, 1, 2, 3]
#         >>> list_manipulation(lst, 'add', 'end', 30) [20, 1, 2, 3, 30]
#         >>> lst [20, 1, 2, 3, 30]

#     Invalid commands or locations should return None:
#         >>> list_manipulation(lst, 'foo', 'end') is None True
#         >>> list_manipulation(lst, 'add', 'dunno') is None True
#     """
#     if value == None:
#         if command == 'remove' and location == 'end':
#             lst.pop()              
         
#         if command == 'remove' and location == 'beginning':
#             lst.pop(0)

#     if value:
#         if command == 'add' and location == 'beginning':
#             lst.insert(0, value)
        
#         if command == 'add' and location == 'end':
#             lst.append(value)

#     if 'add' not in command and 'remove' not in command:
#             return 'None'

#     if 'end' not in location and 'beginning' not in location:
#          return 'None'   

    
#     return lst
        

# lst = [1,2,3]
# # print(list_manipulation(lst, 'remove', 'end')) # [1, 2]
# # print(list_manipulation(lst, 'remove', 'beginning')) # [2]
# print(list_manipulation(lst, 'add', 'beginning', 20)) # [20, 1, 2, 3]
# print(list_manipulation(lst, 'add', 'end', 30)) # [20, 1, 2, 3, 30]
# print(list_manipulation(lst, 'foo', 'end')) # None
# print(list_manipulation(lst, 'add', 'dunno')) # None

# Exercise 9 Is Palindrome
# def is_palindrome(phrase):
#     """Is phrase a palindrome?
#     Return True/False if phrase is a palindrome (same read backwards and
#     forwards).
#         >>> is_palindrome('tacocat')
#         True
#         >>> is_palindrome('noon')
#         True
#         >>> is_palindrome('robert')
#         False

#     Should ignore capitalization/spaces when deciding:
#         >>> is_palindrome('taco cat')
#         True
#         >>> is_palindrome('Noon')
#         True
#     """
#     list_word = [] # making empty list to be able to use  the list and reverse method on the string input so that i can make 
#     # a copy of the string reversed so that i can compare elements in order with an if statement
#     if " " in phrase: # if 'space string char' == True for the elements in the variable phrase'. At top so it executes first
#         phrase = phrase.replace(" ", "") # replace "space string char" with "empty string"
    
#     for word in phrase: # making a variable called word which is equal to the individual elements in the variable phrase
#         list_word += word # making the variable list_word = to list_word + word so that every time the loop runs it adds the element to the 
#         # list_word variable. 

#     copy_list = list_word.copy() # making a copy of the list_word variable so that you can use the reverse() method, which is a list method. 
#     copy_list.reverse() # using the list method reverse on the variable copy_list
#     rev_string = "".join(copy_list) # turing the list variable copy_list into a string with the .join string method.

#     if rev_string.lower() != phrase.lower(): # if rev_string with its elements lower cased is not equal to variable phrase with its elements lower cased 
#         # i.e. rev_string != phrase == True
#         return False # then output the Boolean False
#     elif rev_string.lower() == phrase.lower(): # else if rev_string.lower == phrase.lower == True
#         return True # then output the Boolean True. 


# print(is_palindrome('tacocat')) # True
# print(is_palindrome('noon')) # True
# print(is_palindrome('robert')) # False
# print(is_palindrome('taco cat')) # True
# print(is_palindrome('Noon')) # True
# print(is_palindrome('wizard')) # False
# print(is_palindrome('a man a plan a canal Panama')) # True

# Exercise 10 Frequency
# def frequency(lst, search_term):
#     """Return frequency of term in lst.
#         >>> frequency([1, 4, 3, 4, 4], 4)
#         3  
#         >>> frequency([1, 4, 3], 7)
#         0
#     """
#     count = 0
#     for i in lst:
#         if i == search_term:
#             count += 1
#     return count

# print(frequency([1, 4, 3, 4, 4], 4)) # 3
# print(frequency([1, 4, 3], 7)) # 0
# print(frequency([1, 4, 3, 3, 5, 3, 6, 7, 8, 3, 3, 3, 3], 3)) # 7

# Exercise 11 Flip Case
# def flip_case(phrase, to_swap):
#     """Flip [to_swap] case each time it appears in phrase.
#         >>> flip_case('Aaaahhh', 'a')
#         'aAAAhhh'
#         >>> flip_case('Aaaahhh', 'A')
#         'aAAAhhh'
#         >>> flip_case('Aaaahhh', 'h')
#         'AaaaHHH'

#     """
#     flipped_list = []

#     for i in phrase:
#         if i != to_swap: # if i does not equal to_swap == True
#             if i.lower() == to_swap: # if i.lower() is equal to_swap == True
#                 flipped_list.append(i.swapcase()) # swap the case of i and then append it to the variable flipped_list
#             if i.upper() == to_swap: # if i.upper() is equal to_swap == True
#                 flipped_list.append(i.swapcase()) # swap the case of i and then append it to the variable flipped_list
#             if i.upper() != to_swap and i.lower() != to_swap: # if i.upper() is not equal to_swap == True and i.lower() is not equal to_swap == True
#                 flipped_list.append(i) # swap the case of i and then append it to the variable flipped_list

#         if i == to_swap: # if the variable i is equal to variable to_swap == True
#             flipped_list.append(i.swapcase()) # swap the case of i and then append it to the variable flipped_list
            
#     return "".join(flipped_list) # return the list as a string using the .join method. 

# print(flip_case('Aaaahhh', 'a')) # aAAAhhh
# print(flip_case('Aaaahhh', 'A')) # aAAAhhh
# print(flip_case('Aaaahhh', 'h')) # AaaaHHH
# print(flip_case('FrejJjya', 'j')) # FreJjJya

# Exercise 12 Multiply Even Numbers
def multiply_even_numbers(nums):
    """Multiply the even numbers.
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48   
        >>> multiply_even_numbers([3, 4, 5])
        4      
    If there are no even numbers, return 1.
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    even_list = 1

    for num in nums:
        if num % 2 == 0:
            even_list = even_list * num
        if num % 2 != 0:
            num = 1          

    return even_list

print(multiply_even_numbers([2, 3, 4, 5, 6])) # 48
print(multiply_even_numbers([2, 3, 4, 5, 6, 2, 2])) # 192
print(multiply_even_numbers([3, 4, 5])) # 4
print(multiply_even_numbers([1, 3, 5])) # 1
print(multiply_even_numbers([3, 5])) # 1
print(multiply_even_numbers([3, 5, 7, 9, 11, 13])) # 1