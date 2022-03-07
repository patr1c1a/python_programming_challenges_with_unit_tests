##################################
#         TOPIC: STRINGS         #
##################################


def has_even_amount_chars(s1, s2):
    """
    Decides if both strings have an even amount of characters.
    Examples:
        even_amount_chars("aaaa", "aaaa") -> True
        even_amount_chars("aaa", "aaaa") -> False
    -Parameters:
        s1 (str): one of the strings to evaluate.
        s2 (str): the other string to evaluate.
    -Returns:
        (bool) True if the amount of characters in both s1 and s2 is an even number.
        False if at least one of the two strings has an odd amount of characters.
    """
    pass


def count_occurrences(s, character):
    """
    Finds how many times a character occurs in a given string, case sensitive.
    Suggestion: avoid using count().
    Example:
        occurrence_count("This is an example sentence", "s") -> 3
    -Parameters:
        s (str): string where character occurrences will be evaluated.
        character: character whose occurrences will be counted.
    -Returns:
        (int) How many occurrences of character can be found in s.
    """
    pass


def count_vowels(s):
    """
    Counts vowel occurrences (including duplicates) in a given string, case insensitive (both upper and lower case).
    Vowels in the English language are: a, e, i, o, u.
    Suggestion: avoid using count().
    Example:
        count_vowels("This is an Example Sentence") -> 9
    -Parameter:
        s (str): string whose vowels will be counted.
    -Returns:
        (int) How many vowels are there in s.
    """
    pass


def count_unique_vowels(s):
    """
    Counts vowels in a given string.
    Vowels in the English language are: a, e, i, o, u.
    Each vowel must be accounted for only once, be it upper or lowe case.
    Suggestion: avoid using count().
    Example:
        count_unique_vowels("This is an Example Sentence") -> 3
    -Parameter:
        s (str): string whose vowels will be counted.
    -Returns:
        (int) How many unique vowels are there in s.
    """
    pass


def replace_character_w_asterisk(s, character):
    """
    Replaces every occurrence of the character with '*'.
    Suggestion: avoid using replace().
    Examples:
        replace_character_w_asterisk("this is an example sentence", "e") -> "this is an *xampl* s*nt*nc*"
    -Parameters:
        s (str): string where replacements will take place.
        character (str): character to be replaced with '*'.
    -Returns:
        (str) A new string where every occurrence of character in s has been replaced with '*'.
    """
    pass


def reverse_string(s):
    """
    Reverses characters in a given string.
    Suggestion: avoid using slices with a negative step.
    Example:
        reverse_string("This is an example sentence!") -> "!ecnetnes elpmaxe na si sihT"
    -Parameter:
        s (str): string that will be reversed.
    -Returns:
        (str) A new string where characters from s are in reverse order.
    """
    pass


def replace_symbols(s, new_character):
    """
    Replaces every symbol in a given string with the given character.
    Symbol: every character that is not a letter, a digit or a space.
    Example:
        replace_symbols("--This is 1 example sentence and we'll replace the @ symbol", "@")
        -> "@@This is 1 example sentence and we@ll replace the @ symbol"
    -Parameters:
        s (str): string where replacements will take place.
        new_character (str): string with length 1 that will replace every symbol in s.
    -Returns:
        (str) A string where every occurrence of any symbol is replaced with new_character.
    """
    pass


def percentage_numerical_digits(s):
    """
    Returns the percentage of numerical digit characters over the total number of characters in a given string.
    Only the number is returned, without the % symbol and with no rounding (in case the number is not an integer).
    Examples:
        percentage_numerical_digits("This has 1 digit") -> 6.25
        percentage_numerical_digits("1984") -> 100
    -Parameter:
        s (str): string to be processed, which may or may not have numerical digit characters.
    -Returns:
        (numeric) Percentage (0 to 100) of numerical digit characters in s, over the total number of characters.
    """
    pass


def classify_numerical_string(s):
    """
    Given a number as a string, returns a new string with just the characters that represent digits that are multiples
    of 2 and digits that are multiples of 3, each group separated by a '$'.
    If a digit is a multiple of 2 and 3 at the same time, it will show up in both sides of the '$ symbol'
    Examples:
         classify_numerical_string("123456") -> "246$36"
         classify_numerical_string("2222") -> "2222$"
    -Paremeter:
        s (str): numerical string that will be processed. The string will only contain numerical digits.
    -Returns:
        (str) A concatenation of characters in s that are multiples of 2 (in their numerical representation), followed
        by a '$' symbol, followed by the concatenation of characters in s that are multiples of 3.
    """
    pass


def middle_characters(s):
    """
    Given a string, returns the 3 middle characters.
    Examples:
        middle_characters("AbcDefGhi") -> "Def"
        middle_characters("A   A") -> "   "
    -Parameter:
        s (str): string that will be processed. The string contains 5 or more characters and its length
        is an odd number.
    -Returns:
        (str) String of length 3 containing the middle characters of s.
    """
    pass


def is_palindrome(s):
    """
    Decides if a string is a palindrome (case insensitive).
    All characters are taken into account, even if they're not letters.
    Accented characters are considered different from their non-accented counterparts.
    Empty string is not considered a palindrome.
    Suggestion: avoid using slices with a negative step, as well as reversed().
    Examples:
        is_palindrome("abba") -> True
        is_palindrome("baéceab") -> False
    -Parameter:
        s (str): string to be evaluated.
    -Returns:
        (bool) True if s is a palindrome. False if it's not.
    """
    pass


def contains_characters(s1, s2):
    """
    Decides if s2 contains all characters included in s1.
    The order in which characters occur shouldn't be taken into account.
    Upper and lower case letters are considered different characters.
    If a character occurs more than once in s1, it counts as one character to find in s2.
    Examples:
        contains_characters("super", "supermarket") -> True
        contains_characters("fff", "foo") will return True.
    -Parameters:
        s1 (str): string whose characters will be evaluated in s2.
        s2 (str): string where characters from s1 will be evaluated.
    -Returns:
        (bool) True is s2 contains all characters included in s1. False if it doesn't contain all of them.
    """
    pass


def is_anagram(s1, s2):
    """
    Decides if s1 is an anagram of s2.
    Case insensitive. Duplicate letters should be taken into account.
    s1 and s2 will only contain letters.
    Examples:
        is_anagram("below", "elbow") -> True
        is_anagram("below", "elbows") -> False
    -Parameters:
        s1 (str): string to be processed, to find out if it's an anagram of s2.
        s2 (str): string to be processed, to find out if it's an anagram of s1.
    -Returns:
        (bool) True if s1 and s2 are anagrams of each other. False if they're not.
    """
    pass


def how_many_remove_for_anagram(s1, s2):
    """
    Returns how many characters should be removed so that s1 and s2 are anagrams of each other.
    Case insensitive. Duplicate letters should be taken into account.
    s1 and s2 will only contain letters.
    Example:
        how_many_remove_for_anagram("states", "tasted") ->2
    -Parameters:
        s1 (str): one of the strings to be processed.
        s2 (str): another string to be processed.
    -Returns:
        (int) Number of characters that should be removed so that both strings become anagrams.
    """
    pass


def reverse_words(s):
    """
    Reverts characteres of every word in a given string.
    Word separator: one space.
    s won't contain leading or trailing spaces. It can contain symbols or digits, and in that case they're treated the
    same way as letters.
    Suggestion: avoid using split().
    Example:
        reverse_words("This is an example sentence.") -> "sihT si na elpmaxe .ecnetnes"
    -Parameters:
        s (str): string with words that will be reversed.
    -Returns:
        (str) A new string where every word is reversed, without altering its original position within s.
    """
    pass


def length_last_word(s):
    """
    Returns the length of the last word in a string.
    Word separator: one or more spaces.
    Examples:
        get_length_last_word("This is an example sentence") -> 8
        get_length_last_word("   spaces   ") -> 6
    -Parameter:
        s (str): string containing letters and spaces only.
    -Returns:
        (int) Number of characters in the last word of s.
    """
    pass


def title_case(s):
    """
    Capitalizes the first letter in every word of a string.
    Word separator: any symbol (characters other than letters and numeric digits), except for apostrophes.
    The position of symbols and digits shouldn't be altered.
    Suggestion: avoid using title().
    Examples:
        title_case("This is an example sentence") -> "This Is An Example Sentence"
        title_case("THIS IS AN EXAMPLE SENTENCE") -> "This Is An Example Sentence"
    -Parameter:
        s (str): string to be processed.
    -Returns:
        (str) A new string with the contents of s, where the first letter in every word is upper case and all other
        letters are lower case.
    """
    pass


def caesar_cipher(s, n):
    """
    Replaces every letter in a string with a letter some fixed number of positions down the alphabet.
    The process is circular: if the end of the alphabet is reached before n shifts can be made, it starts from the
    beginning (letter "a") until n shifts are completed.
    The string may only contain lower case letters, symbols and digits. Only letters will be replaced, leaving other
    characters unmodified.
    The number of shifts (n) will be a number between 1 and 26.
    Examples:
        caesar_cipher("this is an example sentence", 2) -> "vjku ku co gacñrng ugovgoeg"
        caesar_cipher("abc123 xyz987!", 4) -> "efg123 cde987!"
    -Parameters:
        s (str): string to be ciphered.
        n (int): the number of characters to shift the cipher alphabet.
    -Returns:
        (str) A new string where every letter from s has been replaced by another letter, shifting n positions down the
        alphabet.
    """
    pass


def shift_n_characters(s, n):
    """
    Given a string, shifts every character n places forward by n, in a circular way (going back to the beginning when
    the end of the string is reached before n shifts are made).
    Characters can be letters, digits or symbols.
    n isn't necessarily limited to the length of s.
    Examples:
        shift_n_characters("This is an example sentence", 9) -> " sentenceThis is an example"
        shift_n_characters("word", 11) -> "ordw"
    -Parameters:
        s (str): string where characters will be shifted.
        n (int): number of positions each character will be shifted from its original position within s.
    -Returns:
        (str) A new string where each character has been shifted n positions forward.
    """
    pass


def encode_rle(s):
    """
    Compresses a string using RLE ("Run-Length Encoding").
    RLE: replace sequences of the same data values by a single value and a count number. Consecutive characters that
    occur more than once will be stored as one single occurrence, followed by the number of occurrences only when it's
    greater than 1. For distinct characters, only the character will be stored, and no number appended to it.
    The string s may only contain letters and symbols other than digits.
    Examples:
        encode_rle("aaabbc") -> "a3b2c"
        encode_rle("abcde") -> "abcde"
    -Parameter:
        s (str): string to be encoded.
    -Returns:
        (str) Compressed string as a result of applying run-length encoding.
    """
    pass
