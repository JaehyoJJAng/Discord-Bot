from __init__ import HomeWorkLunch,HomeWorkCSV
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

class HomeWorkCSVTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls)-> None:
        cls.csv = HomeWorkCSV()

        cls.file_path : str = r'C:\github\Discord-Bot\cogs\data'
    
    def test_get_csv_data(self)-> None:
        data : Dict[str,str] = self.csv.get_csv_data(file=os.path.join(self.file_path,'quiz.csv'))
        self.assertEqual(len(data),30)

    def test_get_answer(self)-> None:
        data : Dict[str,str] = self.csv.get_csv_data(file=os.path.join(self.file_path,'quiz.csv'))
        
        problem_info : Dict[str,str] = self.csv.get_answer(quiz_dict=data)

        self.assertIn('problem',list(problem_info.keys()))
        self.assertIn('answer',list(problem_info.keys()))

    def test_json_to_dict(self)-> None:
        dic : dict = self.csv.json_to_dict(file=os.path.join(self.file_path,'score.json'))
        self.assertDictEqual(dic,{'착짱죽짱멸공하자':2})

if __name__ == '__main__':
    unittest.main()