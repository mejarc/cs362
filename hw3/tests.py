import unittest
import random
from credit_card_validator import credit_card_validator


def generate_credit_card_number(length):
    result = ''
    for _ in range(length):
        result += str(random.randint(0, 9))
    # returns credit card number as a string
    return result


class TestCreditCardValidator(unittest.TestCase):
    def test1(self):
        tests_to_generate = 502000
        for _ in range(tests_to_generate):
            length = random.randint(15, 17)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)


if __name__ == '__main__':
    unittest.main()
