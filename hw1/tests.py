import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        """Verifies that credit card with no number returns False
        Picked using Error Guessing
        """
        self.assertFalse(credit_card_validator(" "))

    def test2(self):
        """Verifies that credit card with less < 10 numbers returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("333333333"))

    def test3(self):
        """Verifies that credit card with > 19 numbers returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("33333333333333333333"))

    def test4(self):
        """Verifies that credit card with first digit 6 returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("6333333333"))

    def test5(self):
        """Verifies that credit card with first digit 7 returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("7333333333"))

    def test6(self):
        """Verifies that Amex starting with 3,
        length = 15, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator("333333333333337"))

    def test7(self):
        """Verifies that Visa starting with 4,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator("4333333333333339"))

    def test8(self):
        """Verifies that Mastercard starting with 2333,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator("2333333333333333"))

    def test9(self):
        """Verifies that Mastercard starting with 50,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("5033333333333339"))

    def test10(self):
        """Verifies that Amex starting with 33,
        length = 15, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("333333333333337"))

    def test11(self):
        """Verifies that Amex starting with 38,
        length = 15, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("383333333333336"))

    def test12(self):
        """Verifies that Amex starting with 36,
        length = 15, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("363333333333330"))

    def test13(self):
        """Verifies that Mastercard starting with 56,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("5633333333333333"))

    def test14(self):
        """Verifies that Mastercard starting with 2220,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("2220333333333339"))

    def test15(self):
        """Verifies that Mastercard starting with 2721,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator("2721333333333333"))

    def test16(self):
        """Verifies that Mastercard starting with 2500,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator("2500333333333330"))

    def test17(self):
        """Verifies that Mastercard starting with 52,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator("5233333333333337"))

    def test18(self):
        """Verifies that Visa starting with 4,
        length = 15, valid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("433333333333336"))

    def test19(self):
        """Verifies that Mastercard starting with 52,
        length = 15, valid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator("523333333333337"))

    def test20(self):
        """Verifies that Mastercard starting with 2720,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator("2720333333333334"))

    def test21(self):
        """Verifies that Amex starting with 3,
        length = 15, invalid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator("333333333333331"))

    def test22(self):
        """Verifies that Visa starting with 4,
        length = 16, invalid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator("4333333333333338"))

    def test23(self):
        """Verifies that Mastercard starting with 2333,
        length = 16, invalid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator("2333333333333336"))


if __name__ == '__main__':
    unittest.main()
