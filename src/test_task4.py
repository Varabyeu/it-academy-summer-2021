import ddt
import task4
import unittest


@ddt.ddt
class TestCase(unittest.TestCase):
    @ddt.data(
        (2, 10 ** 3, 10 ** 9, 442530011399),
        (2, 10 ** 6, 10 ** 9, 450186511399999),

    )
    @ddt.unpack
    def test_positive_nums(
            self,
            input_data_start,
            input_data_end,
            input_data_limit,
            expected
    ):
        """This function is used to be a test for Euler project task

        This test gets inputted data and compares result of function
        with expected one using assertEqual
        """
        result = task4.f_n(
            input_data_start,
            input_data_end,
            input_data_limit
        )
        self.assertEqual(result, expected)

    @ddt.data(
        (2, 10 ** 3, 10 ** 9, 442530011399),
        (2, 10 ** 6, 10 ** 9, 450186511399999),

    )
    @ddt.unpack
    def test_negative_num(
            self,
            input_data_start,
            input_data_end,
            input_data_limit,
            expected
    ):
        """This function is used to be a test for Euler project task

        This negative test gets inputted data and compares result
         of function with expected one using assertEqual
        """
        result = task4.f_n(
            input_data_start,
            input_data_end,
            input_data_limit
        )
        self.assertEqual(result, expected)

        @ddt.data(
            ('2', 10 ** 3, 10 ** 9, TypeError),
            (2, '10 ** 3', 10 ** 9, TypeError),
            (2, 10 ** 3, '10 ** 9', TypeError),
            (2, 10 ** 3, [10 ** 9], TypeError),
            (2, [10 ** 3], 10 ** 9, TypeError),
            ([2], 10 ** 3, 10 ** 9, TypeError),
            ((2, ), 10 ** 3, 10 ** 9, TypeError),
            (2, (10 ** 3), 10 ** 9, TypeError),
            (2, 10 ** 3, (10 ** 9), TypeError),
            ({2}, 10 ** 3, 10 ** 9, TypeError),
            (2, {10 ** 3}, 10 ** 9, TypeError),
            (2, 10 ** 3, {10 ** 9}, TypeError),
        )
        @ddt.unpack
        def test_negative_data_type(
                self,
                input_data_start,
                input_data_end,
                input_data_limit,
                expected
        ):
            """This function is used to be a test for Euler project task

            This negative test gets inputted data and expect an inputted
            type of error as a result of function
            """
            with self.assertRaises(expected):
                task4.f_n(
                    input_data_start,
                    input_data_end,
                    input_data_limit)


if __name__ == '__name__':
    unittest.main()
