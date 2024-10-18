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
def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
        >>> single_letter_count('Hello World', 'h')
        1
        >>> single_letter_count('Hello World', 'z')
        0
        >>> single_letter_count("Hello World", 'l')
        3
    """
    # turing the variable input into a list after it has been lower cased
    list_word = list(word.lower())
    # return the number of times the variable 'letter' appears in the list 'list_word'
    return list_word.count(letter)

print(single_letter_count('Hello World', 'h'))
print(single_letter_count('Hello World', 'z'))
print(single_letter_count('Hello World', 'l'))