import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    def test1(self):
        contrived_func(2)

    def test2(self):
        contrived_func(-1)

    def test3(self):
        contrived_func(14)

    def test4(self):
        contrived_func(15)

    def test5(self):
        contrived_func(-18)

    def test6(self):
        contrived_func(26)

    def test7(self):
        contrived_func(3)

    def test8(self):
        contrived_func(35)


if __name__ == '__main__':
    unittest.main()
