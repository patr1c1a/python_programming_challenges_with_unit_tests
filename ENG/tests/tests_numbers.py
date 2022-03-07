###########################
# DO NOT MODIFY THIS FILE #
###########################

import unittest
from ENG.src.numbers import *


class TestsNumberFunctions(unittest.TestCase):

    def test_smallest(self):
        test_cases = {
            'Arguments used: 3, 1': [
                smallest(3, 1),
                1
            ],
            'Arguments used: 3, 3': [
                smallest(3, 3),
                3
            ],
            'Arguments used: -4, 1': [
                smallest(-4, 1),
                -4
            ],
            'Arguments used: 2, -3': [
                smallest(2, -3),
                -3
            ],
            'Arguments used: -1, -1': [
                smallest(-1, -1),
                -1
            ],
            'Arguments used: 0, 0': [
                smallest(0, 0),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_absolute_value(self):
        test_cases = {
            'Argument used: 3': [
                absolute_value(3),
                3
            ],
            'Argument used: -10': [
                absolute_value(-10),
                10
            ],
            'Argument used: 0': [
                absolute_value(0),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_extract_month(self):
        test_cases = {
            'Argument used: 31122020': [
                extract_month(31122020),
                12
            ],
            'Argument used: 5091946': [
                extract_month(5091946),
                9
            ],
            'Argument used: 10021582': [
                extract_month(10021582),
                2
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_add_multiples(self):
        test_cases = {
            'Arguments used: 0, 30, 5': [
                add_multiples(0, 30, 5),
                105
            ],
            'Arguments used: -30, 0, 5': [
                add_multiples(-30, 0, 5),
                -105
            ],
            'Arguments used: 100, 105, 9': [
                add_multiples(100, 105, 9),
                0
            ],
            'Arguments used: 5, 5, 4': [
                add_multiples(5, 5, 4),
                0
            ],
            'Arguments used: 0, 0, 1': [
                add_multiples(0, 0, 1),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_palindromic_number(self):
        test_cases = {
            'Argument used: 123321': [
                is_palindromic_number(123321),
                True
            ],
            'Argument used: 1234': [
                is_palindromic_number(1234),
                False
            ],
            'Argument used: 0': [
                is_palindromic_number(0),
                True
            ],
            'Argument used: 111': [
                is_palindromic_number(111),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_leap_year(self):
        test_cases = {
            'Argument used: 2000': [
                leap_year(2000),
                True
            ],
            'Argument used: 2020': [
                leap_year(2020),
                True
            ],
            'Argument used: 1800': [
                leap_year(1800),
                False
            ],
            'Argument used: 1533': [
                leap_year(1533),
                False
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_days_in_month(self):
        test_cases = {
            'Arguments used: 11, 1981': [
                days_in_month(11, 1981),
                30
            ],
            'Arguments used: 12, 2020': [
                days_in_month(12, 2020),
                31
            ],
            'Arguments used: 2, 2020': [
                days_in_month(2, 2020),
                29
            ],
            'Arguments used: 2, 2019': [
                days_in_month(2, 2019),
                28
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_digit_count(self):
        test_cases = {
            'Argument used: 120': [
                digit_count(120),
                3
            ],
            'Argument used: 123456789': [
                digit_count(123456789),
                9
            ],
            'Argument used: 1': [
                digit_count(1),
                1
            ],
            'Argument used: 0': [
                digit_count(0),
                1
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_add_square_digits(self):
        test_cases = {
            'Argument used: 15': [
                add_square_digits(15),
                26
            ],
            'Argument used: 2': [
                add_square_digits(2),
                4
            ],
            'Argument used: 200': [
                add_square_digits(200),
                4
            ],
            'Argument used: 6503': [
                add_square_digits(6503),
                70
            ],
            'Argument used: 0': [
                add_square_digits(0),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_percentage_even_digits(self):
        test_cases = {
            'Argument used: 5555666555': [
                percentage_even_digits(5555666555),
                30.0
            ],
            'Argument used: 123456': [
                percentage_even_digits(123456),
                50.0
            ],
            'Argument used: 0': [
                percentage_even_digits(0),
                0.0
            ],
            'Argument used: 1': [
                percentage_even_digits(1),
                0.0
            ],
            'Argument used: 1111': [
                percentage_even_digits(1111),
                0.0
            ],
            'Argument used: 2222': [
                percentage_even_digits(2222),
                100.0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_pronic(self):
        test_cases = {
            'Argument used: 56': [
                is_pronic(56),
                True
            ],
            'Argument used: 182': [
                is_pronic(182),
                True
            ],
            'Argument used: 8': [
                is_pronic(8),
                False
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_prime(self):
        test_cases = {
            'Argument used: 7': [
                is_prime(7),
                True
            ],
            'Argument used: 10': [
                is_prime(10),
                False
            ],
            'Argument used: 0': [
                is_prime(0),
                False
            ],
            'Argument used: 47': [
                is_prime(47),
                True
            ]

        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_factorial(self):
        test_cases = {
            'Argument used: 4': [
                factorial(4),
                24
            ],
            'Argument used: 0': [
                factorial(0),
                1
            ],
            'Argument used: 1': [
                factorial(1),
                1
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_sum_first_n_fibonacci(self):
        test_cases = {
            'Argument used: 6': [
                sum_first_n_fibonacci(6),
                12
            ],
            'Argument used: 2': [
                sum_first_n_fibonacci(2),
                1
            ],
            'Argument used: 3': [
                sum_first_n_fibonacci(15),
                986
            ],
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_greatest_divisor(self):
        test_cases = {
            'Argument used: 182': [
                greatest_divisor(182),
                91
            ],
            'Argument used: 25': [
                greatest_divisor(25),
                5
            ],
            'Argument used: 8': [
                greatest_divisor(8),
                4
            ],
            'Argument used: 1': [
                greatest_divisor(1),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_euclidean_gcd(self):
        test_cases = {
            'Arguments used: 60, 24': [
                euclidean_gcd(60, 24),
                12
            ],
            'Arguments used: 24, 60': [
                euclidean_gcd(24, 60),
                12
            ],
            'Arguments used: 10, 20': [
                euclidean_gcd(10, 20),
                10
            ],
            'Arguments used: 1, 625': [
                euclidean_gcd(1, 625),
                1
            ],
            'Arguments used: 0, 14': [
                euclidean_gcd(0, 14),
                14
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_get_month(self):
        test_cases = {
            'Arguments used: 200, 1969': [
                get_month(200, 1969),
                7
            ],
            'Arguments used: 1, 1981': [
                get_month(1, 1981),
                1
            ],
            'Arguments used: 60, 2020': [
                get_month(60, 2020),
                2
            ],
            'Arguments used: 60, 2018': [
                get_month(60, 2018),
                3
            ],
            'Arguments used: 365, 2014': [
                get_month(365, 2014),
                12
            ],
            'Arguments used: 366, 2020': [
                get_month(366, 2020),
                12
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_disarium(self):
        test_cases = {
            'Argument used: 518': [
                is_disarium(518),
                True
            ],
            'Argument used: 175': [
                is_disarium(175),
                True
            ],
            'Argument used: 89': [
                is_disarium(89),
                True
            ],
            'Argument used: 182': [
                is_disarium(182),
                False
            ],
            'Argument used: 91': [
                is_disarium(91),
                False
            ],
            'Argument used: 4': [
                is_disarium(4),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_arrange_coins(self):
        test_cases = {
            'Argument used: 5': [
                arrange_coins(5),
                2
            ],
            'Argument used: 6': [
                arrange_coins(6),
                3
            ],
            'Argument used: 8': [
                arrange_coins(8),
                3
            ],
            'Argument used: 10': [
                arrange_coins(10),
                4
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_single_ones(self):
        test_cases = {
            'Argument used: 141211': [
                single_ones(141211),
                2
            ],
            'Argument used: 11411211': [
                single_ones(11411211),
                0
            ],
            'Argument used: 1141121': [
                single_ones(1141121),
                1
            ],
            'Argument used: 1111': [
                single_ones(1111),
                0
            ],
            'Argument used: 321': [
                single_ones(321),
                1
            ],
            'Argument used: 8888': [
                single_ones(8888),
                0
            ],
            'Argument used: 0': [
                single_ones(0),
                0
            ],
            'Argument used: 1': [
                single_ones(1),
                1
            ],
            'Argument used: 12131415161718191': [
                single_ones(12131415161718191),
                9
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)
