###########################
# DO NOT MODIFY THIS FILE #
###########################

import unittest
from ENG.src.dictionaries import *


class TestsSetDictionaryFunctions(unittest.TestCase):

    def test_find_duplicates(self):
        test_cases = {
            'Arguments used: ["abc", "cde", "abc", "fff"], ["cde", "aaa"]': [
                find_duplicates(["abc", "cde", "abc", "fff"], ["cde", "aaa"]),
                {"cde"}
            ],
            'Arguments used: ["abc", "cde", "fgh", "ijk"], ["fgh", "abc"]': [
                find_duplicates(["abc", "cde", "fgh", "ijk"], ["fgh", "abc"]),
                {"abc", "fgh"}
            ],
            'Arguments used: ["abc", "cde"], ["fgh", "ijk"]': [
                find_duplicates(["abc", "cde"], ["fgh", "ijk"]),
                set()
            ],
            'Arguments used: ["abc"], ["abc"]': [
                find_duplicates(["abc"], ["abc"]),
                {"abc"}
            ],
            'Arguments used: [], []': [
                find_duplicates([], []),
                set()
            ],
            'Arguments used: ["abc", "cde", "abc", "fff"], []': [
                find_duplicates(["abc", "cde", "abc", "fff"], []),
                set()
            ],
            'Arguments used: [], ["abc", "cde", "abc", "fff"]': [
                find_duplicates([], ["abc", "cde", "abc", "fff"]),
                set()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_only_one_pet_type(self):
        test_cases = {
            'Arguments used: ["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"],'
            '["John Sebastian Batch", "Jon Jack Russo", "Anna Bologna", "Christopher Colum"]': [
                only_one_pet_type(["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"],
                                  ["John Sebastian Batch", "Jon Jack Russo", "Anna Bologna", "Christopher Colum"]),
                {"Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"}
            ],
            'Arguments used: ["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"], ["Jon Jack Russo",'
            '"Anna Bologna"]': [
                only_one_pet_type(["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"],
                                  ["Jon Jack Russo", "Anna Bologna"]),
                {"Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum", "Jon Jack Russo", "Anna Bologna"}
            ],
            'Arguments used: ["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"], ["Lucrezia Georgia",'
            '"Jon Jack Russo", "Anna Bologna"]': [
                only_one_pet_type(["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"],
                                  ["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"]),
                set()
            ],
            'Arguments used: ["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"], ["Lucrezia Georgia",'
            '"Jon Jack Russo"]': [
                only_one_pet_type(["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"],
                                  ["Lucrezia Georgia", "Jon Jack Russo"]),
                {"Anna Bologna"}
            ],
            'Arguments used: ["Lucrezia Georgia", "Jon Jack Russo"], ["Lucrezia Georgia", "Jon Jack Russo",'
            '"Anna Bologna"]': [
                only_one_pet_type(["Lucrezia Georgia", "Jon Jack Russo"],
                                  ["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"]),
                {"Anna Bologna"}
            ],
            'Arguments used: [], ["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"]': [
                only_one_pet_type([],
                                  ["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"]),
                {"Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"}
            ],
            'Arguments used: ["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"], []': [
                only_one_pet_type(["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"],
                                  []),
                {"Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_unique_elements(self):
        test_cases = {
            'Argument used: [(1,2,3), (2,2,2,2), (3,4,5), (1,3,5,7,9)]': [
                unique_elements([(1, 2, 3), (2, 2, 2, 2), (3, 4, 5), (1, 3, 5, 7, 9)]),
                (1, 2, 3, 4, 5, 7, 9)
            ],
            'Argument used: [(1,2,3), (1,2,3), (1,2,3)]': [
                unique_elements([(1, 2, 3), (1, 2, 3), (1, 2, 3)]),
                (1, 2, 3)
            ],
            'Argument used: [(1,2,3)]': [
                unique_elements([(1, 2, 3)]),
                (1, 2, 3)
            ],
            'Argument used: [(1,2,3), (4,5,6), (7,8,9)]': [
                unique_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)]),
                (1, 2, 3, 4, 5, 6, 7, 8, 9)
            ],
            'Argument used: [(1,1,1), (1,1,1), (1,1,1)]': [
                unique_elements([(1, 1, 1), (1, 1, 1), (1, 1, 1)]),
                (1,)
            ],
            'Argument used: []': [
                unique_elements([]),
                ()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_unique_last_names(self):
        test_cases = {
            'Argument used: ["Maude Baker", "Milton Llewellyn Davis", "Leela Evans", "Keelan Davis"]': [
                unique_last_names(["Maude Baker", "Milton Llewellyn Davis", "Leela Evans", "Keelan Davis"]),
                {"Baker", "Davis", "Evans"}
            ],
            'Argument used: ["Maude Baker", "Milton Llewellyn Davis", "Leela Evans"]': [
                unique_last_names(["Maude Baker", "Milton Llewellyn Davis", "Leela Evans"]),
                {"Baker", "Davis", "Evans"}
            ],
            'Argument used: ["Maude Baker", "Milton Llewellyn Baker", "Leela Baker", "Keelan Baker"]': [
                unique_last_names(["Maude Baker", "Milton Llewellyn Baker", "Leela Baker", "Keelan Baker"]),
                {"Baker"}
            ],
            'Argument used: []': [
                unique_last_names([]),
                set()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_billing_addresses(self):
        test_cases = {
            'Argument used: [("Stephan Carey", 5, 1250.23, "355 Boulevard St."), ("Jocelyn Harris", 7, 699,'
            '"218 Main St."), ("Stephan Carey", 7, 532.90, "355 Boulevard St."), ("Frances Adams", 12, 57.99, '
            '"761 South Rd."), ("Jocelyn Harris", 15, 958, "218 Main St.")]': [
                billing_addresses([("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                                   ("Jocelyn Harris", 7, 699, "218 Main St."),
                                   ("Stephan Carey", 7, 532.90, "355 Boulevard St."),
                                   ("Frances Adams", 12, 57.99, "761 South Rd."),
                                   ("Jocelyn Harris", 15, 958, "218 Main St.")]),
                {'355 Boulevard St.', '218 Main St.', '761 South Rd.'}
            ],
            'Argument used: [("Stephan Carey", 5, 1250.23, "355 Boulevard St."), ("Jocelyn Harris", 7, 699, '
            '"218 Main St."), ("Frances Adams", 12, 57.99, "761 South Rd.")]': [
                billing_addresses([("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                                   ("Jocelyn Harris", 7, 699, "218 Main St."),
                                   ("Frances Adams", 12, 57.99, "761 South Rd.")]),
                {'355 Boulevard St.', '218 Main St.', '761 South Rd.'}
            ],
            'Argument used: [("Stephan Carey", 5, 1250.23, "355 Boulevard St."), ("Stephan Carey", 5, 1250.23, '
            '"355 Boulevard St."), ("Stephan Carey", 5, 1250.23, "355 Boulevard St.")]': [
                billing_addresses([("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                                   ("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                                   ("Stephan Carey", 5, 1250.23, "355 Boulevard St.")]),
                {'355 Boulevard St.'}
            ],
            'Argument used: []': [
                billing_addresses([]),
                set()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_add_movie(self):
        test_cases = {
            'Arguments used: {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]},'
            '("Lord of the rings: The two towers", "Peter Jackson", 2002)': [
                add_movie({"Joker": ["Todd Phillips", 2019],
                           "Avatar": ["James Cameron", 2009]},
                          ("Lord of the rings: The two towers", "Peter Jackson", 2002)),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009],
                 "Lord of the rings: The two towers": ["Peter Jackson", 2002]}
            ],
            'Arguments used: {}, ("Lord of the rings: The two towers", "Peter Jackson", 2002)': [
                add_movie({},
                          ("Lord of the rings: The two towers", "Peter Jackson", 2002)),
                {"Lord of the rings: The two towers": ["Peter Jackson", 2002]}
            ],
            'Arguments used: {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]},'
            '("Avatar", "James Cameron", 2009)': [
                add_movie({"Joker": ["Todd Phillips", 2019],
                           "Avatar": ["James Cameron", 2009]},
                          ("Avatar", "James Cameron", 2009)),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}
            ],
            'Arguments used: {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, ()': [
                add_movie({"Joker": ["Todd Phillips", 2019],
                           "Avatar": ["James Cameron", 2009]},
                          ()),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_most_voted(self):
        test_cases = {
            'Arguments used: {1:["john","john","laura","john","laura","paula"], 2:["amy","sean","olivia","olivia"],'
            '3:["liam","sophie","liam","sophie","sophie","isabella","sophie"]}, 3': [
                most_voted({1: ["john", "john", "laura", "john", "laura", "paula"],
                            2: ["amy", "sean", "olivia", "olivia"],
                            3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                           3),
                {"liam", "sophie", "isabella"}
            ],
            'Arguments used: {1:["john","laura","paula"], 2:["amy","sean","olivia","olivia"], '
            '3:["liam","sophie","liam","sophie","sophie","isabella","sophie"]}, 1': [
                most_voted({1: ["john", "laura", "paula"], 2: ["amy", "sean", "olivia", "olivia"],
                            3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                           1),
                {"john", "laura", "paula"}
            ],
            'Arguments used: {1:["laura","laura","laura","laura"], 2:["amy","sean","olivia","olivia"], '
            '3:["liam","sophie","liam","sophie","sophie","isabella","sophie"]}, 1': [
                most_voted(
                    {1: ["laura", "laura", "laura", "laura"], 2: ["amy", "sean", "olivia", "olivia"],
                     3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                    1),
                {"laura"}
            ],
            'Arguments used: {1:["john","john","laura","john","laura","paula"], 2:["amy","sean","olivia","olivia"], '
            '3:["liam","sophie","liam","sophie","sophie","isabella","sophie"]}, 4': [
                most_voted({1: ["john", "john", "laura", "john", "laura", "paula"],
                            2: ["amy", "sean", "olivia", "olivia"],
                            3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                           4),
                set()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_digit_occurrence(self):
        test_cases = {
            'Argument used: [8, 9, 0, 4, 2, 2, 4, 1, 8, 2]': [
                digit_occurrence([8, 9, 0, 4, 2, 2, 4, 1, 8, 2]),
                {0: 1, 1: 1, 2: 3, 3: 0, 4: 2, 5: 0, 6: 0, 7: 0, 8: 2, 9: 1}
            ],
            'Argument used: [0, 0, 0, 0, 0, 0]': [
                digit_occurrence([0, 0, 0, 0, 0, 0]),
                {0: 6, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            ],
            'Argument used: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]': [
                digit_occurrence([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
            ],
            'Argument used: []': [
                digit_occurrence([]),
                {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_count_occurrences(self):
        test_cases = {
            'Argument used: (["i", "%", "u"], ["^", "%", "^", "s", "i", "i", "u"], ["a", "u"])': [
                count_occurrences((["i", "%", "u"], ["^", "%", "^", "s", "i", "i", "u"], ["a", "u"])),
                {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
            ],
            'Argument used: (["i", "%", "u", "^", "%", "^", "s", "i", "i", "u", "a", "u"])': [
                count_occurrences((["i", "%", "u", "^", "%", "^", "s", "i", "i", "u", "a", "u"])),
                {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
            ],
            'Argument used: (["i", "%", "u"], ["i", "%", "u"], ["i", "%", "u"])': [
                count_occurrences((["i", "%", "u"], ["i", "%", "u"], ["i", "%", "u"])),
                {'i': 3, '%': 3, 'u': 3}
            ],
            'Argument used: (["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"])': [
                count_occurrences((["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"])),
                {'i': 12}
            ],
            'Argument used: ([], [], [], [], [])': [
                count_occurrences(([], [], [], [], [])),
                {}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_highest_value(self):
        test_cases = {
            'Arguments used: {"a":1, "e":7, "i":4, "o":9, "u":3}': [
                highest_value({"a": 1, "e": 7, "i": 4, "o": 9, "u": 3}),
                "o"
            ],
            'Arguments used: {"z":198}': [
                highest_value({"z": 198}),
                "z"
            ],
            'Arguments used: {}': [
                highest_value({}),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_sowing_season(self):
        test_cases = {
            'Arguments used: {"spinach":["february","march"], "garlic":["february","march","april"], "eggplant":'
            '["july","august","september"]}, "march"': [
                sowing_season({"spinach": ["february", "march"],
                               "garlic": ["february", "march", "april"],
                               "eggplant": ["july", "august", "september"]},
                              "march"),
                ["spinach", "garlic"]
            ],
            'Arguments used: {"spinach":["february","march"], "garlic":["february","march","april"], "eggplant":'
            '["july","august","september"]}, "december"': [
                sowing_season({"spinach": ["february", "march"],
                               "garlic": ["february", "march", "april"],
                               "eggplant": ["july", "august", "september"]},
                              "december"),
                []
            ],
            'Arguments used: {"spinach":["february","march"], "garlic":["february","march","april"], "eggplant":'
            '["july","august","september"]}, "august"': [
                sowing_season({"spinach": ["february", "march"],
                               "garlic": ["february", "march", "april"],
                               "eggplant": ["july", "august", "september"]},
                              "august"),
                ['eggplant']
            ],
            'Arguments used: ({}, "march")': [
                sowing_season({}, "march"),
                []
            ],
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_register_payment(self):
        test_cases = {
            'Arguments used: {423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, 289': [
                register_payment({423: ["Darlene Johnson", 4523114, True],
                                  289: ["Anna Brown", 6345112, False],
                                  657: ["Steven Lloyd", 4767992, False]},
                                 289),
                {423: ["Darlene Johnson", 4523114, True],
                 289: ["Anna Brown", 6345112, True],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Arguments used: {423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, 423': [
                register_payment({423: ["Darlene Johnson", 4523114, True],
                                  289: ["Anna Brown", 6345112, False],
                                  657: ["Steven Lloyd", 4767992, False]},
                                 423),
                {423: ["Darlene Johnson", 4523114, True],
                 289: ["Anna Brown", 6345112, False],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Arguments used: {423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, 158': [
                register_payment({423: ["Darlene Johnson", 4523114, True],
                                  289: ["Anna Brown", 6345112, False],
                                  657: ["Steven Lloyd", 4767992, False]},
                                 158),
                {423: ["Darlene Johnson", 4523114, True],
                 289: ["Anna Brown", 6345112, False],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Arguments used: {}, 289': [
                register_payment({}, 289),
                {}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_late_payments(self):
        test_cases = {
            'Argument used: {423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}': [
                late_payments({423: ["Darlene Johnson", 4523114, True],
                               289: ["Anna Brown", 6345112, False],
                               657: ["Steven Lloyd", 4767992, False]}),
                2
            ],
            'Argument used: {423:["Darlene Johnson", 4523114, False], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}': [
                late_payments({423: ["Darlene Johnson", 4523114, False],
                               289: ["Anna Brown", 6345112, False],
                               657: ["Steven Lloyd", 4767992, False]}),
                3
            ],
            'Argument used: {423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, True], 657:'
            '["Steven Lloyd", 4767992, True]}': [
                late_payments({423: ["Darlene Johnson", 4523114, True],
                               289: ["Anna Brown", 6345112, True],
                               657: ["Steven Lloyd", 4767992, True]}),
                0
            ],
            'Argument used: {}': [
                late_payments({}),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_delete_member(self):
        test_cases = {
            'Arguments used: {423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, "Anna Brown"': [
                delete_member({423: ["Darlene Johnson", 4523114, True],
                               289: ["Anna Brown", 6345112, False],
                               657: ["Steven Lloyd", 4767992, False]}, "Anna Brown"),
                {423: ["Darlene Johnson", 4523114, True],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Argument used: {423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, "Lucia Perez': [
                delete_member({423: ["Darlene Johnson", 4523114, True],
                               289: ["Anna Brown", 6345112, False],
                               657: ["Steven Lloyd", 4767992, False]}, "Lucia Perez"),
                {423: ["Darlene Johnson", 4523114, True],
                 289: ["Anna Brown", 6345112, False],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Argument used: {}, "Anna Brown"': [
                delete_member({}, "Anna Brown"),
                {}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_roman_to_arabic(self):
        test_cases = {
            'Argument used: MCMLXXIV': [
                roman_to_arabic("MCMLXXIV"),
                1974
            ],
            'Argument used: I': [
                roman_to_arabic("I"),
                1
            ],
            'Argument used: V': [
                roman_to_arabic("V"),
                5
            ],
            'Argument used: X': [
                roman_to_arabic("X"),
                10
            ],
            'Argument used: L': [
                roman_to_arabic("L"),
                50
            ],
            'Argument used: C': [
                roman_to_arabic("C"),
                100
            ],
            'Argument used: D': [
                roman_to_arabic("D"),
                500
            ],
            'Argument used: M': [
                roman_to_arabic("M"),
                1000
            ],
            'Argument used: MMMCMXCIX': [
                roman_to_arabic("MMMCMXCIX"),
                3999
            ],
            'Argument used: III': [
                roman_to_arabic("III"),
                3
            ],
            'Argument used: IV': [
                roman_to_arabic("IV"),
                4
            ],
            'Argument used: IX': [
                roman_to_arabic("IX"),
                9
            ],
            'Argument used: XL': [
                roman_to_arabic("XL"),
                40
            ],
            'Argument used: XC': [
                roman_to_arabic("XC"),
                90
            ],
            'Argument used: CD': [
                roman_to_arabic("CD"),
                400
            ],
            'Argument used: CM': [
                roman_to_arabic("CM"),
                900
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_phone_number(self):
        test_cases = {
            'Argument used: "(325)444-TEST"': [
                phone_number("(325)444-TEST"),
                "(325)444-8378"
            ],
            'Argument used: "435-224-7613"': [
                phone_number("(325)444-TEST"),
                "(325)444-8378"
            ],
            'Argument used: "54212456"': [
                phone_number("54212456"),
                "54212456"
            ],
            'Argument used: "0800-TEST"': [
                phone_number("0800-TEST"),
                "0800-8378"
            ],
            'Argument used: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"': [
                phone_number("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                "22233344455566677778889999"
            ],
            'Argument used: "(325)444TEST"': [
                phone_number("(325)444TEST"),
                "(325)4448378"
            ],
            'Argument used: "(325)444-8378"': [
                phone_number("(325)444-8378"),
                "(325)444-8378"
            ],
            'Argument used: "(TEST)444-12345"': [
                phone_number("(TEST)444-12345"),
                "(8378)444-12345"
            ],
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_isomorphic_strings(self):
        test_cases = {
            'Arguments used: "paper", "title"': [
                isomorphic_strings("paper", "title"),
                True
            ],
            'Arguments used: "paper", "yoyos"': [
                isomorphic_strings("paper", "yoyos"),
                False
            ],
            'Arguments used: "abcd", "efgh"': [
                isomorphic_strings("abcd", "efgh"),
                True
            ],
            'Arguments used: "aaa", "bbb"': [
                isomorphic_strings("aaa", "bbb"),
                True
            ],
            'Arguments used: "abb", "baa"': [
                isomorphic_strings("abb", "baa"),
                True
            ],
            'Arguments used: "badc", "baba"': [
                isomorphic_strings("badc", "baba"),
                False
            ],
            'Arguments used: "z", "z"': [
                isomorphic_strings("z", "z"),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)
