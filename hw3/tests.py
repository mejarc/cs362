import unittest
import random
from credit_card_validator import credit_card_validator


# TODO: your tests MUST be random.
# TODO: You may not have tests that have hardcoded credit card numbers in them.
# TODO: you may not have more than 4 digits of a number hardcoded
# into any given random test generator for a prefix
# TODO: You also cannot hard code numbers at the end or in the middle
# Therefore, don't worry about asserting; just call
# the function-under-test (credit_card_validator).
# TODO: Tests must run within 25 seconds on Gradescope.
# See Gradescope results for your test runtime.

def generate_credit_card_number(prefix, length):
    result = str(prefix)
    for i in range(length - 1):
        result += str(random.randint(0, 9))
    # returns credit card number as a string
    return result


'''Luhn's algorithm implementation
Adapted from URL: https://en.wikipedia.org/wiki/Luhn_algorithm
Author: Wikipedia contributors
Adapted by: Melanie Archer
'''


def generate_checksum(credit_card_number):
    # Note that credit_card_number is a string
    sum = 0
    # start from the rightmost digit. Moving left,
    # double the value of every second digit
    # (including the rightmost digit).

    for i in range(len(credit_card_number) - 1, -1, -2):
        digit = int(credit_card_number[i]) * 2
        if digit > 9:
            digit -= 9
        sum += digit
        if (sum % 10) == 0:
            return 0
        else:
            return (10 - (sum % 10)) % 10


class TestCreditCardValidator(unittest.TestCase):
    def test1(self):
        # Visa of valid prefix, valid checksum, but invalid length
        tests_to_generate = 5

        # edge cases are lengths
        edge_cases = [10, 15, 17, 19]

        for i in range(tests_to_generate):
            # chances of generating edge cases
            odds = random.randint(0, 1)
            if odds == 0:
                length = random.choice(edge_cases)
            else:
                length = random.randint(1, 20)

            credit_card_number = generate_credit_card_number(4, length)
            checksum = generate_checksum(credit_card_number)
            credit_card_number += str(checksum)
            expected = True
            if length != 16:
                expected = False

            # generate error message
            if credit_card_validator(credit_card_number) != expected:
                print('Test 1 failure: {} should be {}'
                      .format(credit_card_number, expected))


if __name__ == '__main__':
    unittest.main()
