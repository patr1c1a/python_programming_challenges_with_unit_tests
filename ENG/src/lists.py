##################################
#    TOPIC: LISTS AND TUPLES     #
##################################


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass
    

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
    pass


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
    pass


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
    pass


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
    pass
    

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
    pass


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
    pass
        

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
    pass


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
    pass


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
    pass


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
    pass


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
    pass
