from __init__ import CSV,Quiz
from typing import Dict
import os 
import unittest

class CSVTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls)-> None:
        cls.csv = CSV()
        cls.file : str = r'C:\github\Discord-Bot\cogs\data\quiz.csv'
        
    def test_is_file(self)-> None:
        """ File Exists Test"""
        file_check : bool = os.path.isfile(self.file)
        self.assertTrue(file_check)

    def test_get_csv_data(self)-> None:
        data : Dict[str,str] = self.csv.get_csv_data(file=self.file)
        self.assertEqual(len(data),30)

class QuizTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls)-> None:
        cls.quiz = Quiz(client=None)
    
    def test_get_answer(self)-> None :
        problem_info : Dict[str,str] = self.quiz.get_answer()

        self.assertIn('problem',list(problem_info.keys()))
        self.assertIn('answer' ,list(problem_info.keys()))

if __name__ == '__main__':
    unittest.main()