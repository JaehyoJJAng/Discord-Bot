from __init__ import FileUpload
from typing import List
import unittest

class FileUploadTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls)-> None:
        cls.file_upload = FileUpload(client='')
    
    def test_get_file_list(self)-> None:
        file_list : List[str] = self.file_upload.get_file_list(keyword='고윤정')
        self.assertEqual(len(file_list),16)

    def test_random_choice_any_pic(self)-> None:
        random_pic : List[str] = ['img.png']
        pic : str = self.file_upload.random_choice_any_pic(file_list=random_pic)
        self.assertEqual(random_pic[0],pic)
        
    def test_random_choice_any_test(self)-> None:
        text_list : List[str] = ['안녕하세요']
        text : str = self.file_upload.random_choice_any_text(text_list=text_list)
        self.assertEqual(text_list[0],text)

if __name__ == '__main__':
    unittest.main()