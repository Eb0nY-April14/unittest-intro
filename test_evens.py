import unittest
# This will import the function we created in 'evens.py' file named 
# 'even_number_of_evens()' into our test file i.e test_evens.py file.
from evens import even_number_of_evens

 
# Our 'TestEvens' class needs to inherit from the 
# 'unittest.TestCase' class in order make use of 
# Unittest’s functionality.
class TestEvens(unittest.TestCase):
    # 'pass' is a valid statement that allows our code 
    # to run error free when you have no code yet. 
    # pass

    # test functions must start with the word ‘test’ or else 
    # they’ll be ignored and won’t be run when we run our tests.

    # This test should test our function to check if the value 
    # passed in is a list & returns True if it is, else raise 
    # a TypeError.
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)


    # This test should test our function, returns False if an  
    # empty list is passed in, returns True if 2 or more numbers
    # are passed in & should fail if only 1 number is passed in. 
    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)

if __name__ == '__main__':
    unittest.main()
