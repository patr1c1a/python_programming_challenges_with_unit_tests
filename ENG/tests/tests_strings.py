###########################
# DO NOT MODIFY THIS FILE #
###########################

import unittest
from ENG.src.strings import *


class TestsStringFunctions(unittest.TestCase):

    def test_has_even_amount_chars(self):
        test_cases = {
            'Arguments used: "aaaa", "aaaa"': [
                has_even_amount_chars("aaaa", "aaaa"),
                True
            ],
            'Arguments used: "aaa", "aaaa"': [
                has_even_amount_chars("aaa", "aaaa"),
                False
            ],
            'Arguments used: "aaa", "aaa"': [
                has_even_amount_chars("aaa", "aaa"),
                False
            ],
            'Arguments used: "aaaa", "aaa"': [
                has_even_amount_chars("aaaa", "aaa"),
                False
            ],
            'Arguments used: "" (empty string), "aaaa"': [
                has_even_amount_chars("", "aaaa"),
                True
            ],
            'Arguments used: "aaaa", ""': [
                has_even_amount_chars("aaaa", ""),
                True
            ],
            'Arguments used: "" (empty string), ""': [
                has_even_amount_chars("", ""),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_count_occurrences(self):
        test_cases = {
            'Arguments used: "This is an example sentence", "s"': [
                count_occurrences("This is an example sentence", "s"),
                3
            ],
            'Arguments used: "This is an example sentence", "T"': [
                count_occurrences("This is an example sentence", "T"),
                1
            ],
            'Arguments used: "This is an example sentence", "z"': [
                count_occurrences("This is an example sentence", "z"),
                0
            ],
            'Arguments used: "This is an example sentence", "i"': [
                count_occurrences("This is an example sentence", "i"),
                2
            ],
            'Arguments used: "" (empty string), "a"': [
                count_occurrences("", "a"), 0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_count_vowels(self):
        test_cases = {
            'Argument used: "This is an Example Sentence"': [
                count_vowels("This is an Example Sentence"),
                9
            ],
            'Argument used: "aeiou"': [
                count_vowels("aeiou"),
                5
            ],
            'Argument used: "AEIOU"': [
                count_vowels("AEIOU"),
                5
            ],
            'Argument used: "abcdEfgHijkLMnOPqrsTuVwXyz"': [
                count_vowels("abcdEfgHijkLMnOPqrsTuVwXyz"),
                5
            ],
            'Argument used: "zzz"': [
                count_vowels("zzz"),
                0
            ],
            'Argument used: "123"': [
                count_vowels("123"),
                0
            ],
            'Argument used: ""': [
                count_vowels(""),
                0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_count_unique_vowels(self):
        test_cases = {
            'Argument used: "This is an Example Sentence"': [
                count_unique_vowels("This is an Example Sentence"),
                3
            ],
            'Argument used: "aeiou"': [
                count_unique_vowels("aeiou"),
                5
            ],
            'Argument used: "aeiouAEIOU"': [
                count_unique_vowels("aeiouAEIOU"),
                5
            ],
            'Argument used: "aaeeiioouuAAEEIIOOUU"': [
                count_unique_vowels("aeiouAEIOU"),
                5
            ],
            'Argument used: "abcdEfgHijkLMnOPqrsTuVwXyz"': [
                count_unique_vowels("abcdEfgHijkLMnOPqrsTuVwXyz"),
                5
            ],
            'Argument used: "zzz"': [
                count_unique_vowels("zzz"),
                0
            ],
            'Argument used: "123"': [
                count_unique_vowels("123"),
                0
            ],
            'Argument used: "" (empty string)': [
                count_unique_vowels(""), 0
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_replace_character_w_asterisk(self):
        test_cases = {
            'Arguments used: "this is an example sentence", "e"': [
                replace_character_w_asterisk("this is an example sentence", "e"),
                "this is an *xampl* s*nt*nc*"
            ],
            'Arguments used: "this is an example sentence", "x"': [
                replace_character_w_asterisk("this is an example sentence", "x"),
                "this is an e*ample sentence"
            ],
            'Arguments used: "This is an example sentence", "T"': [
                replace_character_w_asterisk("This is an example sentence", "T"),
                "*his is an example sentence"
            ],
            'Arguments used: "this is an example sentence", "z"': [
                replace_character_w_asterisk("this is an example sentence", "z"),
                "this is an example sentence"
            ],
            'Arguments used: "this is an example sentence", "" (empty string)': [
                replace_character_w_asterisk("this is an example sentence", ""),
                "this is an example sentence"
            ],
            'Arguments used: "" (empty string), "a"': [
                replace_character_w_asterisk("", "a"), ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_reverse_string(self):
        test_cases = {
            'Argument used: "This is an example sentence!"': [
                reverse_string("This is an example sentence!"),
                "!ecnetnes elpmaxe na si sihT"
            ],
            'Argument used: "aaaa"': [
                reverse_string("aaaa"),
                "aaaa"
            ],
            'Argument used: "a"': [
                reverse_string("a"),
                "a"
            ],
            'Argument used: ""': [
                reverse_string(""),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_replace_symbols(self):
        test_cases = {
            'Arguments used: "--This is 1 example sentence and we\'ll replace the @ symbol", "@"': [
                replace_symbols("--This is 1 example sentence and we'll replace the @ symbol", "@"),
                "@@This is 1 example sentence and we@ll replace the @ symbol"
            ],
            'Arguments used: "This is an example sentence", "*"': [
                replace_symbols("This is an example sentence", "*"),
                "This is an example sentence"
            ],
            'Arguments used: "This is an example sentence!", "-"': [
                replace_symbols("This is an example sentence!", "-"),
                "This is an example sentence-"
            ],
            'Arguments used: "/$This/ is@ an# example= sentence*", "@"': [
                replace_symbols("/$This/ is@ an# example= sentence*", "@"),
                "@@This@ is@ an@ example@ sentence@"
            ],
            'Arguments used: "1234", "}"': [
                replace_symbols("1234", "}"),
                "1234"
            ],
            'Arguments used: "@@@", "@"': [
                replace_symbols("@@@", "@"),
                "@@@"
            ],
            'Arguments used: " " (empty string), "*"': [
                replace_symbols(" ", "*"),
                " "
            ],
            'Arguments used: "" (empty string), "*"': [
                replace_symbols("", "*"),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_percentage_numerical_digits(self):
        test_cases = {
            'Argument used: "This has 1 digit"': [
                percentage_numerical_digits("This has 1 digit"),
                6.25
            ],
            'Argument used: "1984"': [
                percentage_numerical_digits("1984"),
                100
            ],
            'Argument used: "This is an example sentence"': [
                percentage_numerical_digits("This is an example sentence"),
                0
            ],
            'Argument used: "" (empty string)': [
                percentage_numerical_digits(""),
                0
            ],
            'Argument used: "abc1"': [
                percentage_numerical_digits("abc1"),
                25
            ],
            'Argument used: "Literature: 95"': [
                percentage_numerical_digits("Literature: 95"),
                14.285714285714286
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_classify_numerical_string(self):
        test_cases = {
            'Argument used: "123456"': [
                classify_numerical_string("123456"),
                "246$36"
            ],
            'Argument used: "2222"': [
                classify_numerical_string("2222"),
                "2222$"
            ],
            'Argument used: "1234567890"': [
                classify_numerical_string("1234567890"),
                "24680$3690"
            ],
            'Argument used: "3333"': [
                classify_numerical_string("3333"),
                "$3333"
            ],
            'Argument used: "6666"': [
                classify_numerical_string("6666"),
                "6666$6666"
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_middle_characters(self):
        test_cases = {
            'Argument used: "AbcDefGhi"': [
                middle_characters("AbcDefGhi"),
                "Def"
            ],
            'Argument used: "A   A"': [
                middle_characters("A   A"),
                "   "
            ],
            'Argument used: "bAAAb"': [
                middle_characters("bAAAb"),
                "AAA"
            ],
            'Argument used: "AAAAA"': [
                middle_characters("AAAAA"),
                "AAA"
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_palindrome(self):
        test_cases = {
            'Argument used: "abba"': [
                is_palindrome("abba"),
                True
            ],
            'Argument used: "baéceab"': [
                is_palindrome("baéceab"),
                False
            ],
            'Argument used: "aba"': [
                is_palindrome("aba"),
                True
            ],
            'Argument used: "aa"': [
                is_palindrome("aa"),
                True
            ],
            'Argument used: "a"': [
                is_palindrome("a"),
                True
            ],
            'Argument used: "" (empty string)': [
                is_palindrome(""),
                False
            ],
            'Argument used: "Aba"': [
                is_palindrome("Aba"),
                True
            ],
            'Argument used: "ab"': [
                is_palindrome("ab"),
                False
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_contains_characters(self):
        test_cases = {
            'Arguments used: "super", "supermarket"': [
                contains_characters("super", "supermarket"),
                True
            ],
            'Arguments used: "fff", "foo"': [
                contains_characters("fff", "foo"),
                True
            ],
            'Arguments used: "alh", "alphabet"': [
                contains_characters("alh", "alphabet"),
                True
            ],
            'Arguments used: "e", "cellular"': [
                contains_characters("e", "cellular"),
                True
            ],
            'Arguments used: "alhc", "alphabet"': [
                contains_characters("alhc", "alphabet"),
                False
            ],
            'Arguments used: "Lgh", "light"': [
                contains_characters("Lgh", "light"),
                False
            ],
            'Arguments used: "Lgh", "Light"': [
                contains_characters("Lgh", "Light"),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_is_anagram(self):
        test_cases = {
            'Arguments used: "below", "elbow"': [
                is_anagram("below", "elbow"),
                True
            ],
            'Arguments used: "below", "elbows"': [
                is_anagram("below", "elbows"),
                False
            ],
            'Arguments used: "aaa", "aaa"': [
                is_anagram("aaa", "aaa"),
                True
            ],
            'Arguments used: "Aaa", "aaa"': [
                is_anagram("aaa", "aaa"),
                True
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_how_many_remove_for_anagram(self):
        test_cases = {
            'Arguments used: "states", "tasted"': [
                how_many_remove_for_anagram("states", "tasted"),
                2
            ],
            'Arguments used: "state", "taste"': [
                how_many_remove_for_anagram("state", "taste"),
                0
            ],
            'Arguments used: "state", "tastes"': [
                how_many_remove_for_anagram("state", "tastes"),
                1
            ],
            'Arguments used: "states", "taste"': [
                how_many_remove_for_anagram("states", "taste"),
                1
            ],
            'Arguments used: "STATE", "untasted"': [
                how_many_remove_for_anagram("STATE", "untasted"),
                3
            ],
            'Arguments used: "state", "TASTE"': [
                how_many_remove_for_anagram("state", "TASTE"),
                0
            ],
            'Arguments used: "abc", "def"': [
                how_many_remove_for_anagram("abc", "def"),
                6
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_reverse_words(self):
        test_cases = {
            'Arguments used: "This is an example sentence."': [
                reverse_words("This is an example sentence."),
                "sihT si na elpmaxe .ecnetnes"
            ],
            'Arguments used: "sihT si na elpmaxe !ecnetnes"': [
                reverse_words("sihT si na elpmaxe !ecnetnes"),
                "This is an example sentence!"
            ],
            'Arguments used: "word"': [
                reverse_words("word"),
                "drow"
            ],
            'Arguments used: "123"': [
                reverse_words("123"),
                "321"
            ],
            'Arguments used: "a b c"': [
                reverse_words("a b c"),
                "a b c"
            ],
            'Arguments used: "" (empty string)': [
                reverse_words(""),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_length_last_word(self):
        test_cases = {
            'Argument used: "This is an example sentence"': [
                length_last_word("This is an example sentence"),
                8
            ],
            'Argument used: "   spaces   "': [
                length_last_word("   spaces   "),
                6
            ],
            'Argument used: "word"': [
                length_last_word("word"),
                4
            ],
            'Argument used: "   this   is   an   example   sentence   "': [
                length_last_word("   this   is   an   example   sentence   "),
                8
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_title_case(self):
        test_cases = {
            'Argument used: "This is an example sentence"': [
                title_case("This is an example sentence"),
                "This Is An Example Sentence"
            ],
            'Argument used: "THIS IS AN EXAMPLE SENTENCE"': [
                title_case("THIS IS AN EXAMPLE SENTENCE"),
                "This Is An Example Sentence"
            ],
            'Argument used: "This Is An Example Sentence"': [
                title_case("This Is An Example Sentence"),
                "This Is An Example Sentence"
            ],
            'Argument used: "word"': [
                title_case("word"),
                "Word"
            ],
            'Argument used: "Word"': [
                title_case("Word"),
                "Word"
            ],
            'Argument used: "    this is an example sentence"': [
                title_case("    this is an example sentence"),
                "    This Is An Example Sentence"
            ],
            'Argument used: "this is an example sentence   "': [
                title_case("this is an example sentence   "),
                "This Is An Example Sentence   "
            ],
            'Argument used: "this   is   an   example   sentence"': [
                title_case("this   is   an   example   sentence"),
                "This   Is   An   Example   Sentence"
            ],
            'Argument used: "1this 2is 3an 4example 5sentence"': [
                title_case("1this 2is 3an 4example 5sentence"),
                "1This 2Is 3An 4Example 5Sentence"
            ],
            'Argument used: "this1 is2 an3 example4 sentence5"': [
                title_case("this1 is2 an3 example4 sentence5"),
                "This1 Is2 An3 Example4 Sentence5"
            ],
            'Argument used: "t1h2i3s4 i1s2 a1n2 e1x2a3m4p5l6e7 s1e2n3t4e5n6c7e8"': [
                title_case("t1h2i3s4 i1s2 a1n2 e1x2a3m4p5l6e7 s1e2n3t4e5n6c7e8"),
                "T1h2i3s4 I1s2 A1n2 E1x2a3m4p5l6e7 S1e2n3t4e5n6c7e8"
            ],
            'Argument used: "this_is_an_example_sentence"': [
                title_case("this_is_an_example_sentence"),
                "This_Is_An_Example_Sentence"
            ],
            'Argument used: "They\'re my best friend\'s siblings"': [
                title_case("They're my best friend's siblings"),
                "They're My Best Friend's Siblings"
            ],
            'Argument used: "" (empty string)': [
                title_case(""),
                ""
            ],
            'Argument used: " "': [
                title_case(" "),
                " "
            ],
            'Argument used: "123"': [
                title_case("123"),
                "123"
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_caesar_cipher(self):
        test_cases = {
            'Arguments used: "this is an example sentence", 2': [
                caesar_cipher("this is an example sentence", 2),
                "vjku ku co gacñrng ugovgoeg"
            ],
            'Arguments used: "abc123 xyz987!", 4': [
                caesar_cipher("abc123 xyz987!", 4),
                "efg123 cde987!"
            ],
            'Arguments used: "this is an example sentence", 6': [
                caesar_cipher("this is an example sentence", 6),
                "anñy ñy gs kegrvqk yksaksik"
            ],
            'Arguments used: "123", 8': [
                caesar_cipher("123", 8),
                "123"
            ],
            'Arguments used: "this is an example sentence", 26': [
                caesar_cipher("this is an example sentence", 26),
                "this is an example sentence"
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_shift_n_characters(self):
        test_cases = {
            'Arguments used: "This is an example sentence", 9': [
                shift_n_characters("This is an example sentence", 9),
                " sentenceThis is an example"
            ],
            'Arguments used: "word", 3': [
                shift_n_characters("word", 3),
                "ordw"
            ],
            'Arguments used: "word", 11': [
                shift_n_characters("word", 11),
                "ordw"
            ],
            'Arguments used: "This is an example sentence", 0': [
                shift_n_characters("This is an example sentence", 0),
                "This is an example sentence"
            ],
            'Arguments used: "word", 4': [
                shift_n_characters("word", 4),
                "word"
            ],
            'Arguments used: "", 5': [
                shift_n_characters("", 5),
                ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)

    def test_encode_rle(self):
        test_cases = {
            'Argument used: "aaabbc"': [
                encode_rle("aaabbc"),
                "a3b2c"
            ],
            'Argument used: "abcde"': [
                encode_rle("abcde"),
                "abcde"
            ],
            'Argument used: "abbccc"': [
                encode_rle("abbccc"),
                "ab2c3"
            ],
            'Argument used: "a"': [
                encode_rle("a"),
                "a"
            ],
            'Argument used: "aaaa"': [
                encode_rle("aaaa"),
                "a4"
            ],
            'Argument used: "Aaaa"': [
                encode_rle("Aaaa"),
                "Aa3"
            ],
            'Argument used: "a$bb&&&&&c"': [
                encode_rle("a$bb&&&&&c"),
                "a$b2&5c"
            ],
            'Argument used: ""': [
                encode_rle(""), ""
            ]
        }
        for test_case, (a, b) in test_cases.items():
            with self.subTest(test_case=test_case):
                self.assertEqual(a, b, test_case)
