from __init__ import Discord
from typing import Union
import unittest

class DiscordTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dico = Discord()
        cls.client = cls.dico.return_bot()
    
    def test_return_bot(self):
        status = self.dico.return_bot()
        self.assertNotEqual(status,False)

    def test_load_extensions(self):
        status : Union[None,bool] = self.dico.load_extensions(client=self.client)
        self.assertEqual(status,None)

if __name__ == '__main__':
    unittest.main()