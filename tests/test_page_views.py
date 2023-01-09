from __init__ import GetPageViews
import unittest

class GetPageViewsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_page_views = GetPageViews()
    
    @staticmethod
    def value_check(value,type):
        if isinstance(value,type):
            return True
        else:
            return False

    def test_parsing(self):
        views: int = self.get_page_views.parsing()

        status : bool = self.value_check(value=views,type=int)
        self.assertTrue(status)

if __name__ == '__main__':
    unittest.main()