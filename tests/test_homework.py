from __init__ import HomeWorkLunch
from typing import List,Dict
import os
import unittest

class LunchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls)-> None:
        cls.lunch = HomeWorkLunch(menu1='한식',menu2='중식')
    
    def test_file_exists(self):
        """ File Exists """
        file : str = 'cogs/data/lunch.json'
        file_check : bool = os.path.isfile(file)
        self.assertEqual(file_check,True)

    def test_get_categorys(self)-> None:
        categories : List[str] = self.lunch.get_categorys()
        cate_count : int = len(categories)
        self.assertEqual(cate_count,4)
        
    def test_get_json_data(self)-> None:
        json_data : Dict[str,List[str]] = self.lunch.get_json_data()
        self.assertEqual(len(list(json_data.keys())),4)

    def test_random_choice(self)-> None:
        text : str = self.lunch.random_choice()
        self.assertIn('오늘 점심은',text)

if __name__ == '__main__':
    unittest.main()