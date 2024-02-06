import unittest
import random
from credit_card_validator import credit_card_validator


def generate_credit_card_number(length):
    random.seed()
    result = ''
    for _ in range(length):
        result += str(random.randint(0, 9))
    # returns credit card number as a string
    return result


class TestCreditCardValidator(unittest.TestCase):
    def test1(self):
        tests_to_generate = 4000
        for _ in range(tests_to_generate):
            random.seed()
            length = random.randint(0, 4)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test2(self):
        tests_to_generate = 3000
        for _ in range(tests_to_generate):
            random.seed()
            length = random.randint(10, 14)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test3(self):
        tests_to_generate = 5000
        for _ in range(tests_to_generate):
            random.seed()
            length = random.randint(15, 16)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test4(self):
        tests_to_generate = 5000
        for _ in range(tests_to_generate):
            random.seed()
            length = random.randint(17, 23)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test5(self):
        tests_to_generate = 6000
        for _ in range(tests_to_generate):
            random.seed()
            length = random.randint(9, 15)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)

    def test6(self):
        tests_to_generate = 3300
        for _ in range(tests_to_generate):
            random.seed()
            length = random.randint(4, 9)
            credit_card_number = generate_credit_card_number(length)
            credit_card_validator(credit_card_number)


if __name__ == '__main__':
    unittest.main()
