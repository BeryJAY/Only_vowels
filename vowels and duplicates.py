from collections import OrderedDict
#defining the function
def only_vowels(string):
    vowels = ["a","e","i","o","u"]
# The statement is to change the first string created into a list
    first_string = list(string)
#The conditional logic to check if the list has vowels and then create a list of those vowels
    created_list = [char for char in first_string if char in vowels]
#The statement to change the created list into a tuple
    change_list = tuple(created_list) 
#In that tuple, the duplicated have to be elimited using a function OrderedDict.from keys()      
    eliminate_duplicates = "".join(OrderedDict.fromkeys(change_list))
#The statement to create a string of vowels without duplicates   
    create_vowels = (eliminate_duplicates,)
#The conditional logic to calculate the number of duplicates in the original string    
    number_of_duplicates = [letter for letter in string if string.count(letter) > 1]
    get_new_char = "".join(OrderedDict.fromkeys(number_of_duplicates))
    create_tuple_for_duplicates = tuple(get_new_char)
    number_of_duplicates_in_created_tuple = len(create_tuple_for_duplicates)
    final_number = (number_of_duplicates_in_created_tuple,)
    final_tuple_created = create_vowels +  final_number
    print( final_tuple_created)
#calling the function
only_vowels("how is the weather today")
  
    