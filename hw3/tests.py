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
        tests_to_generate = 270
        for _ in range(tests_to_generate):
            length = random.randint(10, 15)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test2(self):
        tests_to_generate = 330
        for _ in range(tests_to_generate):
            length = random.randint(10, 17)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test3(self):
        tests_to_generate = 450
        for _ in range(tests_to_generate):
            length = random.randint(15, 16)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test4(self):
        tests_to_generate = 330
        for _ in range(tests_to_generate):
            length = random.randint(14, 17)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test5(self):
        tests_to_generate = 330
        for _ in range(tests_to_generate):
            length = random.randint(9, 23)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)


if __name__ == '__main__':
    unittest.main()
