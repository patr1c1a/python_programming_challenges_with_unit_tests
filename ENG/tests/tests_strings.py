###########################
# DO NOT MODIFY THIS FILE #
###########################

import unittest
from ENG.src.strings import *


class TestsStringFunctions(unittest.TestCase):

    def test_has_even_amount_chars(self):
        test_cases = {
            'Arguments used: s1="aaaa", s2="aaaa"': [
                has_even_amount_chars(s1="aaaa", s2="aaaa"),
                True
            ],
            'Arguments used: s1="aaa", s2="aaaa"': [
                has_even_amount_chars(s1="aaa", s2="aaaa"),
                False
            ],
            'Arguments used: s1="aaa", s2="aaa"': [
                has_even_amount_chars(s1="aaa", s2="aaa"),
                False
            ],
            'Arguments used: s1="aaaa", s2="aaa"': [
                has_even_amount_chars(s1="aaaa", s2="aaa"),
                False
            ],
            'Arguments used: s1="", s2="aaaa"': [
                has_even_amount_chars(s1="", s2="aaaa"),
                True
            ],
            'Arguments used: s1="aaaa", s2=""': [
                has_even_amount_chars(s1="aaaa", s2=""),
                True
            ],
            'Arguments used: s1="", s2=""': [
                has_even_amount_chars(s1="", s2=""),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_count_occurrences(self):
        test_cases = {
            'Arguments used: s="This is an example sentence", character="s"': [
                count_occurrences(s="This is an example sentence", character="s"),
                3
            ],
            'Arguments used: s="This is an example sentence", character="T"': [
                count_occurrences(s="This is an example sentence", character="T"),
                1
            ],
            'Arguments used: s="This is an example sentence", character="z"': [
                count_occurrences(s="This is an example sentence", character="z"),
                0
            ],
            'Arguments used: s="This is an example sentence", character="i"': [
                count_occurrences(s="This is an example sentence", character="i"),
                2
            ],
            'Arguments used: s="", character="a"': [
                count_occurrences(s="", character="a"),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_count_vowels(self):
        test_cases = {
            'Argument used: s="This is an Example Sentence"': [
                count_vowels(s="This is an Example Sentence"),
                9
            ],
            'Argument used: s="aeiou"': [
                count_vowels(s="aeiou"),
                5
            ],
            'Argument used: s="AEIOU"': [
                count_vowels(s="AEIOU"),
                5
            ],
            'Argument used: s="abcdEfgHijkLMnOPqrsTuVwXyz"': [
                count_vowels(s="abcdEfgHijkLMnOPqrsTuVwXyz"),
                5
            ],
            'Argument used: s="zzz"': [
                count_vowels(s="zzz"),
                0
            ],
            'Argument used: s="123"': [
                count_vowels(s="123"),
                0
            ],
            'Argument used: s=""': [
                count_vowels(s=""),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_count_unique_vowels(self):
        test_cases = {
            'Argument used: s="This is an Example Sentence"': [
                count_unique_vowels(s="This is an Example Sentence"),
                3
            ],
            'Argument used: s="aeiou"': [
                count_unique_vowels(s="aeiou"),
                5
            ],
            'Argument used: s="aeiouAEIOU"': [
                count_unique_vowels(s="aeiouAEIOU"),
                5
            ],
            'Argument used: s="aaeeiioouuAAEEIIOOUU"': [
                count_unique_vowels(s="aeiouAEIOU"),
                5
            ],
            'Argument used: s="abcdEfgHijkLMnOPqrsTuVwXyz"': [
                count_unique_vowels(s="abcdEfgHijkLMnOPqrsTuVwXyz"),
                5
            ],
            'Argument used: s="zzz"': [
                count_unique_vowels(s="zzz"),
                0
            ],
            'Argument used: s="123"': [
                count_unique_vowels(s="123"),
                0
            ],
            'Argument used: s=""': [
                count_unique_vowels(s=""),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_replace_character_w_asterisk(self):
        test_cases = {
            'Arguments used: s="this is an example sentence", character="e"': [
                replace_character_w_asterisk(s="this is an example sentence", character="e"),
                "this is an *xampl* s*nt*nc*"
            ],
            'Arguments used: s="this is an example sentence", character="x"': [
                replace_character_w_asterisk(s="this is an example sentence", character="x"),
                "this is an e*ample sentence"
            ],
            'Arguments used: s="This is an example sentence", character="T"': [
                replace_character_w_asterisk(s="This is an example sentence", character="T"),
                "*his is an example sentence"
            ],
            'Arguments used: s="this is an example sentence", character="z"': [
                replace_character_w_asterisk(s="this is an example sentence", character="z"),
                "this is an example sentence"
            ],
            'Arguments used: s="this is an example sentence", character=""': [
                replace_character_w_asterisk(s="this is an example sentence", character=""),
                "this is an example sentence"
            ],
            'Arguments used: s="", character="a"': [
                replace_character_w_asterisk(s="", character="a"),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_reverse_string(self):
        test_cases = {
            'Argument used: s="This is an example sentence!"': [
                reverse_string(s="This is an example sentence!"),
                "!ecnetnes elpmaxe na si sihT"
            ],
            'Argument used: s="aaaa"': [
                reverse_string(s="aaaa"),
                "aaaa"
            ],
            'Argument used: s="a"': [
                reverse_string(s="a"),
                "a"
            ],
            'Argument used: s=""': [
                reverse_string(s=""),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_replace_symbols(self):
        test_cases = {
            'Arguments used: s="--This is 1 example sentence and we\'ll replace the @ symbol", new_character="@"': [
                replace_symbols(s="--This is 1 example sentence and we'll replace the @ symbol", new_character="@"),
                "@@This is 1 example sentence and we@ll replace the @ symbol"
            ],
            'Arguments used: s="This is an example sentence", new_character="*"': [
                replace_symbols(s="This is an example sentence", new_character="*"),
                "This is an example sentence"
            ],
            'Arguments used: s="This is an example sentence!", new_character="-"': [
                replace_symbols(s="This is an example sentence!", new_character="-"),
                "This is an example sentence-"
            ],
            'Arguments used: s="/$This/ is@ an# example= sentence*", new_character="@"': [
                replace_symbols(s="/$This/ is@ an# example= sentence*", new_character="@"),
                "@@This@ is@ an@ example@ sentence@"
            ],
            'Arguments used: s="1234", new_character="}"': [
                replace_symbols(s="1234", new_character="}"),
                "1234"
            ],
            'Arguments used: s="@@@", new_character="@"': [
                replace_symbols(s="@@@", new_character="@"),
                "@@@"
            ],
            'Arguments used: s=" ", new_character="*"': [
                replace_symbols(s=" ", new_character="*"),
                " "
            ],
            'Arguments used: s="", new_character="*"': [
                replace_symbols(s="", new_character="*"),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_percentage_numerical_digits(self):
        test_cases = {
            'Argument used: s="This has 1 digit"': [
                percentage_numerical_digits(s="This has 1 digit"),
                6.25
            ],
            'Argument used: s="1984"': [
                percentage_numerical_digits(s="1984"),
                100
            ],
            'Argument used: s="This is an example sentence"': [
                percentage_numerical_digits(s="This is an example sentence"),
                0
            ],
            'Argument used: s=""': [
                percentage_numerical_digits(s=""),
                0
            ],
            'Argument used: s="abc1"': [
                percentage_numerical_digits(s="abc1"),
                25
            ],
            'Argument used: s="Literature: 95"': [
                percentage_numerical_digits(s="Literature: 95"),
                14.285714285714286
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_classify_numerical_string(self):
        test_cases = {
            'Argument used: s="123456"': [
                classify_numerical_string(s="123456"),
                "246$36"
            ],
            'Argument used: s="2222"': [
                classify_numerical_string(s="2222"),
                "2222$"
            ],
            'Argument used: s="1234567890"': [
                classify_numerical_string(s="1234567890"),
                "24680$3690"
            ],
            'Argument used: s="3333"': [
                classify_numerical_string(s="3333"),
                "$3333"
            ],
            'Argument used: s="6666"': [
                classify_numerical_string(s="6666"),
                "6666$6666"
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_middle_characters(self):
        test_cases = {
            'Argument used: s="AbcDefGhi"': [
                middle_characters(s="AbcDefGhi"),
                "Def"
            ],
            'Argument used: s="A   A"': [
                middle_characters(s="A   A"),
                "   "
            ],
            'Argument used: s="bAAAb"': [
                middle_characters(s="bAAAb"),
                "AAA"
            ],
            'Argument used: s="AAAAA"': [
                middle_characters(s="AAAAA"),
                "AAA"
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_palindrome(self):
        test_cases = {
            'Argument used: s="abba"': [
                is_palindrome(s="abba"),
                True
            ],
            'Argument used: s="baéceab"': [
                is_palindrome(s="baéceab"),
                False
            ],
            'Argument used: s="aba"': [
                is_palindrome(s="aba"),
                True
            ],
            'Argument used: s="aa"': [
                is_palindrome(s="aa"),
                True
            ],
            'Argument used: s="a"': [
                is_palindrome(s="a"),
                True
            ],
            'Argument used: s=""': [
                is_palindrome(s=""),
                False
            ],
            'Argument used: s="Aba"': [
                is_palindrome(s="Aba"),
                True
            ],
            'Argument used: s="ab"': [
                is_palindrome(s="ab"),
                False
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_contains_characters(self):
        test_cases = {
            'Arguments used: s1="super", s2="supermarket"': [
                contains_characters(s1="super", s2="supermarket"),
                True
            ],
            'Arguments used: s1="fff", s2="foo"': [
                contains_characters(s1="fff", s2="foo"),
                True
            ],
            'Arguments used: s1="alh", s2="alphabet"': [
                contains_characters(s1="alh", s2="alphabet"),
                True
            ],
            'Arguments used: s1="e", s2="cellular"': [
                contains_characters(s1="e", s2="cellular"),
                True
            ],
            'Arguments used: s1="alhc", s2="alphabet"': [
                contains_characters(s1="alhc", s2="alphabet"),
                False
            ],
            'Arguments used: s1="Lgh", s2="light"': [
                contains_characters(s1="Lgh", s2="light"),
                False
            ],
            'Arguments used: s1="Lgh", s2="Light"': [
                contains_characters(s1="Lgh", s2="Light"),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_anagram(self):
        test_cases = {
            'Arguments used: s1="below", s2="elbow"': [
                is_anagram(s1="below", s2="elbow"),
                True
            ],
            'Arguments used: s1="below", s2="elbows"': [
                is_anagram(s1="below", s2="elbows"),
                False
            ],
            'Arguments used: s1="aaa", s2="aaa"': [
                is_anagram(s1="aaa", s2="aaa"),
                True
            ],
            'Arguments used: s1="Aaa", s2="aaa"': [
                is_anagram(s1="aaa", s2="aaa"),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_how_many_remove_for_anagram(self):
        test_cases = {
            'Arguments used: s1="states", s2="tasted"': [
                how_many_remove_for_anagram(s1="states", s2="tasted"),
                2
            ],
            'Arguments used: s1="state", s2="taste"': [
                how_many_remove_for_anagram(s1="state", s2="taste"),
                0
            ],
            'Arguments used: s1="state", s2="tastes"': [
                how_many_remove_for_anagram(s1="state", s2="tastes"),
                1
            ],
            'Arguments used: s1="states", s2="taste"': [
                how_many_remove_for_anagram(s1="states", s2="taste"),
                1
            ],
            'Arguments used: s1="STATE", s2="untasted"': [
                how_many_remove_for_anagram(s1="STATE", s2="untasted"),
                3
            ],
            'Arguments used: s1="state", s2="TASTE"': [
                how_many_remove_for_anagram(s1="state", s2="TASTE"),
                0
            ],
            'Arguments used: s1="abc", s2="def"': [
                how_many_remove_for_anagram(s1="abc", s2="def"),
                6
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_reverse_words(self):
        test_cases = {
            'Arguments used: s="This is an example sentence."': [
                reverse_words(s="This is an example sentence."),
                "sihT si na elpmaxe .ecnetnes"
            ],
            'Arguments used: s="sihT si na elpmaxe !ecnetnes"': [
                reverse_words(s="sihT si na elpmaxe !ecnetnes"),
                "This is an example sentence!"
            ],
            'Arguments used: s="word"': [
                reverse_words(s="word"),
                "drow"
            ],
            'Arguments used: s="123"': [
                reverse_words(s="123"),
                "321"
            ],
            'Arguments used: s="a b c"': [
                reverse_words(s="a b c"),
                "a b c"
            ],
            'Arguments used: s=""': [
                reverse_words(s=""),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_length_last_word(self):
        test_cases = {
            'Argument used: s="This is an example sentence"': [
                length_last_word(s="This is an example sentence"),
                8
            ],
            'Argument used: s="   spaces   "': [
                length_last_word(s="   spaces   "),
                6
            ],
            'Argument used: s="word"': [
                length_last_word(s="word"),
                4
            ],
            'Argument used: s="   this   is   an   example   sentence   "': [
                length_last_word(s="   this   is   an   example   sentence   "),
                8
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_title_case(self):
        test_cases = {
            'Argument used: s="This is an example sentence"': [
                title_case(s="This is an example sentence"),
                "This Is An Example Sentence"
            ],
            'Argument used: s="THIS IS AN EXAMPLE SENTENCE"': [
                title_case(s="THIS IS AN EXAMPLE SENTENCE"),
                "This Is An Example Sentence"
            ],
            'Argument used: s="This Is An Example Sentence"': [
                title_case(s="This Is An Example Sentence"),
                "This Is An Example Sentence"
            ],
            'Argument used: s="word"': [
                title_case(s="word"),
                "Word"
            ],
            'Argument used: s="Word"': [
                title_case(s="Word"),
                "Word"
            ],
            'Argument used: s="    this is an example sentence"': [
                title_case(s="    this is an example sentence"),
                "    This Is An Example Sentence"
            ],
            'Argument used: s="this is an example sentence   "': [
                title_case(s="this is an example sentence   "),
                "This Is An Example Sentence   "
            ],
            'Argument used: s="this   is   an   example   sentence"': [
                title_case(s="this   is   an   example   sentence"),
                "This   Is   An   Example   Sentence"
            ],
            'Argument used: s="1this 2is 3an 4example 5sentence"': [
                title_case(s="1this 2is 3an 4example 5sentence"),
                "1This 2Is 3An 4Example 5Sentence"
            ],
            'Argument used: s="this1 is2 an3 example4 sentence5"': [
                title_case(s="this1 is2 an3 example4 sentence5"),
                "This1 Is2 An3 Example4 Sentence5"
            ],
            'Argument used: s="t1h2i3s4 i1s2 a1n2 e1x2a3m4p5l6e7 s1e2n3t4e5n6c7e8"': [
                title_case(s="t1h2i3s4 i1s2 a1n2 e1x2a3m4p5l6e7 s1e2n3t4e5n6c7e8"),
                "T1h2i3s4 I1s2 A1n2 E1x2a3m4p5l6e7 S1e2n3t4e5n6c7e8"
            ],
            'Argument used: s="this_is_an_example_sentence"': [
                title_case(s="this_is_an_example_sentence"),
                "This_Is_An_Example_Sentence"
            ],
            'Argument used: s="They\'re my best friend\'s siblings"': [
                title_case(s="They're my best friend's siblings"),
                "They're My Best Friend's Siblings"
            ],
            'Argument used: s=""': [
                title_case(s=""),
                ""
            ],
            'Argument used: s=" "': [
                title_case(s=" "),
                " "
            ],
            'Argument used: s="123"': [
                title_case(s="123"),
                "123"
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_caesar_cipher(self):
        test_cases = {
            'Arguments used: s="this is an example sentence", n=2': [
                caesar_cipher(s="this is an example sentence", n=2),
                "vjku ku co gacñrng ugovgoeg"
            ],
            'Arguments used: s="abc123 xyz987!", n=4': [
                caesar_cipher(s="abc123 xyz987!", n=4),
                "efg123 cde987!"
            ],
            'Arguments used: s="this is an example sentence", n=6': [
                caesar_cipher(s="this is an example sentence", n=6),
                "anñy ñy gs kegrvqk yksaksik"
            ],
            'Arguments used: s="123", n=8': [
                caesar_cipher(s="123", n=8),
                "123"
            ],
            'Arguments used: s="this is an example sentence", n=26': [
                caesar_cipher(s="this is an example sentence", n=26),
                "this is an example sentence"
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_shift_n_characters(self):
        test_cases = {
            'Arguments used: s="This is an example sentence", n=9': [
                shift_n_characters(s="This is an example sentence", n=9),
                " sentenceThis is an example"
            ],
            'Arguments used: s="word", n=3': [
                shift_n_characters(s="word", n=3),
                "ordw"
            ],
            'Arguments used: s="word", n=11': [
                shift_n_characters(s="word", n=11),
                "ordw"
            ],
            'Arguments used: s="This is an example sentence", n=0': [
                shift_n_characters(s="This is an example sentence", n=0),
                "This is an example sentence"
            ],
            'Arguments used: s="word", n=4': [
                shift_n_characters(s="word", n=4),
                "word"
            ],
            'Arguments used: s="", n=5': [
                shift_n_characters(s="", n=5),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_encode_rle(self):
        test_cases = {
            'Argument used: s="aaabbc"': [
                encode_rle(s="aaabbc"),
                "a3b2c"
            ],
            'Argument used: s="abcde"': [
                encode_rle(s="abcde"),
                "abcde"
            ],
            'Argument used: s="abbccc"': [
                encode_rle(s="abbccc"),
                "ab2c3"
            ],
            'Argument used: s="a"': [
                encode_rle(s="a"),
                "a"
            ],
            'Argument used: s="aaaa"': [
                encode_rle(s="aaaa"),
                "a4"
            ],
            'Argument used: s="Aaaa"': [
                encode_rle(s="Aaaa"),
                "Aa3"
            ],
            'Argument used: s="a$bb&&&&&c"': [
                encode_rle(s="a$bb&&&&&c"),
                "a$b2&5c"
            ],
            'Argument used: s=""': [
                encode_rle(s=""),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)
