"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def town_name(string):
    """Takes a string and determines if it is my hometown Champaign.  Returns
    True if it is my hometown, and False if otherwise.  Also checks if the string 
    is a word, versus string of non-alphabetic characters.

    >>> town_name("Chicago")
    False

    >>> town_name("Champaign")
    True

    """
    try:
        string.isalpha()
    except AttributeError or SyntaxError or False:
        print "Give only town names."

    if string == "Champaign":
        return True
    else:
        return False



#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def one_string_from_two(first_name, last_name):
    """Returns a first name and last name as one concatenation.

    >>> one_string_from_two("Jenny", "Justh")
    'Jenny Justh'

    >>> one_string_from_two("Bobby", "Smith")
    'Bobby Smith'

    """
    try:
        first_name.isalpha() and last_name.isalpha()
    except AttributeError:
        print "Give only names."

    return first_name + " " + last_name

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

def greeting(hometown, first_name, last_name):
    if town_name(hometown):
        print "Hi," + " " + one_string_from_two(first_name, last_name) + ", " + "we're from the same place!"
    else:
        print "Hi " + one_string_from_two(first_name, last_name) + ", I'd like to visit " + hometown + "!"



###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """
    try:
        fruit.isalpha()
    except SyntaxError or False:
        print "You must type in a word."
    
    if fruit == "raspberry" or fruit == "blackberry" or fruit == "strawberry":
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    try:
        fruit.isalpha()
    except SyntaxError or False:
        print "You must type in a word."

    fruit_type = is_berry(fruit)

    if fruit_type == True:
        return 0
    else:
        return 5


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """
    try:
        for item in lst:
            int(item)
    except SyntaxError or ValueError:
            print "You must give numbers."

    lst.append(num)
    return lst

def calculate_price(price, state, tax = 0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    try:
        int(price)
    except SyntaxError or ValueError:
        print "You must give numbers."

    try:
        state.isalpha()
    except ValueError or False:
        print "You must type in a state abbreviation with two letters."

    try:
        float(tax)
    except SyntaxError or ValueError:
        print "You must give numbers."

    if type(tax) == 'int':
        tax == tax * (.01) 

    if state == "CA":
        total_price = price + (price * tax)
        total = total_price + (total_price * 0.03)
        return total
    elif state == "NM":
        total_price = price + (price * tax)
        return total_price
    elif state == "OR":
        total_price = price + (price * tax) 
        return total_price
    elif state == "PA":
        total_price = price + (price * tax)
        price = total_price + 2.00
        return price
    elif state == "MA":
        total_price = price + (price * tax)
        if total_price < 100:
            total = total_price + 1.00
            return total
        elif total_price >= 100:
            total = total_price + 3.00
            return total
    

###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

def adding_to_list(lst, *args):
    """Takes in any number of arguments and adds them to a list.

    >>> adding_to_list([1, 2], 3, 4, 5, 6)
    [1, 2, 3, 4, 5, 6]

    >>> adding_to_list(['a', 'b'], 'c', 'd', 'e')
    ['a', 'b', 'c', 'd', 'e']

    """

    for i in args:
        lst.append(i)

    return lst

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def nested_function(word):
    final_result = ()
    final_result = final_result + (word,) 
    def inner_function(word):
        final_words = word * 3
        final_result = final_result + (final_words,)
        return final_result
    print inner_function(word)
   




###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
