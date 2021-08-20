import ddt
import task4_hw3
import unittest


@ddt.ddt
class TestCase(unittest.TestCase):
    
    @ddt.data(
        ('1', 0),
        ('1 1', 1),
        ('1 1 1', 3),
        ('1 1 1 1', 6),
        ('1 1 1 1 1', 12),
        ('1 2 3 2 1', 2),
        ('1 2 3 3 2 1', 3),
    )
    @ddt.unpack
    def test_positive(self, input_data, expected):
        """This function is used to be a positive test"""
        result = task4_hw3.function(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ([], AttributeError),
        ({}, AttributeError),
        (1, AttributeError),

    )
    @ddt.unpack
    def test_negative(self, input_data, expected):
        """This function is used to be a negative test"""
        with self.assertRaises(expected):
            task4_hw3.function(input_data)


if __name__ == '__name__':
    unittest.main()
