
# main.py advanced functions

def is_even(number: int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: The integer number to check whether it is even.
    :return: Boolean, True if the number is even and False if it is odd.
    """
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: The string to check for vowels.
    :return: The number of vowels in the string.
    """
    count = 0
    text = text.lower()
    for character in text:
        if character in 'aeiou':
            count += 1
    return count


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: The temperature in Celsius.
    :return: The temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def reverse_text(text: str) -> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: The string to reverse.
    :return: The reversed string.
    """
    reversed_string = ""
    for character in range(len(text) - 1, -1, -1):
        reversed_string += text[character]
    return reversed_string

def larger_number(a: int, b: int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: The first integer.
    :param b: The second integer.
    :return: The larger of the two integers.
    """
    if a > b:
        return a
    else:
        # If a == b, the integers are equal, so we can return either value.
        return b


def average_two(a: int, b: int) -> float:
    """Calculate and return the average of two integers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The average of the two integers.
    """
    return (a + b) / 2


def can_afford(balance: float, cost: float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: The current balance (float).
    :param cost: The cost of the item (float).
    :return: True if the balance is greater than or equal to cost, False otherwise.
    """
    if balance >= cost:
        return True
    else:
        return False


def repeat_text(text: str, times: int) -> str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: The string to repeat.
    :param times: The number of times to repeat the string.
    :return: A string containing the repeated text.
    """
    return text * times


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: The sentence to search in.
    :param word: The word to search for.
    :return: True if the word is found, False otherwise.
    """
    if word in sentence:
        return True
    else:
        return False


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: The total cost of the item.
    :param percent: The percentage of the cost to give as a tip.
    :return: The amount of tip to give.
    """
    return cost * (percent / 100)


def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: The first name.
    :param last_name: The last name.
    :return: A string containing the uppercase first letters of the two names.
    """
    first_name_initial = first_name[0].upper()
    last_name_initial = last_name[0].upper()
    return first_name_initial + last_name_initial


def percent_score(points: float, possible: float) -> float:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: The points earned.
    :param possible: The possible points.
    :return: The percentage of points earned.
    """
    if possible < 1:
        return None
    # Do we need to check if points are less than possible?
    return (points / possible) * 100


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: The number to check.
    :param minimum: The minimum value.
    :param maximum: The maximum value.
    :return: True if the number is between the minimum and maximum, False otherwise.
    """
    if minimum <= number <= maximum:
        return True
    else:
        return False


def all_different(a: str, b: str, c: str) -> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a: The first string.
    :param b: The second string.
    :param c: The third string.
    :return: True if all three strings are different, False otherwise.
    """
    if a != b and b != c and a != c:
        return True
    else:
        return False


def average_three(a: int, b: int, c: int) -> float:
    """Calculate and return the average of three integers.

    :param a: The first integer.
    :param b: The second integer.
    :param c: The third integer.
    :return: The average of the three integers.
    """
    return (a + b + c) / 3


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: The temperature to describe.
    :param cold_limit: The limit below which the temperature is considered cold.
    :param hot_limit: The limit above which the temperature is considered hot.
    :return: A string describing the temperature.
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"


# START of Advanced Functions
# I reused previous functions from Basic
def temperature_in_safe_range(celsius: float, minimum_f: float, maximum_f: float) -> bool:
    """Return whether a Celsius temperature is within Fahrenheit limits.

    :param celsius: The temperature in Celsius.
    :param minimum_f: The minimum safe temperature in Fahrenheit.
    :param maximum_f: The maximum safe temperature in Fahrenheit.
    :return: True if the converted temperature is within the range.
    """
    convert_temperature = celsius_to_fahrenheit(celsius)
    return is_between(convert_temperature, minimum_f, maximum_f)


def can_afford_with_tip(balance: float, cost: float, tip_percent: float) -> bool:
    """Return whether balance covers the cost plus its tip.

    :param balance: The available balance.
    :param cost: The original cost.
    :param tip_percent: The tip percentage applied to the cost.
    :return: True if the balance covers the complete total.
    """
    tip = calculate_tip(cost, tip_percent)
    total_cost = cost + tip
    return can_afford(balance, total_cost)


def meets_average(score1: float, score2: float, score3: float, required_average: float) -> bool:
    """Return whether the average of three scores meets the requirement.

    :param score1: The first score.
    :param score2: The second score.
    :param score3: The third score.
    :param required_average: The minimum required average.
    :return: True if the average is greater than or equal to the requirement.
    """
    average = average_three(score1, score2, score3)
    if average >= required_average:
        return True
    else:
        return False


def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """Return whether a person's initials match the expected initials.

    Capitalization is ignored when comparing the initials.

    :param first_name: The person's first name.
    :param last_name: The person's last name.
    :param expected_initials: The initials to compare against.
    :return: True if the initials match, ignoring capitalization.
    """
    initials = make_initials(first_name, last_name)
    if initials.upper() == expected_initials.upper():
        return True
    else:
        return False

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """

    # Tested two cases for each function

    print("temperature_in_safe_range:", temperature_in_safe_range(20, 60, 75))
    print("temperature_in_safe_range:", temperature_in_safe_range(0, 33, 40))

    print("can_afford_with_tip:", can_afford_with_tip(25, 20, 15))
    print("can_afford_with_tip:", can_afford_with_tip(22, 20, 15))

    print("meets_average:", meets_average(80, 90, 100, 90))
    print("meets_average:", meets_average(60, 70, 80, 75))

    print("initials_match:", initials_match("Ada", "Lovelace", "al"))
    print("initials_match:", initials_match("Ada", "Lovelace", "ab"))