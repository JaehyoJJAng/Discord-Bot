from __init__ import GetImage
from typing import List,Dict
import requests as rq
import unittest


class GetImageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_image = GetImage()
    
    def test_main(self)-> None:
        """ Execute Test"""
        image_links: List[str] = self.get_image.main(query='제니')
        self.assertEqual(len(image_links),5)

    def test_fetch(self):
        url : str = 'https://openapi.naver.com/v1/search/image?query=제니&display=5'
        
        with rq.Session() as session:
            image_links: List[str] = self.get_image.fetch(url=url,session=session)
        self.assertEqual(len(image_links),5)

    
if __name__ == '__main__':
    unittest.main()