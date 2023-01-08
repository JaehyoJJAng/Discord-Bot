from __init__ import HomeWork
import unittest

class HomeWorkTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.home_work = HomeWork()

    def test_author(self):
        author : str = self.home_work.author(name='이재효')
        self.assertEqual(author,'이재효')

if __name__ == '__main__':
    unittest.main()