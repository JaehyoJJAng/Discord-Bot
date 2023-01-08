from __init__ import RealTimeSearchWord
from typing import Dict,List
import requests as rq
import unittest

class RealTimeSearchWordTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls)-> None:
        cls.real_time_search_word  = RealTimeSearchWord()

    def test_chrome_driver(self)-> None:
        """ Web Driver Test """
        self.assertNotEqual(self.real_time_search_word.browser,None)
    
    def test_get_soup_obj(self)-> None:
        """ Testing Static Method : get_soup_obj """
        with rq.Session() as session:
            with session.get(self.real_time_search_word.url) as response:
                if response.ok:
                    soup = self.real_time_search_word.get_soup_obj(page_source=response.text)
                    text : str = soup.select_one('strong').text
                    self.assertNotEqual(text,None)
    
    def test_get_items(self)-> None:
        items: List[Dict[str,str]] = self.real_time_search_word.get_items()
        item_count : int = len(items)
        self.assertEqual(item_count,3)
if __name__ == '__main__':
    unittest.main()