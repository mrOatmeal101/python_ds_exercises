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
# def multiply_even_numbers(nums):
#     """Multiply the even numbers.
#         >>> multiply_even_numbers([2, 3, 4, 5, 6])
#         48   
#         >>> multiply_even_numbers([3, 4, 5])
#         4      
#     If there are no even numbers, return 1.
#         >>> multiply_even_numbers([1, 3, 5])
#         1
#     """
#     even_list = 1

#     for num in nums:
#         if num % 2 == 0:
#             even_list = even_list * num
#         if num % 2 != 0:
#             num = 1          

#     return even_list

# print(multiply_even_numbers([2, 3, 4, 5, 6])) # 48
# print(multiply_even_numbers([2, 3, 4, 5, 6, 2, 2])) # 192
# print(multiply_even_numbers([3, 4, 5])) # 4
# print(multiply_even_numbers([1, 3, 5])) # 1
# print(multiply_even_numbers([3, 5])) # 1
# print(multiply_even_numbers([3, 5, 7, 9, 11, 13])) # 1

# Exercise 13 Capitalize
# def capitalize(phrase):
#     """Capitalize first letter of first word of phrase.
#         >>> capitalize('python')
#         'Python'
#         >>> capitalize('only first word')
#         'Only first word'
#     """
#     cap_first_letter = []

#     for letter in phrase:
#         cap_first_letter.append(letter)

#     return ''.join(cap_first_letter).capitalize()

#     # or can use 
#     # return phrase.capitalize()

#     # or can use
#     # return phrase[:1].upper() + phrase[1:]

# print(capitalize('python')) # Python
# print(capitalize('only first word')) # Only first word

# Exercise 14 Compact
# def compact(lst):
#     """Return a copy of lst with non-true elements removed.
#         >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
#         [1, 2, 'All done']
#     """
#     output = []

#     for item in lst:
#         if item:
#             output.append(item)
#         else:
#             continue

#     return output

#     # or can do this way
#     # return [val for val in lst if val]

# print(compact([0, 1, 2, '', [], False, (), None, 'All done'])) # [1, 2, 'All done']

# Exercise 15 Intersection
# def intersection(l1, l2):
#     """Return intersection of two lists as a new list::
#         >>> intersection([1, 2, 3], [2, 3, 4])
#         [2, 3]  
#         >>> intersection([1, 2, 3], [1, 2, 3, 4])
#         [1, 2, 3]  
#         >>> intersection([1, 2, 3], [3, 4])
#         [3]
#         >>> intersection([1, 2, 3], [4, 5, 6])
#         []
#     """
#     new_set1 = set(l1)
#     new_set2 = set(l2)
#     common_set = new_set1 & new_set2
#     final_output = list(common_set)

#     # if you set final_output = [] you can loop over common_set and get same result
#     # for i in common_set:
#     #     final_output = list(common_set)

#     # return final_output

#     # can also do if you want to make even shorter
#     common_set = set(l1) & set(l2)
#     final_output = list(common_set)
#     return final_output    

# print(intersection([1, 2, 3], [2, 3, 4])) # [2, 3]
# print(intersection([1, 2, 3], [1, 2, 3, 4])) # [1, 2, 3]
# print(intersection([1, 2, 3], [3, 4])) # [3]
# print(intersection([1, 2, 3], [4, 5, 6])) # []
# print(intersection([1, 2, 3, 6], [4, 5, 6, 1])) # [1, 6]

# Exercise 16 Partition
# def partition(lst, fn):
#     """Partition lst by predicate. 
#      - lst: list of items
#      - fn: function that returns True or False 
#      Returns new list: [a, b], where `a` are items that passed fn test,
#      and `b` are items that failed fn test.
#         >>> def is_even(num):
#         ...     return num % 2 == 0    
#         >>> def is_string(el):
#         ...     return isinstance(el, str)     
#         >>> partition([1, 2, 3, 4], is_even)
#         [[2, 4], [1, 3]]    
#         >>> partition(["hi", None, 6, "bye"], is_string)
#         [['hi', 'bye'], [None, 6]]
#     """ 
#     return fn(lst)        

# def is_even(val):
#     even = []
#     odd = [] 

#     for items in val:
#         if items % 2 == 0:
#             even.append(items)
#         else:
#             odd.append(items)

#     return [even, odd]

# def is_string(arg):
#     strings = []
#     not_strings = []

#     for items in arg:
#         if isinstance(items, str):
#             strings.append(items)
#         else:
#             not_strings.append(items)

#     return [strings, not_strings]

# print(partition([1, 2, 3, 4], is_even)) # [[2, 4], [1, 3]]
# print(partition(["hi", None, 6, "bye"], is_string)) # [['hi', 'bye'], [None, 6]]

# Exercise 17 Mode
# def mode(nums):
#     """Return most-common number in list.
#     For this function, there will always be a single-most-common value;
#     you do not need to worry about handling cases where more than one item
#     occurs the same number of times.
#         >>> mode([1, 2, 1])
#         1
#         >>> mode([2, 2, 3, 3, 2])
#         2
#     """
#     counts = {} # empty dic to store key value pairs from for loop

#     for num in nums: # for loop to loop over nums. 
#         #have counts keys = to the [num] = and have the values equal to the number of times num appears in nums
#         counts[num] = nums.count(num)

#     max_count = 0 # making empty variable to store values from for loop below.
#     most_common = None # making empty variable to store keys from the loop below
    
#     for key, value in counts.items():
#         # seting the variables key and value to the key:value pairs by using .items()
#         # Using .items() allows us to retrieve both the key and value in each iteration of the loop.    
#         if value > max_count: # Inside the loop, check if the current value is greater than max_count which is set to 0 on first loop
#             max_count = value # sets max_count to the the value if it was bigger. Need this so that max_count will get updated.
#             most_common = key # then this is set to the key if the value was bigger than max count.

#     return most_common        

# print(mode([1, 2, 1])) # 1
# print(mode([2, 2, 3, 3, 2])) # 2
# print(mode([2, 2, 3, 3, 2, 3, 3, 3, 3])) # 3
# print(mode([7, 9, 7, 9, 7])) # 7

# Exercise 18 Calculate
# def calculate(operation, a, b, make_int=False, message='The result is'):
#     """Perform operation on a + b, ()possibly truncating) & returning w/msg.
#     - operation: 'add', 'subtract', 'multiply', or 'divide'
#     - a and b: values to operate on
#     - make_int: (optional, defaults to False) if True, truncates to integer
#     - message: (optional) message to use (if not provided, use 'The result is')

#     Performs math operation (truncating if make_int), then returns as
#     "[message] [result]"
#         >>> calculate('add', 2.5, 4)
#         'The result is 6.5'
#         >>> calculate('subtract', 4, 1.5, make_int=True)
#         'The result is 2'
#         >>> calculate('multiply', 1.5, 2)
#         'The result is 3.0'
#         >>> calculate('divide', 10, 4, message='I got')
#         'I got 2.5'
#     If a valid operation isn't provided, return None.
#         >>> calculate('foo', 2, 3)
        
#     """
#     def add(a,b):
#         total = a + b
#         if make_int == True:
#             return int(total)
#         else:
#             return total
    
#     def subtract(a,b):
#         total = a - b
#         if make_int == True:
#             return int(total)
#         else:
#             return total
        
#     def multiply(a,b):
#         total = a * b
#         if make_int == True:
#             return int(total)
#         else:
#             return total
    
#     def divide(a,b):
#         total = a / b
#         if make_int == True:
#             return int(total)
#         else:
#             return total
    
#     if operation == 'add':
#         return f'{message}, {add(a,b)}'
#     if operation == 'subtract':
#         return f'{message}, {subtract(a,b)}'
#     if operation == 'multiply':
#         return f'{message}, {multiply(a,b)}'
#     if operation == 'divide':
#         return f'{message}, {divide(a,b)}'
#     else:
#         return None
     
# print(calculate('add', 2.5, 4, message = 'the total is')) # the total is, 6.5
# print(calculate('subtract', 4, 1.5, make_int=True)) # The result is, 2
# print(calculate('multiply', 1.5, 2)) # The result is, 3.0
# print(calculate('divide', 10, 4, message='I got')) # I got, 2.5
# print(calculate('foo', 2, 3)) # None

# Exercise 19 Friend Date
# def friend_date(a, b):
#     """Given two friends, do they have any hobbies in common?
#     - a: friend #1, a tuple of (name, age, list-of-hobbies)
#     - b: same, for friend #2
#     Returns True if they have any hobbies in common, False is not.
#         >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
#         >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
#         >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])
#         >>> friend_date(elmo, sauron)
#         False
#         >>> friend_date(sauron, gandalf)
#         True
#     """
 
#     if set(a[2]) & set(b[2]):
#         return True
#     else:
#         return False
    
# elmo = ('Elmo', 5, ['hugging', 'being nice'])
# sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
# gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])
# print(friend_date(elmo, sauron)) # False
# print(friend_date(sauron, gandalf)) # True