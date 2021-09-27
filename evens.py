def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the number of even numbers is even - return True
    """

    if isinstance(numbers, list):
        # return True

        # IF THE LIST IS EMPTY, IT WILL RETURN False. 
        # if numbers == []:
        #    return False
        # else:  # IF LIST IS NOT EMPTY, DO A COUNT OF HOW MANY NUMBERS ARE IN THE LIST
        evens = sum([1 for n in numbers if n % 2 == 0])

        # print([n for n in numbers])
        # for n in numbers:
        #    if n % 2 == 0:
        #        evens += 1
            
            # These 4 lines of code below works same as the if stmt below them
            # if evens:
            #   return evens % 2 == 0  
            # else:
            #    return False

        # IF THE COUNT OF NUMBERS IN THE LIST IS EVEN, RETURN TRUE
        # Short Way: Using single line conditional expression
        return True if (evens > 0 ) and (evens % 2 == 0) else False
        # Long Alternative Way:
        # if (evens > 0 ) and (evens % 2 == 0):
        #     return True
        # else:  # IF THE COUNT OF NUMBERS IN THE LIST IS ODD, RETURN FALSE
        #     return False

    else:
        raise TypeError("A list was not passed into the function")


# We need to prevent this function call below (i.e print....) from being run 
# when the test is run. To do this, we add the if statement. What this does is
# explained thus: When Python runs a file directly, it names it __main__ and any 
# code beneath the if statement will only be run if the name of the file is __main__.
# In other words, when we run the test file (i.e test_evens.py), it won't have the 
# name __main__ and this code beneath the 'if' statement  won't run but when we run 
# this file (i.e evens.py), it will have the  name __main__ and it will run this code.
if __name__ == '__main__':
    print(even_number_of_evens([2, 1, 4]))   