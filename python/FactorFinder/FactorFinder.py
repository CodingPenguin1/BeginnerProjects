""" Factor Finder

Gets an integer from the user, then prints out the factors of that number in ascending order
"""

def getFactors(number):
    """ Returns a sorted list of the factors of the parameter

    Args:
        number (int): the integer to find the factors of

    Returns:
        A sorted list of the factors of `number`
    """

    # Store the factors in a list since we don't know how many we'll have
    factors = []

    # Iterate through all the numbers <= number.
    # "Technically" we only need to go up to the square root of the number,
    # as long as we add the number itself to the list later.
    # However, there are many other better ways of finding factors,
    # and this is just a tutorial.
    # If you have a problem with it, write a better getFactors() function!
    # It'll be good practice.
    # Note here that range() returns a range-type variable, which is iterable.
    # The range() function is inclusive with the starting parameter and exclusive with the end parameter,
    # which is why we need to go to number + 1
    for potentialFactor in range(1, number + 1):
        # If the number divided by the potential factor has no remainders
        # the potential factor is a factor and should be added to the list
        if number % potentialFactor == 0:
            factors.append(potentialFactor)

    # Sort the list
    factors.sort()

    # Return the list
    return factors


if __name__ == '__main__':
    # Initialize a number variable
    number = 0

    # Get an integer from the user
    while True:
        ipt = input('Enter an integer to find the factors of: ')

        # Python takes in all keyboard input as a string,
        # so we want to try to cast it as an integer.
        # Without the try/except block, the program would crash if the
        # user inputted something that we can't cast into an integer (ex. "hello").
        try:
            number = int(ipt)
            # If we CAN cast the input to an integer, it's probably a valid input
            # However, we want positive numbers, so make sure it's > 0 before we exit the input loop
            if number > 0:
                break
        # Python has many kinds of exceptions, but since we only care about one, putting a general Exception here is ok
        # I recommend reading more about Python's exceptions here:
        # https://docs.python.org/2/library/exceptions.html
        except Exception:
            # The "pass" keyword in Python means "do nothing"
            # We could print out some error message about the input not being valid instead,
            # but I wanted to throw a pass in here for the sake of learning
            pass

    # Now that we gave a number, let's find the factors
    factors = getFactors(number)

    # The str.join(iterable) method requires the iterable to only contain strings,
    # so let's cast all the elements to strings.
    # This is a fancy thing called inline list comprehension.
    # You can read more here in section 5.1.3:
    # https://docs.python.org/3/tutorial/datastructures.html
    factors = [str(i) for i in factors]

    # Print all of the factors
    print(', '.join(factors))
