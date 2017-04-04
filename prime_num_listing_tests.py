import unittest
from prime_num_listing import prime_num_listing

class primeNumListingTestCases(unittest.TestCase):
    def test_it_returns_prime_numbers(self):
        result = prime_num_listing(8)
        self.assertEqual(result,[2, 3, 5, 7], msg='It should produce a list of prime numbers for a range of 8')

    def test_it_returns_anemptylist_for_an_input_of_1(self):
        result = prime_num_listing(1)
        self.assertEquals(result,[],'It should return an empty list for an input of 1')

    def test_it_RaisesValueError_for_a_Negative_input(self):
        with assertRaises(ValueError):
        prime_num_listing(-7)

    def test_it_returns_anemptylist_for_an_input_of_0(self):
        result = prime_num_listing(0)
        self.assertEquals(result,[],'It should return an empty list for an input of 0')
    
     def test_it_does_not_accept_strings(self):
         with self.assertRaises(ValueError) as context:
             prime_num_listing("str")
        self.assertEqual("The provided input is not correct.",context.exception.message, "Invalid input of type str not allowed")