###########################
# DO NOT MODIFY THIS FILE #
###########################

import unittest
from ENG.src.numbers import *


class TestsNumberFunctions(unittest.TestCase):

    def test_smallest(self):
        test_cases = {
            'Arguments used: number1=3, number2=1': [
                smallest(number1=3, number2=1),
                1
            ],
            'Arguments used: number1=1, number2=3': [
                smallest(number1=3, number2=1),
                1
            ],
            'Arguments used: number1=3, number2=3': [
                smallest(number1=3, number2=3),
                3
            ],
            'Arguments used: number1=-4, number2=1': [
                smallest(number1=-4, number2=1),
                -4
            ],
            'Arguments used: number1=2, number2=-3': [
                smallest(number1=2, number2=-3),
                -3
            ],
            'Arguments used: number1=-1, number2=-1': [
                smallest(number1=-1, number2=-1),
                -1
            ],
            'Arguments used: number1=0, number2=0': [
                smallest(number1=-5, number2=0),
                -5
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_absolute_value(self):
        test_cases = {
            'Argument used: number=3': [
                absolute_value(number=3),
                3
            ],
            'Argument used: number=-10': [
                absolute_value(number=-10),
                10
            ],
            'Argument used: number=0': [
                absolute_value(number=0),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_extract_month(self):
        test_cases = {
            'Argument used: date=31122020': [
                extract_month(date=31122020),
                12
            ],
            'Argument used: date=5091946': [
                extract_month(date=5091946),
                9
            ],
            'Argument used: date=10021582': [
                extract_month(date=10021582),
                2
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_add_multiples(self):
        test_cases = {
            'Arguments used: lower=0, upper=30, n=5': [
                add_multiples(lower=0, upper=30, n=5),
                105
            ],
            'Arguments used: lower=-30, upper=0, n=5': [
                add_multiples(lower=-30, upper=0, n=5),
                -105
            ],
            'Arguments used: lower=100, upper=105, n=9': [
                add_multiples(lower=100, upper=105, n=9),
                0
            ],
            'Arguments used: lower=5, upper=5, n=4': [
                add_multiples(lower=5, upper=5, n=4),
                0
            ],
            'Arguments used: lower=0, upper=0, n=1': [
                add_multiples(lower=0, upper=0, n=1),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_palindromic_number(self):
        test_cases = {
            'Argument used: number=123321': [
                is_palindromic_number(number=123321),
                True
            ],
            'Argument used: number=1234': [
                is_palindromic_number(number=1234),
                False
            ],
            'Argument used: number=0': [
                is_palindromic_number(number=0),
                True
            ],
            'Argument used: number=111': [
                is_palindromic_number(number=111),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_leap_year(self):
        test_cases = {
            'Argument used: year=2000': [
                leap_year(year=2000),
                True
            ],
            'Argument used: year=2020': [
                leap_year(year=2020),
                True
            ],
            'Argument used: year=1800': [
                leap_year(year=1800),
                False
            ],
            'Argument used: year=1533': [
                leap_year(year=1533),
                False
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_days_in_month(self):
        test_cases = {
            'Arguments used: month=11, year=1981': [
                days_in_month(month=11, year=1981),
                30
            ],
            'Arguments used: month=12, year=2020': [
                days_in_month(month=12, year=2020),
                31
            ],
            'Arguments used: month=2, year=2020': [
                days_in_month(month=2, year=2020),
                29
            ],
            'Arguments used: month=2, year=2019': [
                days_in_month(month=2, year=2019),
                28
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_digit_count(self):
        test_cases = {
            'Argument used: number=120': [
                digit_count(number=120),
                3
            ],
            'Argument used: number=123456789': [
                digit_count(number=123456789),
                9
            ],
            'Argument used: number=1': [
                digit_count(number=1),
                1
            ],
            'Argument used: number=0': [
                digit_count(number=0),
                1
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_add_square_digits(self):
        test_cases = {
            'Argument used: number=15': [
                add_square_digits(number=15),
                26
            ],
            'Argument used: number=2': [
                add_square_digits(number=2),
                4
            ],
            'Argument used: number=200': [
                add_square_digits(number=200),
                4
            ],
            'Argument used: number=6503': [
                add_square_digits(number=6503),
                70
            ],
            'Argument used: number=0': [
                add_square_digits(number=0),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_percentage_even_digits(self):
        test_cases = {
            'Argument used: number=5555666555': [
                percentage_even_digits(number=5555666555),
                30.0
            ],
            'Argument used: number=123456': [
                percentage_even_digits(number=123456),
                50.0
            ],
            'Argument used: number=0': [
                percentage_even_digits(number=0),
                0.0
            ],
            'Argument used: number=1': [
                percentage_even_digits(number=1),
                0.0
            ],
            'Argument used: number=1111': [
                percentage_even_digits(number=1111),
                0.0
            ],
            'Argument used: number=2222': [
                percentage_even_digits(number=2222),
                100.0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_pronic(self):
        test_cases = {
            'Argument used: number=56': [
                is_pronic(number=56),
                True
            ],
            'Argument used: number=182': [
                is_pronic(number=182),
                True
            ],
            'Argument used: number=8': [
                is_pronic(number=8),
                False
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_prime(self):
        test_cases = {
            'Argument used: number=7': [
                is_prime(number=7),
                True
            ],
            'Argument used: number=10': [
                is_prime(number=10),
                False
            ],
            'Argument used: number=0': [
                is_prime(number=0),
                False
            ],
            'Argument used: number=47': [
                is_prime(number=47),
                True
            ]

        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_factorial(self):
        test_cases = {
            'Argument used: number=4': [
                factorial(number=4),
                24
            ],
            'Argument used: number=0': [
                factorial(number=0),
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
            'Argument used: n=6': [
                sum_first_n_fibonacci(n=6),
                12
            ],
            'Argument used: n=2': [
                sum_first_n_fibonacci(n=2),
                1
            ],
            'Argument used: n=3': [
                sum_first_n_fibonacci(n=15),
                986
            ],
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_greatest_divisor(self):
        test_cases = {
            'Argument used: number=182': [
                greatest_divisor(number=182),
                91
            ],
            'Argument used: number=25': [
                greatest_divisor(number=25),
                5
            ],
            'Argument used: number=8': [
                greatest_divisor(number=8),
                4
            ],
            'Argument used: number=1': [
                greatest_divisor(number=1),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_euclidean_gcd(self):
        test_cases = {
            'Arguments used: m=60, n=24': [
                euclidean_gcd(m=60, n=24),
                12
            ],
            'Arguments used: m=24, n=60': [
                euclidean_gcd(m=24, n=60),
                12
            ],
            'Arguments used: m=10, n=20': [
                euclidean_gcd(m=10, n=20),
                10
            ],
            'Arguments used: m=1, n=625': [
                euclidean_gcd(m=1, n=625),
                1
            ],
            'Arguments used: m=0, n=14': [
                euclidean_gcd(m=0, n=14),
                14
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_get_month(self):
        test_cases = {
            'Arguments used: consecutive_day=200, year=1969': [
                get_month(consecutive_day=200, year=1969),
                7
            ],
            'Arguments used: consecutive_day=1, year=1981': [
                get_month(consecutive_day=1, year=1981),
                1
            ],
            'Arguments used: consecutive_day=60, year=2020': [
                get_month(consecutive_day=60, year=2020),
                2
            ],
            'Arguments used: consecutive_day=60, year=2018': [
                get_month(consecutive_day=60, year=2018),
                3
            ],
            'Arguments used: consecutive_day=365, year=2014': [
                get_month(consecutive_day=365, year=2014),
                12
            ],
            'Arguments used: consecutive_day=366, year=2020': [
                get_month(consecutive_day=366, year=2020),
                12
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_disarium(self):
        test_cases = {
            'Argument used: number=518': [
                is_disarium(number=518),
                True
            ],
            'Argument used: number=175': [
                is_disarium(number=175),
                True
            ],
            'Argument used: number=89': [
                is_disarium(number=89),
                True
            ],
            'Argument used: number=182': [
                is_disarium(number=182),
                False
            ],
            'Argument used: number=91': [
                is_disarium(number=91),
                False
            ],
            'Argument used: number=4': [
                is_disarium(number=4),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_arrange_coins(self):
        test_cases = {
            'Argument used: amount=5': [
                arrange_coins(amount=5),
                2
            ],
            'Argument used: amount=6': [
                arrange_coins(amount=6),
                3
            ],
            'Argument used: amount=8': [
                arrange_coins(amount=8),
                3
            ],
            'Argument used: amount=10': [
                arrange_coins(amount=10),
                4
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_single_ones(self):
        test_cases = {
            'Argument used: number=141211': [
                single_ones(number=141211),
                2
            ],
            'Argument used: number=11411211': [
                single_ones(number=11411211),
                0
            ],
            'Argument used: number=1141121': [
                single_ones(number=1141121),
                1
            ],
            'Argument used: number=1111': [
                single_ones(number=1111),
                0
            ],
            'Argument used: number=321': [
                single_ones(number=321),
                1
            ],
            'Argument used: number=8888': [
                single_ones(number=8888),
                0
            ],
            'Argument used: number=0': [
                single_ones(number=0),
                0
            ],
            'Argument used: number=1': [
                single_ones(number=1),
                1
            ],
            'Argument used: number=12131415161718191': [
                single_ones(number=12131415161718191),
                9
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)
