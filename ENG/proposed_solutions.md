# Proposed solutions

Here you can find code that might be a solution for each one of the exercises. This doesn't imply these are the only or
even the most efficient solutions. It's just example code that could be useful as a starting point in case you cannot
solve any of the challenges.

Select a category depending on the topic you're working on and then click on the function to expand it and view code.


* [Numbers](#numbers)
* [Strings](#strings)
* [Lists and tuples](#lists-and-tuples)
* [Sets and dictionaries](#sets-and-dictionaries)


# Numbers
<details>
    <summary>
        <pre>
def smallest(number1, number2):
    """
    Returns the smallest between two numbers.
    Examples:
        smallest(number1=3, number2=1) -> 1
        smallest(number1=3, number2=3) -> 3
    -Parameters:
        number1 (numeric): one of the numbers to be processed.
        number2 (numeric): the other number to be processed.
    -Returns:
        (numeric) The smallest between two numbers. number1 if they're equal.
    """
        </pre>
    </summary>
    <pre>
    if number1 < number2 or number1 == number2:
        return number1
    else:
        return number2
    </pre>
</details>


<details>
    <summary>
        <pre>
def absolute_value(number):
    """
    Returns the absolute value of a number.
    Suggestion: avoid using the abs() method.
    Examples:
        absolute_value(number=3) -> 3
        absolute_value(number=-10) -> 10
    -Parameter:
        number (numeric): the number whose absolute value will be calculated.
    -Returns:
        (numeric) Absolute value of a number.
    """
        </pre>
    </summary>
    <pre>
    if number < 0:
        return number * -1
    return number
    </pre>
</details>


<details>
    <summary>
        <pre>
def extract_month(date):
    """
    Given a date consisting of day, month and year, returns the month. Date will have the ddmmaaaa or dmmaaaa format,
    where "d" stands for day digits, "m" stands for month digits and "a" stands for year digits.
    Examples:
        extract_month(date=31122020) -> 12
        extract_month(date=5091946) -> 9
    -Parameters:
        date (int): valid date in a ddmmaaaa or dmmaaaa format. dd (or d) will be between 1 and 31. mm will be between
        1 and 12. Positive.
    -Returns:
        (int) The month contained in date.
    """
        </pre>
    </summary>
    <pre>
    return (date // 10000) % 100
    </pre>
</details>


<details>
    <summary>
        <pre>
def add_multiples(lower, upper, n):
    """
    Adds up the multiples of n contained in a closed interval of integers.
    Examples:
        add_multiples(lower=0, upper=30, n=5) -> 105
        add_multiples(lower=-30, upper=0, n=5) -> -105
    -Parameters:
        lower (int): lower bound of the interval. Lesser or equal to upper.
        upper (int): upper bound of the interval. Greater or equal to lower.
        n (int): number whose multiples will be added up. Cannot be 0.
    -Returns:
        (int) Summation of multiples of n between lower and upper bounds.
    """
        </pre>
    </summary>
    <pre>
    summation = 0
    for number in range(lower, upper + 1):
        if number % n == 0:
            summation += number
    return summation
    </pre>
</details>


<details>
    <summary>
        <pre>
def is_palindromic_number(number):
    """
    Decides if a number is a palindrome or not. A palindrome number remains the same when its digits are reversed.
    Suggestion: only work with numbers (avoid other data types).
    Examples:
        is_palindromic_number(number=123321) -> True
        is_palindromic_number(number=1234) -> False
    -Parameters:
        number (int): number to evaluate. Positive.
    -Returns:
        (bool) True if number is a palindrome, False if it's not.
    """
        </pre>
    </summary>
    <pre>
    number_copy = number
    reverse = 0
    while number_copy != 0:
        remainder = number_copy % 10
        reverse = (reverse * 10) + remainder
        number_copy //= 10
    return number == reverse
    </pre>
</details>


<details>
    <summary>
        <pre>
def leap_year(year):
    """
    Decides if a given year is a leap year according to the Gregorian calendar.
    Examples:
        leap_year(year=2020) -> True
        leap_year(year=1800) -> False
    -Parameter:
        year (int): year to evaluate. Positive.
    -Returns:
        (bool) True if it's a leap year. False if it's not.
    """
        </pre>
    </summary>
    <pre>
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    return False
    </pre>
</details>


<details>
    <summary>
        <pre>
def days_in_month(month, year):
    """
    Determines how many days are there in a given month, from a given year (the case where the month is February in a
    leap year must be considered).
    Suggestion: use the leap_year() function defined above.
    Example:
        days_in_month(month=11, year=1981) -> 30
    -Parameters:
        month (int): number representing the month. Between 1 and 12.
        year (int): number representing the year. Positive.
    -Returns:
        (int) Day count in the given month.
    """
        </pre>
    </summary>
    <pre>
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if leap_year(year):
        return 29
    else:
        return 28
    </pre>
</details>


<details>
    <summary>
        <pre>
def digit_count(number):
    """
    Counts digits in a number.
    Example:
        digit_count(number=120) -> 3
    -Parameter:
        number (int): number whose digits are being counted.
    -Returns:
        (int) Digit count in number.
    """
        </pre>
    </summary>
    <pre>
    if number == 0:
        return 1
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count
    </pre>
</details>


<details>
    <summary>
        <pre>
def add_square_digits(number):
    """
    Finds the sum of squares of digits in a given number.
    Example:
        add_square_digits(number=15) -> 26
    -Parameter:
        number (int): number where digits are being processed. Positive.
    -Returns:
        (int) Sum of squares of every digit in number.
    """
        </pre>
    </summary>
    <pre>
    square_sum = 0
    while number != 0:
        digit = number % 10
        square_sum += digit ** 2
        number = number // 10
    return square_sum
    </pre>
</details>


<details>
    <summary>
        <pre>
def percentage_even_digits(number):
    """
    Finds the percentage of even digits over the total amount of digits in a given number.
    Example:
        percentage_even_digits(number=5555666555) -> 30.0
    -Parameter:
        number (int): number where digits are being processed. Positive.
    -Returns:
        (float) Percentage (from 0 to 100) of even digits in number.
    """
        </pre>
    </summary>
    <pre>
    total_amount = 0
    even_amount = 0
    while number != 0:
        total_amount += 1
        digit = number % 10
        if digit % 2 == 0:
            even_amount += 1
        number //= 10
    if total_amount != 0:
        return (even_amount * 100) / total_amount
    else:
        return 0.0
    </pre>
</details>


<details>
    <summary>
        <pre>
def is_pronic(number):
    """
    Decides if a number is "pronic". A number is considered "pronic" if it's the product of two consecutive integers.
    Example:
        is_pronic(number=56) -> True
        (56 can be expressed as 7*8).
    -Parameter:
        numbero (int): number to evaluate. Greater than 0.
    -Returns:
        (bool) True if number is pronic, False if it's not.
    """
        </pre>
    </summary>
    <pre>
    for i in range(number):
        if i * (i + 1) == number:
            return True
    return False
    </pre>
</details>


<details>
    <summary>
        <pre>
def is_prime(number):
    """
    Finds if a number is prime.
    Example:
        is_prime(number=7) -> True
    -Parameter:
        number (int): number to evaluate. Positive.
    -Returns:
        (bool) True if number is prime. False if it's not.
    """
        </pre>
    </summary>
    <pre>
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    </pre>
</details>


<details>
    <summary>
        <pre>
def factorial(number):
    """
    Finds the factorial of a positive number.
    Example:
        factorial(number=4) -> 24
    -Parameter:
        number (int): number whose factorial will be calculated. Positive.
    -Returns:
        (int) Factorial of number.
    """
        </pre>
    </summary>
    <pre>
    result = 1
    if number >= 0:
        for i in range(1, number + 1):
            result *= i
    return result
    </pre>
</details>


<details>
    <summary>
        <pre>
def sum_first_n_fibonacci(n):
    """
    Finds the sum of the first n terms in the Fibonacci sequence, considering the first two terms in the series are 0
    and 1.
    Example:
        sum_first_n_fibonacci(n=6) -> 12
    -Parameters:
        n (int): how many Fibonacci terms will be summed. Greater or equal than 2.
    -Returns:
        (int) Sum of first n numbers in the Fibonacci sequence.
    """
        </pre>
    </summary>
    <pre>
    first_term = 0
    second_term = 1
    sum_first_second = first_term + second_term
    for i in range(n - 2):
        next_term = first_term + second_term
        sum_first_second += next_term
        first_term = second_term
        second_term = next_term
    return sum_first_second
    </pre>
</details>


<details>
    <summary>
        <pre>
def greatest_divisor(number):
    """
    Finds the greatest integer divisor of a number (except for the number itself).
    Example:
        greatest_divisor(number=182) -> 91
    -Parameters:
        number (int): number whose divisor will be calculated. Positive.
    -Returns:
        (int) Greatest number that can be used as a divisor for the number, without a remainder.
    """
        </pre>
    </summary>
    <pre>
    greatest = 0
    for i in range(1, number):
        if number % i == 0:
            if i > greatest:
                greatest = i
    return greatest
    </pre>
</details>


<details>
    <summary>
        <pre>
def euclidean_gcd(m, n):
    """
    Finds the greatest common divisor of m and n using the Euclidean algorithm.
    Euclidean algorithm: dividing m by n (both integer numbers), we get a quotient q and a remainder r. The greatest
    common divisor of m and n is the same as for n and r. n can't be 0.
    Example:
        euclidean_gcd(m=60, n=24) -> 12
    -Parameters:
        m (int): positive number.
        n (int): positive number, greater than 0.
    -Returns:
        (int) Greatest common divisor of m and n.
    """
        </pre>
    </summary>
    <pre>
    while n != 0:
        r = m % n
        m = n
        n = r
    return m
    </pre>
</details>


<details>
    <summary>
        <pre>
def get_month(consecutive_day, year):
    """
    Finds the month number, given the number of days gone by since January 1st in a particular year (taking into
    account that it could be a leap year).
    Suggestion: use function days_in_month() found above.
    Example:
        get_month(consecutive_day=200, year=1969) -> 7
        (the 60th consecutive day in a leap year represents February 29, while in a non-leap
        year it will be March 1st).
    -Parameters:
        consecutive_day (int): number of days gone by from January 1st. Between 1 and 366.
        year (int): year (leap or non-leap). Positive.
    -Returns:
        (int) Month number (between 1 and 12) where consecutive_day lies in the given year.
    """
        </pre>
    </summary>
    <pre>
    days_gone_by = 0
    month = 1
    while days_gone_by + days_in_month(month, year) < consecutive_day:
        days_gone_by += days_in_month(month, year)
        month += 1
    return month
    </pre>
</details>


<details>
    <summary>
        <pre>
def is_disarium(number):
    """
    Finds if a number is a "disarium" number.
    A disarium number is a number in which the sum of the digits to the power of their respective position (starting
    from position 1 on the left), is equal to the number itself.
    Suggestion: use function digit_count() found above.
    Example:
        is_disarium(number=518) -> True
        (518 is a disarium number, since 5**1=5, 1**2=1, 8**3=512, and 5+1+512=518).
    -Parameter:
        number (int): number whose digits will be evaluated. Positive.
    -Returns:
        (bool) True if number is "disarium", False if it's not.
    """
        </pre>
    </summary>
    <pre>
    digit_position = digit_count(number)
    number_copy = number
    current_sum = 0
    while number_copy > 0:
        digit = number_copy % 10
        current_sum = current_sum + (digit ** digit_position)
        digit_position -= 1
        number_copy //= 10
    return current_sum == number
    </pre>
</details>


<details>
    <summary>
        <pre>
def arrange_coins(amount):
    """
    Finds how many rows can be "built" using a given amount of coins that will be arranged in a "staircase" way, where
    every "n"th row must contain exactly "n" coins. The last row of the staircase can be incomplete.
    Example:
        arrange_coins(amount=5) -> 2
        (With 5 coins we can build only 2 full rows, since there are not enough coins for the third row:
        ¤
        ¤ ¤
        ¤ ¤
        )
    -Parameter:
        amount (int): number of coins that must be used. Positive.
    -Returns:
        (int) Maximum full rows that can be built with the given amount of coins.
    """
        </pre>
    </summary>
    <pre>
    row = 1
    while amount - row >= 0:
        amount -= row
        row += 1
    return row - 1
    </pre>
</details>


<details>
    <summary>
        <pre>
def single_ones(number):
    """
    Finds how many "ones" in a number are not followed by another consecutive "one".
    Suggestion: avoid converting the number or its digits into a diferent data type.
    Example:
        single_ones(number=141211) -> 2
        single_ones(number=11411211) -> 0
    -Parameter:
        number (int): number whose digits will be evaluated. Positive.
    -Returns:
        (int) How many non-consecutive 1's are there in number.
    """
        </pre>
    </summary>
    <pre>
    ones = 0
    prev_is_one = False
    consecutive_ones = False
    while number != 0:
        current_digit = number % 10
        if current_digit == 1:
            if prev_is_one:
                consecutive_ones = True
            prev_is_one = True
        else:
            if prev_is_one and not consecutive_ones:
                ones += 1
            prev_is_one = False
            consecutive_ones = False
        number //= 10
    if prev_is_one and not consecutive_ones:
        return ones + 1
    return ones
    </pre>
</details>


# Strings

<details>
    <summary>
        <pre>
def has_even_amount_chars(s1, s2):
    """
    Decides if both strings have an even amount of characters.
    Examples:
        even_amount_chars(s1="aaaa", s2="aaaa") -> True
        even_amount_chars(s1="aaa", s2="aaaa") -> False
    -Parameters:
        s1 (str): one of the strings to evaluate.
        s2 (str): the other string to evaluate.
    -Returns:
        (bool) True if the amount of characters in both s1 and s2 is an even number.
        False if at least one of the two strings has an odd amount of characters.
    """
        </pre>
    </summary>
    <pre>
    return len(s1) % 2 == 0 and len(s2) % 2 == 0
    </pre>
</details>


<details>
    <summary>
        <pre>
def count_occurrences(s, character):
    """
    Finds how many times a character occurs in a given string, case sensitive.
    Suggestion: avoid using count().
    Example:
        occurrence_count(s="This is an example sentence", character="s") -> 3
    -Parameters:
        s (str): string where character occurrences will be evaluated.
        character: character whose occurrences will be counted.
    -Returns:
        (int) How many occurrences of character can be found in s.
    """
        </pre>
    </summary>
    <pre>
    count = 0
    for c in s:
        if c == character:
            count += 1
    return count
    </pre>
</details>


<details>
    <summary>
        <pre>
def count_vowels(s):
    """
    Counts vowel occurrences (including duplicates) in a given string, case insensitive (both upper and lower case).
    Vowels in the English language are: a, e, i, o, u.
    Suggestion: avoid using count().
    Example:
        count_vowels(s="This is an Example Sentence") -> 9
    -Parameter:
        s (str): string whose vowels will be counted.
    -Returns:
        (int) How many vowels are there in s.
    """
        </pre>
    </summary>
    <pre>
    count = 0
    for character in s:
        if character in "aeiouAEIOU":
            count += 1
    return count
    </pre>
</details>


<details>
    <summary>
        <pre>
def count_unique_vowels(s):
    """
    Counts vowels in a given string.
    Vowels in the English language are: a, e, i, o, u.
    Each vowel must be accounted for only once, be it upper or lowe case.
    Suggestion: avoid using count().
    Example:
        count_unique_vowels(s="This is an Example Sentence") -> 3
    -Parameter:
        s (str): string whose vowels will be counted.
    -Returns:
        (int) How many unique vowels are there in s.
    """
        </pre>
    </summary>
    <pre>
    lowercase_str = s.lower()
    count = 0
    for character in "aeiou":
        if character in lowercase_str:
            count += 1
    return count
    </pre>
</details>


<details>
    <summary>
        <pre>
def replace_character_w_asterisk(s, character):
    """
    Replaces every occurrence of the character with '*'.
    Suggestion: avoid using replace().
    Examples:
        replace_character_w_asterisk(s="this is an example sentence", character="e") -> "this is an *xampl* s*nt*nc*"
    -Parameters:
        s (str): string where replacements will take place.
        character (str): character to be replaced with '*'.
    -Returns:
        (str) A new string where every occurrence of character in s has been replaced with '*'.
    """
        </pre>
    </summary>
    <pre>
    new = ""
    for c in s:
        if c == character:
            new = new + "*"
        else:
            new = new + c
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def reverse_string(s):
    """
    Reverses characters in a given string.
    Suggestion: avoid using slices with a negative step.
    Example:
        reverse_string(s="This is an example sentence!") -> "!ecnetnes elpmaxe na si sihT"
    -Parameter:
        s (str): string that will be reversed.
    -Returns:
        (str) A new string where characters from s are in reverse order.
    """
        </pre>
    </summary>
    <pre>
    new = ""
    i = len(s) - 1
    while i >= 0:
        new = new + s[i]
        i -= 1
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def replace_symbols(s, new_character):
    """
    Replaces every symbol in a given string with the given character.
    Symbol: every character that is not a letter, a digit or a space.
    Example:
        replace_symbols(s="--This is 1 example sentence and we'll replace the @ symbol", new_character="@")
        -> "@@This is 1 example sentence and we@ll replace the @ symbol"
    -Parameters:
        s (str): string where replacements will take place.
        new_character (str): string with length 1 that will replace every symbol in s.
    -Returns:
        (str) A string where every occurrence of any symbol is replaced with new_character.
    """
        </pre>
    </summary>
    <pre>
    replaced = ""
    for character in s:
        if (not character.isalpha()) and (not character.isdigit()) and character != " ":
            replaced = replaced + new_character
        else:
            replaced = replaced + character
    return replaced
    </pre>
</details>


<details>
    <summary>
        <pre>
def percentage_numerical_digits(s):
    """
    Returns the percentage of numerical digit characters over the total number of characters in a given string.
    Only the number is returned, without the % symbol and with no rounding (in case the number is not an integer).
    Examples:
        percentage_numerical_digits(s="This has 1 digit") -> 6.25
        percentage_numerical_digits(s="1984") -> 100
    -Parameter:
        s (str): string to be processed, which may or may not have numerical digit characters.
    -Returns:
        (numeric) Percentage (0 to 100) of numerical digit characters in s, over the total number of characters.
    """
        </pre>
    </summary>
    <pre>
    if len(s) == 0:
        return 0
    number_count = 0
    for character in s:
        if character in "1234567890":
            number_count += 1
    return (number_count * 100) / len(s)
    </pre>
</details>


<details>
    <summary>
        <pre>
def classify_numerical_string(s):
    """
    Given a number as a string, returns a new string with just the characters that represent digits that are multiples
    of 2 and digits that are multiples of 3, each group separated by a '$'.
    If a digit is a multiple of 2 and 3 at the same time, it will show up in both sides of the '$ symbol'
    Examples:
         classify_numerical_string(s="123456") -> "246$36"
         classify_numerical_string(s="2222") -> "2222$"
    -Paremeter:
        s (str): numerical string that will be processed. The string will only contain numerical digits.
    -Returns:
        (str) A concatenation of characters in s that are multiples of 2 (in their numerical representation), followed
        by a '$' symbol, followed by the concatenation of characters in s that are multiples of 3.
    """
        </pre>
    </summary>
    <pre>
    multiples2 = ""
    multiples3 = ""
    for character in s:
        if int(character) % 2 == 0:
            multiples2 += character
        if int(character) % 3 == 0:
            multiples3 += character
    return multiples2 + "$" + multiples3
    </pre>
</details>


<details>
    <summary>
        <pre>
def middle_characters(s):
    """
    Given a string, returns the 3 middle characters.
    Examples:
        middle_characters(s="AbcDefGhi") -> "Def"
        middle_characters(s="A   A") -> "   "
    -Parameter:
        s (str): string that will be processed. The string contains 5 or more characters and its length
        is an odd number.
    -Returns:
        (str) String of length 3 containing the middle characters of s.
    """
        </pre>
    </summary>
    <pre>
    centro = (len(s) // 2)
    return s[centro - 1:centro + 2]
    </pre>
</details>


<details>
    <summary>
        <pre>
def is_palindrome(s):
    """
    Decides if a string is a palindrome (case insensitive).
    All characters are taken into account, even if they're not letters.
    Accented characters are considered different from their non-accented counterparts.
    Empty string is not considered a palindrome.
    Suggestion: avoid using slices with a negative step, as well as reversed().
    Examples:
        is_palindrome(s="abba") -> True
        is_palindrome(s="baéceab") -> False
    -Parameter:
        s (str): string to be evaluated.
    -Returns:
        (bool) True if s is a palindrome. False if it's not.
    """
        </pre>
    </summary>
    <pre>
    lower_case = s.lower()
    if len(lower_case) == 0:
        return False
    if len(lower_case) == 1:
        return True
    else:
        i = 0
        length = len(lower_case) - 1
        while length > i:
            if lower_case[i] != lower_case[length]:
                return False
            i = i + 1
            length = length - 1
        return True
    </pre>
</details>


<details>
    <summary>
        <pre>
def contains_characters(s1, s2):
    """
    Decides if s2 contains all characters included in s1.
    The order in which characters occur shouldn't be taken into account.
    Upper and lower case letters are considered different characters.
    If a character occurs more than once in s1, it counts as one character to find in s2.
    Examples:
        contains_characters(s1="super", s2="supermarket") -> True
        contains_characters(s1="fff", s2="foo") will return True.
    -Parameters:
        s1 (str): string whose characters will be evaluated in s2.
        s2 (str): string where characters from s1 will be evaluated.
    -Returns:
        (bool) True is s2 contains all characters included in s1. False if it doesn't contain all of them.
    """
        </pre>
    </summary>
    <pre>
    for character in s1:
        if character not in s2:
            return False
    return True
    </pre>
</details>


<details>
    <summary>
        <pre>
def is_anagram(s1, s2):
    """
    Decides if s1 is an anagram of s2.
    Case insensitive. Duplicate letters should be taken into account.
    s1 and s2 will only contain letters.
    Examples:
        is_anagram(s1="below", s2="elbow") -> True
        is_anagram(s1="below", s2="elbows") -> False
    -Parameters:
        s1 (str): string to be processed, to find out if it's an anagram of s2.
        s2 (str): string to be processed, to find out if it's an anagram of s1.
    -Returns:
        (bool) True if s1 and s2 are anagrams of each other. False if they're not.
    """
        </pre>
    </summary>
    <pre>
    if len(s1) != len(s2):
        return False
    remaining_s2 = s2.lower()
    for character in s1.lower():
        if character in remaining_s2:
            remaining_s2 = remaining_s2.replace(character, "", 1)
        else:
            return False
    return remaining_s2 == ""
    </pre>
</details>


<details>
    <summary>
        <pre>
def how_many_remove_for_anagram(s1, s2):
    """
    Returns how many characters should be removed so that s1 and s2 are anagrams of each other.
    Case insensitive. Duplicate letters should be taken into account.
    s1 and s2 will only contain letters.
    Example:
        how_many_remove_for_anagram(s1="states", s2="tasted") -> 2
    -Parameters:
        s1 (str): one of the strings to be processed.
        s2 (str): another string to be processed.
    -Returns:
        (int) Number of characters that should be removed so that both strings become anagrams.
    """
        </pre>
    </summary>
    <pre>
    extra_characters = 0
    remaining_s2 = s2.lower()
    for character in s1.lower():
        if character not in remaining_s2:
            extra_characters += 1
        else:
            remaining_s2 = remaining_s2.replace(character, "", 1)
    return extra_characters + len(remaining_s2)
    </pre>
</details>


<details>
    <summary>
        <pre>
def reverse_words(s):
    """
    Reverts characteres of every word in a given string.
    Word separator: one space.
    s won't contain leading or trailing spaces. It can contain symbols or digits, and in that case they're treated the
    same way as letters.
    Suggestion: avoid using split().
    Example:
        reverse_words(s="This is an example sentence.") -> "sihT si na elpmaxe .ecnetnes"
    -Parameters:
        s (str): string with words that will be reversed.
    -Returns:
        (str) A new string where every word is reversed, without altering its original position within s.
    """
        </pre>
    </summary>
    <pre>
    new = ""
    for i in range(s.count(" ")):
        space = s.find(" ")
        word = s[:space]
        new += word[::-1] + " "
        s = s[space + 1:]
    new += s[::-1]
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def length_last_word(s):
    """
    Returns the length of the last word in a string.
    Word separator: one or more spaces.
    Examples:
        get_length_last_word(s="This is an example sentence") -> 8
        get_length_last_word(s="   spaces   ") -> 6
    -Parameter:
        s (str): string containing letters and spaces only.
    -Returns:
        (int) Number of characters in the last word of s.
    """
        </pre>
    </summary>
    <pre>
    if len(s) == 0:
        return 0
    count = 0
    for i in range(len(s)):
        if s[i] != " ":
            count += 1
        else:
            if i < len(s) - 1 and s[i + 1] != " ":
                count = 0
    return count
    </pre>
</details>


<details>
    <summary>
        <pre>
def title_case(s):
    """
    Capitalizes the first letter in every word of a string.
    Word separator: any symbol (characters other than letters and numeric digits), except for apostrophes.
    The position of symbols and digits shouldn't be altered.
    Suggestion: avoid using title().
    Examples:
        title_case(s="This is an example sentence") -> "This Is An Example Sentence"
        title_case(s="THIS IS AN EXAMPLE SENTENCE") -> "This Is An Example Sentence"
    -Parameter:
        s (str): string to be processed.
    -Returns:
        (str) A new string with the contents of s, where the first letter in every word is upper case and all other
        letters are lower case.
    """
        </pre>
    </summary>
    <pre>
    new = ""
    word_start = True
    for character in s:
        if not character.isalpha():
            new = new + character
            if (not character.isdigit()) and character != "'":
                word_start = True
        else:
            if word_start:
                new = new + character.upper()
                word_start = False
            else:
                new = new + character.lower()
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def caesar_cipher(s, n):
    """
    Replaces every letter in a string with a letter some fixed number of positions down the alphabet.
    The process is circular: if the end of the alphabet is reached before n shifts can be made, it starts from the
    beginning (letter "a") until n shifts are completed.
    The string may only contain lower case letters, symbols and digits. Only letters will be replaced, leaving other
    characters unmodified.
    The number of shifts (n) will be a number between 1 and 26.
    Examples:
        caesar_cipher(s="this is an example sentence", n=2) -> "vjku ku co gacñrng ugovgoeg"
        caesar_cipher(s="abc123 xyz987!", n=4) -> "efg123 cde987!"
    -Parameters:
        s (str): string to be ciphered.
        n (int): the number of characters to shift the cipher alphabet.
    -Returns:
        (str) A new string where every letter from s has been replaced by another letter, shifting n positions down the
        alphabet.
    """
        </pre>
    </summary>
    <pre>
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    cipher = ""
    for character in s:
        if character in alphabet:
            position = alphabet.find(character)
            position = (position + n) % 26
            cipher += alphabet[position]
        else:
            cipher += character
    return cipher
    </pre>
</details>


<details>
    <summary>
        <pre>
def shift_n_characters(s, n):
    """
    Given a string, shifts every character n places forward by n, in a circular way (going back to the beginning when
    the end of the string is reached before n shifts are made).
    Characters can be letters, digits or symbols.
    n isn't necessarily limited to the length of s.
    Examples:
        shift_n_characters("This is an example sentence", n=9) -> " sentenceThis is an example"
        shift_n_characters("word", n=11) -> "ordw"
    -Parameters:
        s (str): string where characters will be shifted.
        n (int): number of positions each character will be shifted from its original position within s.
    -Returns:
        (str) A new string where each character has been shifted n positions forward.
    """
        </pre>
    </summary>
    <pre>
    shifted = s
    for position in range(len(s)):
        new_position = (position + n) % len(s)
        shifted = shifted[:new_position] + s[position] + shifted[new_position + 1:]
    return shifted
    </pre>
</details>


<details>
    <summary>
        <pre>
def encode_rle(s):
    """
    Compresses a string using RLE ("Run-Length Encoding").
    RLE: replace sequences of the same data values by a single value and a count number. Consecutive characters that
    occur more than once will be stored as one single occurrence, followed by the number of occurrences only when it's
    greater than 1. For distinct characters, only the character will be stored, and no number appended to it.
    The string s may only contain letters and symbols other than digits.
    Examples:
        encode_rle(s="aaabbc") -> "a3b2c"
        encode_rle(s="abcde") -> "abcde"
    -Parameter:
        s (str): string to be encoded.
    -Returns:
        (str) Compressed string as a result of applying run-length encoding.
    """
        </pre>
    </summary>
    <pre>
    encoded = ""
    if len(s) < 2:
        return s
    position = 1
    count = 1
    while position < len(s):
        if s[position] != s[position - 1]:
            encoded += s[position - 1]
            if count != 1:
                encoded += str(count)
                count = 1
        else:
            count += 1
        position += 1
    encoded += s[position - 1]
    if count != 1:
        encoded += str(count)
    return encoded
    </pre>
</details>



# Lists and tuples

<details>
    <summary>
        <pre>
def multiplication(nums):
    """
    Returns the multiplication of all numbers in a list.
    The list will only contain numbers.
    Example:
        multiplication([1, 2, 3, 4]) -> 24
    -Parameters:
        nums (list, elements: numeric): list whose numbers will be multiplied.
    -Returns:
        (numeric / None) Product of all numbers in nums. If nums is empty, it returns None.
    """
        </pre>
    </summary>
    <pre>
    if len(nums) == 0:
        return None
    product = 1
    for number in nums:
        product *= number
    return product
    </pre>
</details>


<details>
    <summary>
        <pre>
def greatest_element(strings):
    """
    Returns the greatest element (lexicographically) from a list containing string elements.
    Example:
        greatest_element(["x", "y", "z"]) -> "z"
    -Parameters:
        strings (list; elements: str): list where the greatest element will be searched for.
    -Returns:
        (str / None) The greatest string in the list. If the list is empty, it returns None.
    """
        </pre>
    </summary>
    <pre>
    if len(strings) == 0:
        return None
    greatest = ""
    for string in strings:
        if string > greatest:
            greatest = string
    return greatest
    </pre>
</details>


<details>
    <summary>
        <pre>
def highest_profit(prices):
    """
    Given a list where each element represents the price of shares of a company in the stocks market in a given day,
    returns the highest profit that can be obtained if shares are bought on the day with the lowest price and then
    sold on the day with the highest price.
    The list will have at least two elements.
    Example:
        highest_profit([70, 53, 15, 23, 41, 30]) -> 55
        (If prices are [70, 53, 15, 23, 41, 30] the biggest profit can be obtained by buying when price is 15 and then
        selling when it's 70, so 70-15=55).
    -Parameter:
        prices (list; elements: numeric): list with prices of shares of a company in each given day. len(prices) >= 2.
    -Returns:
        (numeric) The highest profit that can be obtained if shares are bought at the lowest price and then sold at the
        highest price.
    """
        </pre>
    </summary>
    <pre>
    max_price = prices[0]
    min_price = prices[0]
    for price in prices:
        if price > max_price:
            max_price = price
        elif price < min_price:
            min_price = price
    return max_price - min_price
    </pre>
</details>


<details>
    <summary>
        <pre>
def no_duplicates(might_have_duplicates):
    """
    Returns a list with those elements from the given list that have no duplicates.
    Examples:
        no_duplicates([3, False, "a", 1, 1, 2, 4, False, 4]) -> [3, "a", 2]
        no_duplicates([1, 1, 1]) -> []
    -Paremeter:
        might_have_duplicates (list; elements: multiple types): list that may or may not have duplicate elements.
    -Returns:
        (list; elements: multiple types) A new list with the elements from might_have_duplicates that are unique (have
        no duplicates).
    """
        </pre>
    </summary>
    <pre>
    new = []
    for element in might_have_duplicates:
        if might_have_duplicates.count(element) == 1:
            new.append(element)
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def percentages_even_odd_numbers(nums):
    """
    Given a list of numbers, returns a tuple with the percentage of even and odd numbers in the list.
    We can assume that len(nums) >= 1.
    Examples:
        percentages_even_odd_numbers([-5, 3, 2, -4, 7]) -> (40.0, 60.0)
        percentages_even_odd_numbers([1, 1, 1, 1]) -> (0.0, 100.0)
    -Parameter:
        nums (list; elements: int): list with numbers. len(numbers) >= 1.
    -Returns:
        (tuple; elements: float). A 2-element tuple where its first element represents the percentage (from 0 to 100) of
        even numbers contained in nums, while the second element represents the percentage of odd numbers in nums.
    """
        </pre>
    </summary>
    <pre>
    even_count = 0
    odd_count = 0
    for number in nums:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count * 100) / len(nums), (odd_count * 100) / len(nums)
    </pre>
</details>


<details>
    <summary>
        <pre>
def add_index(nums):
    """
    Adds the index number to each element in a list of numbers.
    Examples:
        add_index([1, 2, 3, 4, 5, 6]) -> [1, 3, 5, 7, 9, 11]
        add_index([0, 0, 0]) -> [0, 1, 2]
    -Parameters:
        nums (list; elements: numeric): list with numbers.
    -Returns:
        (list; elements: numeric) A new list where each element from nums was added to its index.
    """
        </pre>
    </summary>
    <pre>
    new = []
    for index in range(len(nums)):
        new.append(nums[index] + index)
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def partial_sums(nums):
    """
    Returns a new list where each element is calculated by adding up all previous elements up to the current one in the
    given list.
    Examples:
        partial_sums([4, 6, 10, 7]) -> [4, 10, 20, 27]
        (Each element in the new list is calculated as follows: 4, 6+4, 10+6+4, 7+10+6+4)
    -Parameters:
        nums (list; elements: numeric): list with numbers.
    -Returns:
        (list; elements: numeric) A new list where each element is calculated as the sum of all previous elements plus
        itself in nums.
    """
        </pre>
    </summary>
    <pre>
    new = []
    subtotal = 0
    for numero in nums:
        subtotal += numero
        new.append(subtotal)
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def missing_numbers(nums):
    """
    Given nums, a list of n integer elements, returns a new list containing the numbers between 0 and n-1 that are
    missing in nums.
    Examples:
        missing_numbers([5, 0, 2, 9, 8, 12, 9]) -> [1, 3, 4, 6]
        (n=7, so: 1, 3, 4, 6 are the numbers between 0 and 6 missing in the list).
        missing_numbers([3, 7, 15, 3, 9]) -> [0, 1, 2, 4]
    -Parameter:
        nums (list, elements: int): list with numbers, of length n.
    -Returns:
        (list; elements: int) A new list where elements are the numbers from 0 to n-1 that are not included in nums.
    """
        </pre>
    </summary>
    <pre>
    new = []
    for i in range(len(nums)):
        if i not in nums:
            new.append(i)
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def how_many_are_smaller(nums):
    """
    Returns a new list where each element j represents how many elements in nums are smaller than nums[i].
    Example:
        how_many_are_smaller([6, 3, 3, 4, 2]) -> [4, 1, 1, 3, 0]
        (Since i=0 stores number 6 and there are four other elements in nums that are smaller than 6: 3, 3, 4, 1.
        i=1 stores number 3 and there is one smaller element: 2. The same happens with i=2. i=3 stores 4 and there are
        three smaller elements: 3, 3, 2. And for i=4, which stores number 2, there are no smaller elements).
    -Parameters:
        nums (list; elements: numeric): list with numbers.
    -Returns:
        (list; elements: numeric) A new list where each element j represents the number of elements smaller than
        nums[i].
    """
        </pre>
    </summary>
    <pre>
    new = []
    for current_number in nums:
        lesser_than_number = 0
        for number_to_compare in nums:
            if number_to_compare < current_number:
                lesser_than_number += 1
        new.append(lesser_than_number)
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def two_largest(nums):
    """
    Returns the two largest numbers in nums.
    We can assume that len(nums) >= 2.
    Example:
        two_largest([5, 3, 6, 2, 8]) -> (8, 6)
    -Parameter:
        nums (list; elements: numeric): list with numbers. len(numeros) >=2
    -Returns:
        (tuple; 2 numeric elements) A tuple with the two largest numbers in nums, where the element at index 0 is
        greater or equal to the element at index 1.
    """
        </pre>
    </summary>
    <pre>
    max1 = nums[0]
    max2 = nums[1]
    for number in nums:
        if number > max1:
            max2 = max1
            max1 = number
        elif number > max2:
            max2 = number
    return max1, max2
    </pre>
</details>


<details>
    <summary>
        <pre>
def uno_round(hand, card_discard_pile):
    """
    Given a "hand" of cards for a "Uno" player, and the card on top of the discard pile, returns True if the player is
    allowed to play one of their cards, or False if not.
    The player is allowed to play a card if they:
    * hold a card matching the color of the card on top of the discard pile, or
    * hold a card matching the number of the card on top of the discard pile.
    Cards are represented by a string containing the name of a color and a number (between 0 and 9), separated by a
    space (e.g.: "blue 3"). The player can hold 0 or more cards in a hand.
    Examples:
        uno_round(["red 2", "blue 5", "green 1"], "red 3") -> True
        uno_round(["red 2", "blue 5", "green 1"], "yellow 3") -> False
    -Parameters:
        hand (list; elements: str): list with the cards held in hand by the player.
        card_discard_pile (str): card on top of the discard pile.
    -Returns:
        (bool) True if the player is allowed to play a card: if either the color or the number in one of the cards held
        in hand matches the color or the number in the card on top of the discard pile. False otherwise.
    """
        </pre>
    </summary>
    <pre>
    card_discard_pile_color = card_discard_pile[:len(card_discard_pile) - 2]
    card_discard_pile_number = card_discard_pile[:-2:-1]
    for card in hand:
        color = card[:len(card)-2]
        number = card[:-2:-1]
        if color == card_discard_pile_color or number == card_discard_pile_number:
            return True
    return False
    </pre>
</details>


<details>
    <summary>
        <pre>
def discard_excess_occurrences(nums, maximum):
    """
    Given a list nums and a maximum, returns a new list with the elements from nums without exceeding a maximum of
    occurrences. That means that, for each element in nums, if it occurs more than maximum times, only up to maximum
    occurrences will be included in the new list. All other elements will preserve the same relative order they have in
    the nums list.
    Examples:
        discard_excess_occurrences([1, 2, 3, 2, 3, 3], 1) -> [1, 2, 3]
        discard_excess_occurrences([1, 2, 3, 2, 3, 3], 3) -> [1, 2, 3, 2, 3, 3]
    -Parameters:
        nums (list; elements: int): list with numbers.
        maximum (int): number of maximum occurrences allowed for each element.
    -Returns:
        (list; elements: int) A new list where elements from nums are copied without altering their relative position,
        but discarding any occurrences that exceed the maximum amount allowed.
    """
        </pre>
    </summary>
    <pre>
    new = []
    for element in nums:
        if new.count(element) < maximum:
            new.append(element)
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def is_shifted(nums1, nums2, n):
    """
    Given two lists, decides if the first list matches the second one after its elements have been shifted forward n
    times, in a circular manner (that is: after the last element is reached, the shifting goes back to the beginning).
    Both lists have the same length.
    Examples:
        is_shifted([1, 2, 3, 4], [3, 4, 1, 2], 2) -> True
        is_shifted([1, 2], [3, 4], 1) -> False
    -Parameters:
        nums1 (list; elements: numeric): shifted list.
        nums2 (list; elements: numeric): list with which nums1 will be compared.
        n (int): number of shifts done. Positive.
    -Returns:
        (bool) True if nums2 matches nums1 after n shifts are made. False otherwise.
    """
        </pre>
    </summary>
    <pre>
    return nums1 == nums2[n:] + nums2[:n]
    </pre>
</details>


<details>
    <summary>
        <pre>
def add_every_nth(nums, n):
    """
    Given a list nums and a step n, returns the sum of every nth elements in nums.
    n is not necessarily a multiple of len(nums).
    n cannot be 0.
    If n is greater than len(nums), returns 0.
    Suggestion: avoid using sum().
    Examples:
        add_every_n_numbers([5, 2, 1, 6, 4, 9, 3, 7, 8], 3) -> 18
        (Since 1+9+8=18).
        add_every_n_numbers([1.5, 2, -3, 4], 5) -> 0
    -Parameters:
        nums (list; elements: numeric): list with numbers.
        n (int): step. Greater than 0.
    -Returns:
        (int) Sum of elements in nums, starting with the nth element and going forward every n elements. 0 if n is
        greater than the length of nums.
    """
        </pre>
    </summary>
    <pre>
    if n == 0:
        return nums[0]
    total = 0
    for i in range(len(nums)):
        if (i+1) % n == 0:
            total += nums[i]
    return total
    </pre>
</details>


<details>
    <summary>
        <pre>
def move_zeroes(nums):
    """
    Given a list with integers, moves all 0's to the end of the list, without altering the relative order of other
    elements.
    This will be done in-place, without using additional lists.
    Examples:
        move_zeroes([5, 8, 0, 3, 0, 0, 4]) -> [5, 8, 3, 4, 0, 0, 0]
        move_zeroes([1, 2, 3, 0, 0, 0]) -> [1, 2, 3, 0, 0, 0]
    -Parameter:
        nums (list; elements: int): list with numbers.
    -Returns:
        (list; elements: int) The list (nums) with all zeroes moved to the end of the list and with all non-zero
        elements in their same relative position.
    """
        </pre>
    </summary>
    <pre>
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
    </pre>
</details>


<details>
    <summary>
        <pre>
def unnest(nested_lists):
    """
    Given a list whose elements are also (nested) lists, returns a new list where one level of nesting has been removed.
    Suggestion: avoid using nested loops in the algorithm.
    Examples:
        unnest([[1, 0, 4], ["a", "b"], [True, False, True, True]]) -> [1, 0, 4, "a", "b", True, False, True, True]
        unnest([[], ["a", "b"]]) -> ["a", "b"]
    -Parameter:
        nested_lists (list; elements: lists containing elements of multiple types): a list with nested list elements.
    -Returns:
        (list; elements: multiple types) A new list containing the elements in each nested list, in the same order.
    """
        </pre>
    </summary>
    <pre>
    new = []
    for inner_list in nested_lists:
        new = new + inner_list
    return new
    </pre>
</details>


<details>
    <summary>
        <pre>
def how_many_passed(exam_results):
    """
    Given a list with exam results for a group of students, returns how many of them passed. They need a grade of 6 to
    pass the exam. Results for each student are contained in a list with the following three elements: student name,
    identification number, exam grade.
    Example:
        how_many_passed([
                         ["Joan Taylor", 331, 6],
                         ["Louisa Kay", 112, 3],
                         ["Adam Burton", 256, 8],
                         ["Martin Smith", 209, 7]
                        ])
        -> 3
    -Parameter:
        exam_results (list; elements: lists containing 3 elements: str, int, int): list with student information in
        nested lists.
    -Returns:
        (int) Number of students that passed the exam (with a grade of 6 or more).
    """
        </pre>
    </summary>
    <pre>
    passed = 0
    for result in exam_results:
        if result[2] >= 6:
            passed += 1
    return passed
    </pre>
</details>


<details>
    <summary>
        <pre>
def diagonal_sum(matrix):
    """
    Given a square matrix (made up of a nested lists), returns the sum of its primary diagonal.
    Example:
        diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 15
        (Since the matrix can be read as:
        [[1,2,3],
        [4,5,6],
        [7,8,9]]
        and this returns 15, since 1+5+9=15).
    -Parameter:
        matrix (list; elements: lists containing numeric elements): list with nested lists forming a matrix of n columns
        and n rows.
    -Returns:
        (numeric) Sum of the matrix primary diagonal.
    """
        </pre>
    </summary>
    <pre>
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total
    </pre>
</details>


<details>
    <summary>
        <pre>
def find_country(cities, city_name):
    """
    Given a list with tuples containing a city name and its country, and a city name, decides to which country the given
    city belongs. If the city is not included in any of the tuples, returns None.
    Example:
        find_country(
                     [("Buenos Aires", "Argentina"),
                      ("Glasgow", "Scotland"),
                      ("Liverpool", "England"),
                      ("Madrid", "Spain")],
                     "Glasgow")
        -> "Scotland"
    -Parameters:
        -cities (list; elements: tuples containing 2 elements: str, str): list with cities and their matching countries,
        represented by tuples with the following structure: (city name, country name).
        -city_name (str): name of a city.
    -Returns:
        (str / None) Name of the country that city_name belongs to. None if city_name is not found in any tuple within
        the cities list.
    """
        </pre>
    </summary>
    <pre>
    for city in cities:
        if city_name == city[0]:
            return city[1]
    return None
    </pre>
</details>


<details>
    <summary>
        <pre>
def find_destination(tickets, cities, ticket_number):
    """
    Given a list with travel tickets, a list of cities and a ticket number, returns the destination country to which
    the passenger is travelling.
    The tickets list includes, for each ticket, the ticket number and destination city. The cities list includes, for
    each city, the city name and the country it belongs to. The destination city can be calculated using ticket_number,
    and the destination country can be calculated using the city name.
    If ticket_number is not found within the tickets in the list, it returns None.
    If the city name can't be found in the cities list, it returns None.
    Suggestion: use the find_country() function above.
    Example:
        find_destination(
                         [(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow")],
                         [("Buenos Aires", "Argentina"), ("Glasgow", "Scotland"), ("Liverpool", "England"),
                                                                                      ("Madrid", "Spain")],
                         100)
        -> "Argentina"
    -Parameters:
        -tickets (list; elements: tuples containing 2 elements: int, str): list with ticket information. Each ticket is
        represented by a tuple with the following structure: (ticket number, destination city).
        -cities (list; elements: tuples containing 2 elements: str, str): list with city information. Each city is
        represented by a tuple with the following structure: (city name, country it belongs to).
        -ticket_number (int): a ticket number.
    -Returns:
        (str) Name of the destination country to which the city associated to ticket_number belongs.
    """
        </pre>
    </summary>
    <pre>
    for ticket in tickets:
        if ticket_number == ticket[0]:
            return find_country(cities, ticket[1])
    return None
    </pre>
</details>


# Sets and dictionaries

<details>
    <summary>
        <pre>
def find_duplicates(strings1, strings2):
    """
    Given two lists with string elements, returns which strings are included in both lists.
    Suggestion: avoid using a loop to iterate over lists.
    Examples:
        find_duplicates(["abc", "cde", "abc", "fff"], ["cde", "aaa"]) -> {"cde"}
    -Parameters:
        strings1 (list; elements: str): list with strings.
        strings2 (list; elements: str): list with strings.
    -Returns:
        (set; elements: str) Every string that is included in both strings1 and strings2.
    """
        </pre>
    </summary>
    <pre>
    return set(strings1) & set(strings2)
    </pre>
</details>


<details>
    <summary>
        <pre>
def only_one_pet_type(dogs, cats):
    """
    Given a list with pet owners that have dogs and another list with those that have cats (where the same owner
    can be included in both lists, if they have both types of pets), returns which owners have only one pet type (either
    dog or cat, but not both).
    Suggestion: avoid using a loop to iterate over lists.
    Example:
        only_one_pet_type(["Lucrezia Georgia", "John Sebastian Batch", "Christopher Colum"],
                          ["John Sebastian Batch", "Jon Jack Russo", "Anna Bologna", "Christopher Colum"])
        -> {"Lucrezia Georgia", "Jon Jack Russo", "Anna Bologna"}
    -Parameters:
        dogs (list; elements: str): list with dog owner names.
        cats (list; elements: str): list with cat owner names.
    -Returns:
        (set; elements: str) Names of pet owners that either have dog(s) or cat(s) but not both pet types.
    """
        </pre>
    </summary>
    <pre>
    return set(dogs) ^ set(cats)
    </pre>
</details>


<details>
    <summary>
        <pre>
def unique_elements(tuples):
    """
    Given an undetermined number of tuples containing numbers, returns a tuple combining all other tuples, where each
    number is only included once (no duplicates).
    Suggestion: use a set to remove duplicates.
    Example:
        unique_elements([(1, 2, 3), (2, 2, 2, 2), (3, 4, 5), (1, 3, 5, 7, 9)]) -> (1, 2, 3, 4, 5, 7, 9)
    -Parameter:
        tuples (list; elements: tuples containing int elements): list containing tuples with numbers.
    -Returns:
        (tuple; elements: int) Tuple where all numbers from tuples in the list are combined and unique.
    """
        </pre>
    </summary>
    <pre>
    unique = set()
    for element in tuples:
        unique.update(element)
    return tuple(unique)
    </pre>
</details>


<details>
    <summary>
        <pre>
def unique_last_names(students):
    """
    Given a list with name and last name of school students, returns a structure with just the last names, without
    duplicates. Each student name is represented as a single string, where names are separated by a space. Also, a
    student might have more than one name but only one last name, with the following structure: "name(s) last_name".
    Example:
        unique_last_names(["Maude Baker", "Milton Llewellyn Davis", "Leela Evans", "Keelan Davis"])
        -> {"Baker", "Davis", "Evans"}
    -Parameter:
        students (list; elements: str): list with student names.
    -Returns:
        (set; elements: str) Set with unique last names from the students list.
    """
        </pre>
    </summary>
    <pre>
    last_names = set()
    for student in students:
        last_name = student.split()[-1]
        last_names.add(last_name)
    return last_names
    </pre>
</details>


<details>
    <summary>
        <pre>
def billing_addresses(sales):
    """
    Given a list with information about some company sales during a one-month period, containing tuples with each sale:
    (customer name, day of the month, order amount, billing address), returns all billing addresses from customers. Each
    customer might have placed more than one order and on different days of the month, so their address should only
    be included once.
    Example:
        billing_addresses([("Stephan Carey", 5, 1250.23, "355 Boulevard St."),
                           ("Jocelyn Harris", 7, 699, "218 Main St."),
                           ("Stephan Carey", 7, 532.90, "355 Boulevard St."),
                           ("Frances Adams", 12, 57.99, "761 South Rd."),
                           ("Jocelyn Harris", 15, 958, "218 Main St.")])
        -> {'355 Boulevard St.', '218 Main St.', '761 South Rd.'}
    -Parameter:
        sales (list; elements: tuples containing str, int, float, str): list with tuples representing each sale during
        a specific month.
    -Returns:
        (set; elements: str) A set with all billing addresses from customers who placed orders during a specific month.
    """
        </pre>
    </summary>
    <pre>
    addresses = set()
    for sale in sales:
        addresses.add(sale[3])
    return addresses
    </pre>
</details>


<details>
    <summary>
        <pre>
def add_movie(movies, movie):
    """
    Adds movie information to a dictionary and returns the modified dictionary. If the movie is already present, it
    replaces it with the new information. The information included in the movie parameter is: title, director name,
    release year. The dictionary will use the movie title as a key, and a list with the rest of the information as a
    value.
    Example:
        add_movie({"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]},
                  ("Lord of the rings: The two towers", "Peter Jackson", 2002))
        -> {"Joker": ["Todd Phillips", 2019],
            "Avatar": ["James Cameron", 2009],
            "Lord of the rings: The two towers": ["Peter Jackson", 2002]}
    -Parameters:
        movies (dict; key: str; value: list containing 2 elements, str and int): dictionary with movies.
        movie (tuple; elements: str, str, int): tuple with information of the movie that will be added: title, director
        name, release year.
    -Returns:
        (dict; key: str; value: list containing 2 elements, str and int) The "movies" dictionary with the new movie
        added to it.
    """
        </pre>
    </summary>
    <pre>
    if movie:
        movies[movie[0]] = [movie[1], movie[2]]
    return movies
    </pre>
</details>


<details>
    <summary>
        <pre>
def most_voted(votes, grade):
    """
    Given a dictionary with student votes for "class leader" in a school, and given a grade ID number, returns the names
    of all students that were voted, without duplicates. The dictionary keys represent grade IDs, while the values are
    lists containing strings with each voted student.
    If the grade ID is not found in the dictionary, returns an empty set.
    Example:
        most_voted({1: ["john", "john", "laura", "john", "laura", "paula"],
                    2: ["amy", "sean", "olivia", "olivia"],
                    3: ["liam", "sophie", "liam", "sophie", "sophie", "isabella", "sophie"]},
                   3)
        -> {"liam", "sophie", "isabella"}
    -Parameters:
        votes (dict; key: int, value: list containing str): the votes issued in each grade.
        grade (int): the ID number of a class (to get the names of class students that were voted for).
    -Returns:
        (set; elements: str), The students that were voted for in the given grade.
    """
        </pre>
    </summary>
    <pre>
    if grade in votes:
        return set(votes[grade])
    else:
        return set()
    </pre>
</details>


<details>
    <summary>
        <pre>
def digit_occurrence(digits):
    """
    Given a list with numbers, returns occurrences for each digit (from 0 to 9). Digits that are not in the list will
    have a 0 occurrence value.
    Example:
        digit_occurrence([8, 9, 0, 4, 2, 2, 4, 1, 8, 2]) -> {0: 1, 1: 1, 2: 3, 3: 0, 4: 2, 5: 0, 6: 0, 7: 0, 8: 2, 9: 1}
    -Parameter:
        digits (list; elements: int): list containing only integer digits (from 0 to 9).
    -Returns:
        (dict; key: int; value: int) Dictionary with occurrences of each digit, where keys are numbers from 0 to 9.
    """
        </pre>
    </summary>
    <pre>
    occurrences = {}
    for i in range(10):
        occurrences[i] = 0
    for digit in digits:
        occurrences[digit] += 1
    return occurrences
    </pre>
</details>


<details>
    <summary>
        <pre>
def count_occurrences(lists_tuple):
    """
    Given a tuple containing lists of single characters (strings of length 1), counts the occurrences of each character
    in the overall lists.
    Example:
        count_occurrences(
                          (["i", "%", "u"],
                           ["^", "%", "^", "s", "i", "i", "u"],
                           ["a", "u"]))
        ->  {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
    -Parameter:
        lists (tuple; elements: list: containing str) tuple containing lists where the elements are characters (length 1
        str).
    -Returns:
        (dict; key: str; value: int) Dictionary with occurrences of each character.
    """
        </pre>
    </summary>
    <pre>
    occurrences = {}
    for a_list in lists_tuple:
        for letter in a_list:
            if letter not in occurrences:
                occurrences[letter] = 1
            else:
                occurrences[letter] += 1
    return occurrences
    </pre>
</details>


<details>
    <summary>
        <pre>
def highest_value(occurrences):
    """
    Given a dictionary with positive int values that are unique, returns the key associated to the highest value. If the
    dictionary is empty, it returns an empty string.
    Example:
        highest_value({"a": 1, "e": 7, "i": 4, "o": 9, "u": 3}) -> "o"
    -Parameter:
        occurrences (dict; key: str; value: int): dictionary where the keys are strings representing letters in the
        English alphabet and values represent occurrences of each letter. There is only one highest value, as values
        are unique.
    -Returns:
        (str) The key associated to the highest value. Empty string if the dictionary is empty.
    """
        </pre>
    </summary>
    <pre>
    highest_value_so_far = -1
    associated_key_so_far = ""
    for key, value in occurrences.items():
        if value > highest_value_so_far:
            highest_value_so_far = value
            associated_key_so_far = key
    return associated_key_so_far
    </pre>
</details>


<details>
    <summary>
        <pre>
def sowing_season(vegetables, month):
    """
    Given a dictionary with sowing months of a series of vegetables, and a specific month, returns which vegetables can
    be sown in that month.
    Example:
        sowing_season({"spinach": ["february", "march"],
                       "garlic": ["february", "march", "april"],
                       "eggplant": ["july", "august", "september"]},
                      "march"),
        -> ["spinach", "garlic"]
    -Parameters:
        vegetables (dict; key: str; value: list containing str): dictionary where keys are the names of vegetables and
        values are lists with the months in which each vegetable can be sown.
        month (str): month to find which vegetables can be sown.
    -Returns:
        (list; elements: str) List with vegetables that can be sown in the given month.
    """
        </pre>
    </summary>
    <pre>
    vegetables_sown = []
    for key, value in vegetables.items():
        if month in value:
            vegetables_sown.append(key)
    return vegetables_sown
    </pre>
</details>


<details>
    <summary>
        <pre>
def register_payment(members, number):
    """
    Given a dictionary with information about members of a club, and a member number, modifies the dictionary to
    indicate that their membership fees are up to date. The keys in the dictionary represent member numbers while values
    are lists with member information: [name, phone, fee status (True if fees are up to date, False if not)].
    Example:
        register_payment({423: ["Darlene Johnson", 4523114, True],
                          289: ["Anna Brown", 6345112, False],
                          657: ["Steven Lloyd", 4767992, False]},
                         289),
        -> {423: ["Darlene Johnson", 4523114, True],
           289: ["Anna Brown", 6345112, True],
           657: ["Steven Lloyd", 4767992, False]}
    -Parameters:
        members (dict; key: int; value: list containing 3 elements: str, int, bool): dictionary with information
        about club members. All keys are positive numbers.
        number (int): member number where the payment status will be modified.
    -Returns:
        (dict; key: int; value: list containing 3 elements: str, int, bool) Dictionary with information about club
         members, where the fee status has been updated (if the member number exists and is False).
    """
        </pre>
    </summary>
    <pre>
    if number in members:
        members[number][2] = True
    return members
    </pre>
</details>


<details>
    <summary>
        <pre>
def late_payments(members):
    """
    Given a dictionary with information about members of a club, returns how many of them are late with their membership
    fee payments. The keys in the dictionary represent member numbers while values are lists with member information:
    [name, phone, fee status (True if fees are up to date, False if not)].
    Example:
        late_payments({423: ["Darlene Johnson", 4523114, True],
                       289: ["Anna Brown", 6345112, False],
                       657: ["Steven Lloyd", 4767992, False]}),
        -> 2
    -Parameter:
        members (dict; key: int; value: list containing 3 elements: str, int, bool): dictionary with information
        about club members. All keys are positive numbers.
    -Returns:
        (int) How many club members are late in fulfilling their membership fees.
    """
        </pre>
    </summary>
    <pre>
    debtors = 0
    for member_info in members.values():
        if not member_info[2]:
            debtors += 1
    return debtors
    </pre>
</details>


<details>
    <summary>
        <pre>
def delete_member(members, member_name):
    """
    Given a dictionary with information about members of a club and a member name, it deletes the member from the
    dictionary. The keys in the dictionary represent member numbers while values are lists with member information:
    [name, phone, fee status (True if fees are up to date, False if not)]. If the given name does not match any member,
    the dictionary is not modified.
    Example:
        delete_member({423: ["Darlene Johnson", 4523114, True],
                       289: ["Anna Brown", 6345112, False],
                       657: ["Steven Lloyd", 4767992, False]},
                       "Anna Brown"),
        -> {423: ["Darlene Johnson", 4523114, True],
            657: ["Steven Lloyd", 4767992, False]}
    -Parameters:
        members (dict; key: int; value: list containing 3 elements: str, int, bool): dictionary with information
        about club members. All keys are positive numbers. Member names are unique in the dictionary values.
        member_name (str): name and last name (word separator: space) of the member that will be deleted.
    -Returns:
        (dict; key: int; value: list containing 3 elements: str, int, bool): Dictionary with member information where
        a member has been deleted, if it existed.
    """
        </pre>
    </summary>
    <pre>
    number_to_delete = -1
    for number, member_info in members.items():
        if member_name == member_info[0]:
            number_to_delete = number
            break
    if number_to_delete != -1:
        del members[number_to_delete]
    return members
    </pre>
</details>


<details>
    <summary>
        <pre>
def roman_to_arabic(roman):
    """
    Given a Roman numeral, returns its Arabic form, in base 10 (using simplified rules).
    The conversion chart is as follows: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
    Rules:
    Any letter repeated up to three times: they're added.
    I before V or X means to substract 1.
    X before L or C means to substract 10.
    C before D or M means to substract 100.
    Example:
        roman_to_arabic("MCMLXXIV") -> 1974
    -Parameter:
        roman (str): Roman numeral to be converted. The roman numeral will be all upper-case, will be a valid Roman
        numeral and its Arabic form will be a base-ten number between 1 and 3999.
    -Returns:
        (int) Base 10 Arabic numeral that is the converted form of roman.
    """
        </pre>
    </summary>
    <pre>
    equivalences = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    arabic = 0
    for i in range(len(roman) - 1):
        if equivalences[roman[i]] < equivalences[roman[i + 1]]:
            arabic -= equivalences[roman[i]]
        else:
            arabic += equivalences[roman[i]]
    arabic += equivalences[roman[len(roman) - 1]]
    return arabic
    </pre>
</details>


<details>
    <summary>
        <pre>
def phone_number(phone):
    """
    Given a phone number containing letters, returns its numeric form. The given phone number will only contain numbers,
    upper case letters, '-', '(' and ')'. Only letters will be converted, leaving numbers and other symbols unchanged.
    The letter-number correspondence is as follows:
    A, B, C = 2
    D, E, F = 3
    G, H, I = 4
    J, K, L = 5
    M, N, O = 6
    P, Q, R, S = 7
    T, U, V = 8
    W, X, Y, Z = 10
    Example:
        phone_number("(325)444-TEST") -> "(325)444-8378"
    -Parameter:
        phone (str): a phone number that might contain upper-case letters, numbers, hyphens and parentheses.
    -Returns:
        (str) The phone number with its letters converted into its numeric form.
    """
        </pre>
    </summary>
    <pre>
    result = ""
    equivalences = {'2': "ABC", '3': "DEF", '4': "GHI", '5': "JKL", '6': "MNO", '7': "PQRS", '8': "TUV", '9': "WXYZ"}
    dont_convert = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '-')
    for character in phone:
        if character in dont_convert:
            result += character
        else:
            for number, letters in equivalences.items():
                if character in letters:
                    result += number
                    break
    return result
    </pre>
</details>


<details>
    <summary>
        <pre>
def isomorphic_strings(string1, string2):
    """
    Given two text strings, decides if they are isomorphic. Two strings, a and b, are isomorphic if the characters in a
    can be replaced to get b. All occurrences of a character must be replaced with another character while preserving
    the order of characters. There can't be two different characters replaced by the same character. A character can
    replace itself. Both strings have the same length and are conformed by valid ascii characters.
    Examples:
        isomorphic_strings("paper", "title") -> True
        (since we can replace: 'p'='t'; 'a'='i'; p'='t'; 'e'='l'; 'r'='e').
        isomorphic_strings("paper", "yoyos") -> False
        (Since we can replace: 'p'='y'; 'a'='o'; p'='y'; but when we try to replace 'e' with 'o' we find that 'o' was
        already a replacement for 'a').
    -Parameters:
        string1 (str): a string to be processed. len(string1) == len(string2).
        string2 (str): a second string, to verify if it's isomorphic in relation to string1.
    -Returns:
        (bool) True if strings are isomorphic, False if they aren't.
    """
        </pre>
    </summary>
    <pre>
    equivalences = {}
    already_used = set()
    char_count = len(string1)
    for i in range(char_count):
        if string1[i] not in equivalences:
            if string2[i] not in already_used:
                equivalences[string1[i]] = string2[i]
                already_used.add(string2[i])
            else:
                return False
        else:
            if equivalences[string1[i]] != string2[i]:
                return False
    return True
    </pre>
</details>


<details>
    <summary>
        <pre>
def word_pattern(pattern, words):
    """
    Given a pattern and a string containing words, decides if the words follow the pattern, so that there is a bijection
    between a letter in the pattern and a word in the string. We say the string "follows" the pattern if every letter in
    the pattern can be replaced with a word from the string, and every letter is replaced with just one word. Each word
    in the string must have a replacement letter in the pattern and each letter in the pattern must replace a word in
    the string.
    Examples:
        word_pattern("xyyx", "home sea sea home") -> True
        (Since we can match 'x'='home'; 'y'='sea').
        word_pattern("xyyx", "home sea sea hill") -> False
        (Since 'x' cannot be matched both to 'home' and 'hill' at the same time).
    -Parameters:
        pattern (str): a pattern that only contains lower case letters.
        words (str): a string with words, which will be separated by a single space. There will be no leading or
        trailing spaces in the string. Words will only contain lower case letters and the ' ' character.
    -Returns:
        (bool) True if the words in the string follow the given pattern. False if they don't or any string is empty.
    """
        </pre>
    </summary>
    <pre>
    pattern_matching = {}
    words_list = words.split()
    if len(pattern) != len(words_list) or len(pattern) == 0 or len(words_list) == 0:
        return False
    for i in range(len(pattern)):
        if pattern[i] not in pattern_matching:
            pattern_matching[pattern[i]] = words_list[i]
        else:
            if pattern_matching[pattern[i]] != words_list[i]:
                return False
    return True
    </pre>
</details>
