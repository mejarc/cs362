import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    """ Test numbers
    """
    # Visa
    valid_visa = "4333333333333339"
    short_valid_visa = "433333333333336"
    valid_visa_9 = "433333333"
    valid_visa_10 = "4333333336"
    valid_visa_17 = "43333333333333337"
    invalid_visa_17 = "43333333333333331"
    valid_visa_19 = "4333333333333333338"
    invalid_visa_19 = "4333333333333333331"
    valid_visa_20 = "43333333333333333331"
    invalid_visa_20 = "43333333333333333336"
    visa_bad_checksum = "4333333333333338"
    visa_all_bad = "433333333333337"

    # Amex
    valid_amex_34 = "343333333333335"
    amex_34_bad_checksum = "343333333333337"
    short_amex_34_valid_checksum = "3433333333334"
    valid_amex_37 = "373333333333338"
    amex_37_bad_checksum = "373333333333332"

    boundary_amex_33 = "333333333333337"
    amex_33_bad_checksum = "333333333333332"
    boundary_amex_35 = "353333333333331"
    amex_35_bad_checksum = "353333333333336"
    boundary_amex_36 = "363333333333330"
    amex_36_bad_checksum = "363333333333336"
    boundary_amex_38 = "383333333333336"
    amex_38_bad_checksum = "383333333333331"
    amex_all_bad = "39333333339"

    # Mastercard
    valid_mc_51 = "5133333333333338"
    short_valid_mc_51 = "513333333333339"
    valid_mc_52 = "5233333333333337"
    short_valid_mc_52 = "523333333333337"
    valid_mc_53 = "5333333333333336"
    valid_mc_54 = "5433333333333335"
    valid_mc_55 = "5533333333333334"
    valid_mc_56 = "5633333333333333"
    valid_mc_2221 = "2221333333333338"
    valid_mc_2222 = "2222333333333337"
    valid_mc_2333 = "2333333333333333"
    mc_2333_bad_checksum = "2333333333333336"
    long_mc_2333 = "23333333333333339"
    valid_mc_2500 = "2500333333333330"
    mc_2500_bad_checksum = "2500333333333335"
    valid_mc_2719 = "2719333333333337"
    valid_mc_2720 = "2720333333333334"
    mc_2720_bad_checksum = "2720333333333339"
    short_invalid_mc_2720 = "272033333333339"
    short_valid_mc_2720 = "272033333333336"
    boundary_mc_50 = "5033333333333339"
    mc_50_bad_checksum = "5033333333333331"
    boundary_mc_56 = "5633333333333333"
    boundary_mc_2220 = "2220333333333339"
    boundary_mc_2721 = "2721333333333333"
    mc_2721_bad_checksum = "2721333333333336"
    mc_all_bad = "50333333333331"

    def test1(self):
        """Verifies that credit card with 0 returns None
        Picked using Error Guessing
        """
        self.assertIsNone(credit_card_validator(""))

    def test2(self):
        """Verifies that credit card with less < 10 numbers returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.valid_visa_9))

    def test3(self):
        """Verifies that credit card with > 19 numbers returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.valid_visa_20))

    def test4(self):
        """Verifies that credit card with first digit 6 returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("6333333333"))

    def test5(self):
        """Verifies that credit card with first digit 7 returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("7333333333"))

    def test6(self):
        """Verifies that Amex starting with 36,
        length = 15, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.boundary_amex_36))

    def test7(self):
        """Verifies that Visa starting with 4,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator(TestCase.valid_visa))

    def test8(self):
        """Verifies that Mastercard starting with 2333,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_2333))

    def test9(self):
        """Verifies that Mastercard starting with 50,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.boundary_mc_50))

    def test10(self):
        """Verifies that Amex starting with 33,
        length = 15, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.boundary_amex_33))

    def test11(self):
        """Verifies that Amex starting with 38,
        length = 15, valid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator(TestCase.boundary_amex_38))

    def test12(self):
        """Verifies that Amex starting with 36,
        length = 15, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.boundary_amex_36))

    def test13(self):
        """Verifies that Mastercard starting with 56,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.boundary_mc_56))

    def test14(self):
        """Verifies that Mastercard starting with 2220,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.boundary_mc_2220))

    def test15(self):
        """Verifies that Mastercard starting with 2721,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.boundary_mc_2721))

    def test16(self):
        """Verifies that Mastercard starting with 2500,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_2500))

    def test17(self):
        """Verifies that Mastercard starting with 52,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_52))

    def test18(self):
        """Verifies that Visa starting with 4,
        length = 15, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.short_valid_visa))

    def test19(self):
        """Verifies that Mastercard starting with 52,
        length = 15, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.short_valid_mc_52))

    def test20(self):
        """Verifies that Mastercard starting with 2720,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_2720))

    def test21(self):
        """Verifies that Amex starting with 35,
        length = 15, invalid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator(TestCase.boundary_amex_35))

    def test22(self):
        """Verifies that Visa starting with 4,
        length = 16, invalid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator(TestCase.visa_bad_checksum))

    def test23(self):
        """Verifies that Mastercard starting with 2333,
        length = 16, invalid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator(TestCase.mc_2333_bad_checksum))

    def test24(self):
        """Verifies that Mastercard starting with 2500,
        length = 16, invalid checksum returns False
        Picked using Category Partitioning
        """
        self.assertFalse(credit_card_validator(TestCase.mc_2500_bad_checksum))

    def test25(self):
        """Verifies that Mastercard starting with 2720,
        length = 16, invalid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator(TestCase.mc_2720_bad_checksum))

    def test26(self):
        """Verifies that Mastercard starting with 2721,
        length = 16, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.mc_2721_bad_checksum))

    def test27(self):
        """Verifies that Mastercard starting with 2720,
        length = 15, invalid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(TestCase.short_invalid_mc_2720))

    def test28(self):
        """Verifies that Mastercard starting with 2720,
        length = 15, valid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(TestCase.short_valid_mc_2720))

    def test29(self):
        """Verifies that Mastercard starting with 2333,
        length = 17, valid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(TestCase.long_mc_2333))

    def test30(self):
        """Verifies that Visa starting with 4,
        length = 19, valid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(TestCase.valid_visa_19))

    def test31(self):
        """Verifies that Amex starting with 35,
        length = 15, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.amex_35_bad_checksum))

    def test32(self):
        """Verifies that Amex starting with 34,
        length = 15, invalid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(TestCase.amex_34_bad_checksum))

    def test33(self):
        """Verifies that Amex starting with 37,
        length = 15, invalid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(TestCase.amex_37_bad_checksum))

    def test34(self):
        """Verifies that Amex starting with 33,
        length = 15, invalid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(TestCase.amex_33_bad_checksum))

    def test35(self):
        """Verifies that Amex starting with 38,
        length = 15, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.amex_38_bad_checksum))

    def test36(self):
        """Verifies that Amex starting with 36,
        length = 15, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.amex_36_bad_checksum))

    def test37(self):
        """Verifies that Amex starting with 39,
        length = 11, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.amex_all_bad))

    def test38(self):
        """Verifies that Mastercard starting with 50,
        length = 15, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.mc_all_bad))

    def test39(self):
        """Verifies that Visa starting with 4,
        length = 15, invalid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator(TestCase.visa_all_bad))

    def test40(self):
        """Verifies that Mastercard starting with 51,
        length = 15, valid checksum returns False
        Picked using Category Partitioning"""
        self.assertFalse(credit_card_validator(TestCase.short_valid_mc_51))

    def test41(self):
        """Verifies that Amex starting with 34,
        length = 14, valid checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(
            TestCase.short_amex_34_valid_checksum))

    def test42(self):
        """Verifies that Mastercard starting with 50,
        length = 16, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.mc_50_bad_checksum))

    def test43(self):
        """Verifies that Mastercard starting with 54,
        length = 16, valid checksum returns True
        Picked using Boundary Value Analysis"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_54))

    def test44(self):
        """Verifies that Mastercard starting with 2221,
        length = 16, valid checksum returns True
        Picked using Boundary Value Analysis"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_2221))

    def test45(self):
        """Verifies that Mastercard starting with 2222,
        length = 16, valid checksum returns True
        Picked using Boundary Value Analysis"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_2222))

    def test46(self):
        """Verifies that Mastercard starting with 2719,
        length = 16, valid checksum returns True
        Picked using Boundary Value Analysis"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_2719))

    def test47(self):
        """Verifies that Mastercard starting with 55,
        length = 16, valid checksum returns True
        Picked using Boundary Value Analysis"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_55))

    def test48(self):
        """Verifies that Mastercard starting with 56,
        length = 16, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.valid_mc_56))

    def test49(self):
        """Verifies that Mastercard starting with 53,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_53))

    def test50(self):
        """Verifies that Mastercard starting with 51,
        length = 16, valid checksum returns True
        Picked using Category Partitioning"""
        self.assertTrue(credit_card_validator(TestCase.valid_mc_51))

    def test51(self):
        """Verifies that Visa starting with 4,
        length = 19, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.valid_visa_19))

    def test52(self):
        """Verifies that Visa starting with 4,
        length = 19, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.invalid_visa_19))

    def test53(self):
        """Verifies that Visa starting with 4,
        length = 20, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.valid_visa_20))

    def test54(self):
        """Verifies that Visa starting with 4,
        length = 20, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.invalid_visa_20))

    def test55(self):
        """Verifies that Visa starting with 4,
        length = 17, valid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.valid_visa_17))

    def test56(self):
        """Verifies that Visa starting with 4,
        length = 17, invalid checksum returns False
        Picked using Boundary Value Analysis"""
        self.assertFalse(credit_card_validator(TestCase.invalid_visa_17))


if __name__ == '__main__':
    unittest.main()
