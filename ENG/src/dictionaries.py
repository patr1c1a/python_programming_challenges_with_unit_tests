##################################
#  TOPIC: SETS AND DICTIONARIES  #
##################################


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


def highest_value(occurrences):
    """
    Given a dictionary with positive int values that are unique, returns the key associated to the highest value. If the
    dictionary is empty, it returns an empty string.
    Suggestion: avoid using max().
    Example:
        highest_value({"a": 1, "e": 7, "i": 4, "o": 9, "u": 3}) -> "o"
    -Parameter:
        occurrences (dict; key: str; value: int): dictionary where the keys are strings representing letters in the
        English alphabet and values represent occurrences of each letter. There is only one highest value, as values
        are unique.
    -Returns:
        (str) The key associated to the highest value. Empty string if the dictionary is empty.
    """
    pass


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
    pass


def register_payment(members, number):
    """
    Given a dictionary with information about members of a club, and a member number, modifies the dictionary to
    indicate that their membership fees are up-to-date. The keys in the dictionary represent member numbers while values
    are lists with member information: [name, phone, fee status (True if fees are up-to-date, False if not)].
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
    pass


def late_payments(members):
    """
    Given a dictionary with information about members of a club, returns how many of them are late with their membership
    fee payments. The keys in the dictionary represent member numbers while values are lists with member information:
    [name, phone, fee status (True if fees are up-to-date, False if not)].
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
    pass


def delete_member(members, member_name):
    """
    Given a dictionary with information about members of a club and a member name, it deletes the member from the
    dictionary. The keys in the dictionary represent member numbers while values are lists with member information:
    [name, phone, fee status (True if fees are up-to-date, False if not)]. If the given name does not match any member,
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
    pass


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
    pass


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
    pass


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
    pass


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
        (bool) True if the words in the string follow the given pattern. False if they don't.
    """
    pass
