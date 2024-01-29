import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    ''''
    Combo: F/T/T/F'''
    def test1(self):
        contrived_func(2)

    ''''
    Combo: F/F/T/T'''

    def test2(self):
        contrived_func(-1)

    ''''
    Combo: T/T/T/F'''
    def test3(self):
        contrived_func(14)

    ''''
    Combo: T/F/T/F'''
    def test4(self):
        contrived_func(15)

    ''''
    Combo: F/T/T/T'''
    def test5(self):
        contrived_func(-18)

    ''''
    Inputs: T/T/F/F'''
    def test6(self):
        contrived_func(26)

    ''''
    Inputs: F/F/T/F'''
    def test7(self):
        contrived_func(3)

    ''''
    Combo: T/F/F/F'''
    def test8(self):
        contrived_func(35)


if __name__ == '__main__':
    unittest.main()
