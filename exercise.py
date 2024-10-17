# Exercise 1 Product
# def product(a, b):
#     """Return product of a and b.
#         >>> product(2, 2) = 4 >>> product(2, -2) = -4
#     """
#     return a * b 
# print(product(2,2), ',', product(2,-2)) # 4 , -4

# Exercise 2 
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

# Exercise 3
def last_element(lst):
    """Return last item in list (None if list is empty.)
        >>> last_element([1, 2, 3]) 3        
        >>> last_element([]) is None
        True
    """

    if lst:
        return lst.pop()
    else:
        return "is None"

print(last_element([1,2,3])) # 3
print(last_element([1,2,3,4,5,6,7,8,9])) # 9
print(last_element([])) # is None
