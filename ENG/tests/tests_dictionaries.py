###########################
# DO NOT MODIFY THIS FILE #
###########################

import unittest
from ENG.src.dictionaries import *


class TestsSetDictionaryFunctions(unittest.TestCase):

    def test_find_duplicates(self):
        test_cases = {
            'Arguments used: strings1=["abc", "cde", "abc", "fff"], strings2=["cde", "aaa"]': [
                find_duplicates(strings1=["abc", "cde", "abc", "fff"], strings2=["cde", "aaa"]),
                {"cde"}
            ],
            'Arguments used: strings1=["abc", "cde", "fgh", "ijk"], strings2=["fgh", "abc"]': [
                find_duplicates(strings1=["abc", "cde", "fgh", "ijk"], strings2=["fgh", "abc"]),
                {"abc", "fgh"}
            ],
            'Arguments used: strings1=["abc", "cde"], strings2=["fgh", "ijk"]': [
                find_duplicates(strings1=["abc", "cde"], strings2=["fgh", "ijk"]),
                set()
            ],
            'Arguments used: strings1=["abc"], strings2=["abc"]': [
                find_duplicates(strings1=["abc"], strings2=["abc"]),
                {"abc"}
            ],
            'Arguments used: strings1=[], strings2=[]': [
                find_duplicates(strings1=[], strings2=[]),
                set()
            ],
            'Arguments used: strings1=["abc", "cde", "abc", "fff"], strings2=[]': [
                find_duplicates(strings1=["abc", "cde", "abc", "fff"], strings2=[]),
                set()
            ],
            'Arguments used: strings1=[], strings2=["abc", "cde", "abc", "fff"]': [
                find_duplicates(strings1=[], strings2=["abc", "cde", "abc", "fff"]),
                set()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_only_one_pet_type(self):
        test_cases = {
            'Arguments used: dogs=["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"],'
            'cats=["John Sebastian Batch", "Jon Jack Russo", "Anna Bologna", "Christopher Colum"]': [
                only_one_pet_type(dogs=["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"],
                                  cats=["John Sebastian Batch", "Jon Jack Russo", "Anna Bologna", "Christopher Colum"]),
                {"Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"}
            ],
            'Arguments used: dogs=["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"], cats=["Jon Jack '
            'Russo", "Anna Bologna"]': [
                only_one_pet_type(dogs=["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"],
                                  cats=["Jon Jack Russo", "Anna Bologna"]),
                {"Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum", "Jon Jack Russo", "Anna Bologna"}
            ],
            'Arguments used: dogs=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"], cats=["Lucrezia Georgia",'
            '"Jon Jack Russo", "Anna Bologna"]': [
                only_one_pet_type(dogs=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"],
                                  cats=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"]),
                set()
            ],
            'Arguments used: dogs=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"], cats=["Lucrezia Georgia",'
            '"Jon Jack Russo"]': [
                only_one_pet_type(dogs=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"],
                                  cats=["Lucrezia Georgia", "Jon Jack Russo"]),
                {"Anna Bologna"}
            ],
            'Arguments used: dogs=["Lucrezia Georgia", "Jon Jack Russo"], cats=["Lucrezia Georgia", "Jon Jack Russo",'
            '"Anna Bologna"]': [
                only_one_pet_type(dogs=["Lucrezia Georgia", "Jon Jack Russo"],
                                  cats=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"]),
                {"Anna Bologna"}
            ],
            'Arguments used: dogs=[], cats=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"]': [
                only_one_pet_type(dogs=[],
                                  cats=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"]),
                {"Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"}
            ],
            'Arguments used: dogs=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"], cats=[]': [
                only_one_pet_type(dogs=["Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"],
                                  cats=[]),
                {"Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_unique_elements(self):
        test_cases = {
            'Argument used: tuples=[(1,2,3), (2,2,2,2), (3,4,5), (1,3,5,7,9)]': [
                unique_elements(tuples=[(1, 2, 3), (2, 2, 2, 2), (3, 4, 5), (1, 3, 5, 7, 9)]),
                (1, 2, 3, 4, 5, 7, 9)
            ],
            'Argument used: tuples=[(1,2,3), (1,2,3), (1,2,3)]': [
                unique_elements(tuples=[(1, 2, 3), (1, 2, 3), (1, 2, 3)]),
                (1, 2, 3)
            ],
            'Argument used: tuples=[(1,2,3)]': [
                unique_elements(tuples=[(1, 2, 3)]),
                (1, 2, 3)
            ],
            'Argument used: tuples=[(1,2,3), (4,5,6), (7,8,9)]': [
                unique_elements(tuples=[(1, 2, 3), (4, 5, 6), (7, 8, 9)]),
                (1, 2, 3, 4, 5, 6, 7, 8, 9)
            ],
            'Argument used: tuples=[(1,1,1), (1,1,1), (1,1,1)]': [
                unique_elements(tuples=[(1, 1, 1), (1, 1, 1), (1, 1, 1)]),
                (1,)
            ],
            'Argument used: tuples=[]': [
                unique_elements(tuples=[]),
                ()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_unique_last_names(self):
        test_cases = {
            'Argument used: students=["Maude Baker", "Milton Llewellyn Davis", "Leela Evans", "Keelan Davis"]': [
                unique_last_names(students=["Maude Baker", "Milton Llewellyn Davis", "Leela Evans", "Keelan Davis"]),
                {"Baker", "Davis", "Evans"}
            ],
            'Argument used: students=["Maude Baker", "Milton Llewellyn Davis", "Leela Evans"]': [
                unique_last_names(students=["Maude Baker", "Milton Llewellyn Davis", "Leela Evans"]),
                {"Baker", "Davis", "Evans"}
            ],
            'Argument used: students=["Maude Baker", "Milton Llewellyn Baker", "Leela Baker", "Keelan Baker"]': [
                unique_last_names(students=["Maude Baker", "Milton Llewellyn Baker", "Leela Baker", "Keelan Baker"]),
                {"Baker"}
            ],
            'Argument used: students=[]': [
                unique_last_names(students=[]),
                set()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_billing_addresses(self):
        test_cases = {
            'Argument used: sales=[("Stephan Carey", 5, 1250.23, "355 Boulevard St."), ("Jocelyn Harris", 7, 699,'
            '"218 Main St."), ("Stephan Carey", 7, 532.90, "355 Boulevard St."), ("Frances Adams", 12, 57.99, '
            '"761 South Rd."), ("Jocelyn Harris", 15, 958, "218 Main St.")]': [
                billing_addresses(sales=[("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                                         ("Jocelyn Harris", 7, 699, "218 Main St."),
                                         ("Stephan Carey", 7, 532.90, "355 Boulevard St."),
                                         ("Frances Adams", 12, 57.99, "761 South Rd."),
                                         ("Jocelyn Harris", 15, 958, "218 Main St.")]),
                {'355 Boulevard St.', '218 Main St.', '761 South Rd.'}
            ],
            'Argument used: sales=[("Stephan Carey", 5, 1250.23, "355 Boulevard St."), ("Jocelyn Harris", 7, 699, '
            '"218 Main St."), ("Frances Adams", 12, 57.99, "761 South Rd.")]': [
                billing_addresses(sales=[("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                                         ("Jocelyn Harris", 7, 699, "218 Main St."),
                                         ("Frances Adams", 12, 57.99, "761 South Rd.")]),
                {'355 Boulevard St.', '218 Main St.', '761 South Rd.'}
            ],
            'Argument used: sales=[("Stephan Carey", 5, 1250.23, "355 Boulevard St."), ("Stephan Carey", 5, 1250.23, '
            '"355 Boulevard St."), ("Stephan Carey", 5, 1250.23, "355 Boulevard St.")]': [
                billing_addresses(sales=[("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                                         ("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                                         ("Stephan Carey", 5, 1250.23, "355 Boulevard St.")]),
                {'355 Boulevard St.'}
            ],
            'Argument used: sales=[]': [
                billing_addresses(sales=[]),
                set()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_add_movie(self):
        test_cases = {
            'Arguments used: movies={"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]},'
            'movie=("Lord of the rings: The two towers", "Peter Jackson", 2002)': [
                add_movie(movies={"Joker": ["Todd Phillips", 2019],
                                  "Avatar": ["James Cameron", 2009]},
                          movie=("Lord of the rings: The two towers", "Peter Jackson", 2002)),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009],
                 "Lord of the rings: The two towers": ["Peter Jackson", 2002]}
            ],
            'Arguments used: movies={}, movie=("Lord of the rings: The two towers", "Peter Jackson", 2002)': [
                add_movie(movies={},
                          movie=("Lord of the rings: The two towers", "Peter Jackson", 2002)),
                {"Lord of the rings: The two towers": ["Peter Jackson", 2002]}
            ],
            'Arguments used: movies={"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]},'
            'movie=("Avatar", "James Cameron", 2009)': [
                add_movie(movies={"Joker": ["Todd Phillips", 2019],
                                  "Avatar": ["James Cameron", 2009]},
                          movie=("Avatar", "James Cameron", 2009)),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}
            ],
            'Arguments used: movies={"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, movie=()': [
                add_movie(movies={"Joker": ["Todd Phillips", 2019],
                                  "Avatar": ["James Cameron", 2009]},
                          movie=()),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_most_voted(self):
        test_cases = {
            'Arguments used: votes={1:["john","john","laura","john","laura","paula"], 2:["amy","sean","olivia",'
            '"olivia"], 3:["liam","sophie","liam","sophie","sophie","isabella","sophie"]}, grade=3': [
                most_voted(votes={1: ["john", "john", "laura", "john", "laura", "paula"],
                                  2: ["amy", "sean", "olivia", "olivia"],
                                  3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                           grade=3),
                {"liam", "sophie", "isabella"}
            ],
            'Arguments used: votes={1:["john","laura","paula"], 2:["amy","sean","olivia","olivia"], '
            '3:["liam","sophie","liam","sophie","sophie","isabella","sophie"]}, grade=1': [
                most_voted(votes={1: ["john", "laura", "paula"], 2: ["amy", "sean", "olivia", "olivia"],
                                  3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                           grade=1),
                {"john", "laura", "paula"}
            ],
            'Arguments used: votes={1:["laura","laura","laura","laura"], 2:["amy","sean","olivia","olivia"], '
            '3:["liam","sophie","liam","sophie","sophie","isabella","sophie"]}, grade=1': [
                most_voted(votes={1: ["laura", "laura", "laura", "laura"], 2: ["amy", "sean", "olivia", "olivia"],
                                  3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                           grade=1),
                {"laura"}
            ],
            'Arguments used: votes={1:["john","john","laura","john","laura","paula"], 2:["amy","sean","olivia",'
            '"olivia"], 3:["liam","sophie","liam","sophie","sophie","isabella","sophie"]}, grade=4': [
                most_voted(votes={1: ["john", "john", "laura", "john", "laura", "paula"],
                                  2: ["amy", "sean", "olivia", "olivia"],
                                  3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                           grade=4),
                set()
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_digit_occurrence(self):
        test_cases = {
            'Argument used: digits=[8, 9, 0, 4, 2, 2, 4, 1, 8, 2]': [
                digit_occurrence(digits=[8, 9, 0, 4, 2, 2, 4, 1, 8, 2]),
                {0: 1, 1: 1, 2: 3, 3: 0, 4: 2, 5: 0, 6: 0, 7: 0, 8: 2, 9: 1}
            ],
            'Argument used: digits=[0, 0, 0, 0, 0, 0]': [
                digit_occurrence(digits=[0, 0, 0, 0, 0, 0]),
                {0: 6, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            ],
            'Argument used: digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]': [
                digit_occurrence(digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
            ],
            'Argument used: digits=[]': [
                digit_occurrence(digits=[]),
                {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_count_occurrences(self):
        test_cases = {
            'Argument used: lists_tuple=(["i", "%", "u"], ["^", "%", "^", "s", "i", "i", "u"], ["a", "u"])': [
                count_occurrences(lists_tuple=(["i", "%", "u"], ["^", "%", "^", "s", "i", "i", "u"], ["a", "u"])),
                {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
            ],
            'Argument used: lists_tuple=(["i", "%", "u", "^", "%", "^", "s", "i", "i", "u", "a", "u"])': [
                count_occurrences(lists_tuple=(["i", "%", "u", "^", "%", "^", "s", "i", "i", "u", "a", "u"])),
                {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
            ],
            'Argument used: lists_tuple=(["i", "%", "u"], ["i", "%", "u"], ["i", "%", "u"])': [
                count_occurrences(lists_tuple=(["i", "%", "u"], ["i", "%", "u"], ["i", "%", "u"])),
                {'i': 3, '%': 3, 'u': 3}
            ],
            'Argument used: lists_tuple=(["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"])': [
                count_occurrences(lists_tuple=(["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"])),
                {'i': 12}
            ],
            'Argument used: lists_tuple=([], [], [], [], [])': [
                count_occurrences(lists_tuple=([], [], [], [], [])),
                {}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_highest_value(self):
        test_cases = {
            'Arguments used: occurrences={"a":1, "e":7, "i":4, "o":9, "u":3}': [
                highest_value(occurrences={"a": 1, "e": 7, "i": 4, "o": 9, "u": 3}),
                "o"
            ],
            'Arguments used: occurrences={"z":198}': [
                highest_value(occurrences={"z": 198}),
                "z"
            ],
            'Arguments used: occurrences={}': [
                highest_value(occurrences={}),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_sowing_season(self):
        test_cases = {
            'Arguments used: vegetables={"spinach":["february","march"], "garlic":["february","march","april"], '
            '"eggplant":["july","august","september"]}, month="march"': [
                sowing_season(vegetables={"spinach": ["february", "march"],
                                          "garlic": ["february", "march", "april"],
                                          "eggplant": ["july", "august", "september"]},
                              month="march"),
                ["spinach", "garlic"]
            ],
            'Arguments used: vegetables={"spinach":["february","march"], "garlic":["february","march","april"], '
            '"eggplant":["july","august","september"]}, month="december"': [
                sowing_season(vegetables={"spinach": ["february", "march"],
                                          "garlic": ["february", "march", "april"],
                                          "eggplant": ["july", "august", "september"]},
                              month="december"),
                []
            ],
            'Arguments used: vegetables={"spinach":["february","march"], "garlic":["february","march","april"], '
            '"eggplant":["july","august","september"]}, month="august"': [
                sowing_season(vegetables={"spinach": ["february", "march"],
                                          "garlic": ["february", "march", "april"],
                                          "eggplant": ["july", "august", "september"]},
                              month="august"),
                ['eggplant']
            ],
            'Arguments used: (vegetables={}, month="march")': [
                sowing_season(vegetables={},
                              month="march"),
                []
            ],
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_register_payment(self):
        test_cases = {
            'Arguments used: members={423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, number=289': [
                register_payment(members={423: ["Darlene Johnson", 4523114, True],
                                          289: ["Anna Brown", 6345112, False],
                                          657: ["Steven Lloyd", 4767992, False]},
                                 number=289),
                {423: ["Darlene Johnson", 4523114, True],
                 289: ["Anna Brown", 6345112, True],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Arguments used: members={423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, number=423': [
                register_payment(members={423: ["Darlene Johnson", 4523114, True],
                                          289: ["Anna Brown", 6345112, False],
                                          657: ["Steven Lloyd", 4767992, False]},
                                 number=423),
                {423: ["Darlene Johnson", 4523114, True],
                 289: ["Anna Brown", 6345112, False],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Arguments used: members={423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, number=158': [
                register_payment(members={423: ["Darlene Johnson", 4523114, True],
                                          289: ["Anna Brown", 6345112, False],
                                          657: ["Steven Lloyd", 4767992, False]},
                                 number=158),
                {423: ["Darlene Johnson", 4523114, True],
                 289: ["Anna Brown", 6345112, False],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Arguments used: members={}, number=289': [
                register_payment(members={}, number=289),
                {}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_late_payments(self):
        test_cases = {
            'Argument used: members={423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}': [
                late_payments(members={423: ["Darlene Johnson", 4523114, True],
                                       289: ["Anna Brown", 6345112, False],
                                       657: ["Steven Lloyd", 4767992, False]}),
                2
            ],
            'Argument used: members={423:["Darlene Johnson", 4523114, False], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}': [
                late_payments(members={423: ["Darlene Johnson", 4523114, False],
                                       289: ["Anna Brown", 6345112, False],
                                       657: ["Steven Lloyd", 4767992, False]}),
                3
            ],
            'Argument used: members={423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, True], 657:'
            '["Steven Lloyd", 4767992, True]}': [
                late_payments(members={423: ["Darlene Johnson", 4523114, True],
                                       289: ["Anna Brown", 6345112, True],
                                       657: ["Steven Lloyd", 4767992, True]}),
                0
            ],
            'Argument used: members={}': [
                late_payments(members={}),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_delete_member(self):
        test_cases = {
            'Arguments used: members={423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, member_name="Anna Brown"': [
                delete_member(members={423: ["Darlene Johnson", 4523114, True],
                                       289: ["Anna Brown", 6345112, False],
                                       657: ["Steven Lloyd", 4767992, False]},
                              member_name="Anna Brown"),
                {423: ["Darlene Johnson", 4523114, True],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Argument used: members={423:["Darlene Johnson", 4523114, True], 289:["Anna Brown", 6345112, False], 657:'
            '["Steven Lloyd", 4767992, False]}, member_name="Lucia Perez': [
                delete_member(members={423: ["Darlene Johnson", 4523114, True],
                                       289: ["Anna Brown", 6345112, False],
                                       657: ["Steven Lloyd", 4767992, False]},
                              member_name="Lucia Perez"),
                {423: ["Darlene Johnson", 4523114, True],
                 289: ["Anna Brown", 6345112, False],
                 657: ["Steven Lloyd", 4767992, False]}
            ],
            'Argument used: members={}, member_name="Anna Brown"': [
                delete_member(members={},
                              member_name="Anna Brown"),
                {}
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_roman_to_arabic(self):
        test_cases = {
            'Argument used: roman="MCMLXXIV"': [
                roman_to_arabic(roman="MCMLXXIV"),
                1974
            ],
            'Argument used: roman="I"': [
                roman_to_arabic(roman="I"),
                1
            ],
            'Argument used: roman="V"': [
                roman_to_arabic(roman="V"),
                5
            ],
            'Argument used: roman="X"': [
                roman_to_arabic(roman="X"),
                10
            ],
            'Argument used: roman="L"': [
                roman_to_arabic(roman="L"),
                50
            ],
            'Argument used: roman="C"': [
                roman_to_arabic(roman="C"),
                100
            ],
            'Argument used: roman="D"': [
                roman_to_arabic(roman="D"),
                500
            ],
            'Argument used: roman="M"': [
                roman_to_arabic(roman="M"),
                1000
            ],
            'Argument used: roman="MMMCMXCIX"': [
                roman_to_arabic(roman="MMMCMXCIX"),
                3999
            ],
            'Argument used: roman="III"': [
                roman_to_arabic(roman="III"),
                3
            ],
            'Argument used: roman="IV"': [
                roman_to_arabic(roman="IV"),
                4
            ],
            'Argument used: roman="IX"': [
                roman_to_arabic(roman="IX"),
                9
            ],
            'Argument used: roman="XL"': [
                roman_to_arabic(roman="XL"),
                40
            ],
            'Argument used: roman="XC"': [
                roman_to_arabic(roman="XC"),
                90
            ],
            'Argument used: roman="CD"': [
                roman_to_arabic(roman="CD"),
                400
            ],
            'Argument used: roman="CM"': [
                roman_to_arabic(roman="CM"),
                900
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_phone_number(self):
        test_cases = {
            'Argument used: phone="(325)444-TEST"': [
                phone_number(phone="(325)444-TEST"),
                "(325)444-8378"
            ],
            'Argument used: phone="435-224-7613"': [
                phone_number(phone="(325)444-TEST"),
                "(325)444-8378"
            ],
            'Argument used: phone="54212456"': [
                phone_number(phone="54212456"),
                "54212456"
            ],
            'Argument used: phone="0800-TEST"': [
                phone_number(phone="0800-TEST"),
                "0800-8378"
            ],
            'Argument used: phone="ABCDEFGHIJKLMNOPQRSTUVWXYZ"': [
                phone_number(phone="ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                "22233344455566677778889999"
            ],
            'Argument used: phone="(325)444TEST"': [
                phone_number(phone="(325)444TEST"),
                "(325)4448378"
            ],
            'Argument used: phone="(325)444-8378"': [
                phone_number(phone="(325)444-8378"),
                "(325)444-8378"
            ],
            'Argument used: phone="(TEST)444-12345"': [
                phone_number(phone="(TEST)444-12345"),
                "(8378)444-12345"
            ],
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_isomorphic_strings(self):
        test_cases = {
            'Arguments used: string1="paper", string2="title"': [
                isomorphic_strings(string1="paper", string2="title"),
                True
            ],
            'Arguments used: string1="paper", string2="yoyos"': [
                isomorphic_strings(string1="paper", string2="yoyos"),
                False
            ],
            'Arguments used: string1="abcd", string2="efgh"': [
                isomorphic_strings(string1="abcd", string2="efgh"),
                True
            ],
            'Arguments used: string1="aaa", string2="bbb"': [
                isomorphic_strings(string1="aaa", string2="bbb"),
                True
            ],
            'Arguments used: string1="abb", string2="baa"': [
                isomorphic_strings(string1="abb", string2="baa"),
                True
            ],
            'Arguments used: string1="badc", string2="baba"': [
                isomorphic_strings(string1="badc", string2="baba"),
                False
            ],
            'Arguments used: string1="z", string2="z"': [
                isomorphic_strings(string1="z", string2="z"),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_word_pattern(self):
        test_cases = {
            'Arguments used: pattern="xyyx", words="home sea sea home"': [
                word_pattern(pattern="xyyx", words="home sea sea home"),
                True
            ],
            'Arguments used: pattern="xyyx", words="home sea sea hill"': [
                word_pattern(pattern="xyyx", words="home sea sea hill"),
                False
            ],
            'Arguments used: pattern="xxxxx", words="dog"': [
                word_pattern(pattern="xxxxx", words="dog"),
                False
            ],
            'Arguments used: pattern="x", words="home home home home"': [
                word_pattern(pattern="x", words="home home home home"),
                False
            ],
            'Arguments used: pattern="xxx", words="home home home"': [
                word_pattern(pattern="xxx", words="home home home"),
                True
            ],
            'Arguments used: pattern="xy", words="home sea"': [
                word_pattern(pattern="xy", words="home sea"),
                True
            ],
            'Arguments used: pattern="x", words="home"': [
                word_pattern(pattern="x", words="home"),
                True
            ],
            'Arguments used: pattern="", words="dog"': [
                word_pattern(pattern="", words="dog"),
                False
            ],
            'Arguments used: pattern="xyxy", words=""': [
                word_pattern(pattern="xyxy", words=""),
                False
            ],
            'Arguments used: pattern="", words=""': [
                word_pattern(pattern="", words=""),
                False
            ],
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)
