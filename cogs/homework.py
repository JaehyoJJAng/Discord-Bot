from discord.ext import commands
from typing import Dict,List
import random
import json
import sys

class HomeWorkLunch:
    @staticmethod
    def validation_check(obj,type):
        if isinstance(obj,type):
            pass
        else:
            print(f"타입 오류! - Object : {obj} | Type : {type}\n")
            sys.exit()

    def __init__(self,menu1:str,menu2:str) -> None:
        # Menu 1
        self.menu1 : str = menu1

        # Menu 2 
        self.menu2 : str = menu2

        # Lunch list in Json File
        self.lunch_list : Dict[str,List[str]] = self.get_json_data()    

    def random_choice(self)-> str:
        """ 메뉴 랜덤 추천 """
        # 카테고리 추출하기
        categories : List[str] = [_ for _ in self.get_categorys() if _ == self.menu1 or _ == self.menu2] 

        category = random.choice(categories)

        # 카테고리의 메뉴 추출
        category_menu_list : List[str] = self.lunch_list[category]

        # 카테고리의 메뉴 랜덤 추출
        lunch : str = random.choice(category_menu_list)
        return f'오늘 점심은 {category}, 그 중에서 {lunch}(은)는 어떠세요?'
        
    def get_categorys(self)-> List[str]:
        """ Category Return (한식 중식 일식 .. ) """
        return list(self.lunch_list.keys())

    def get_json_data(self)-> Dict[str,List[str]]:
        """ Json Data Load """
        file : str = 'cogs/data/lunch.json'
        with open(file,'r',encoding='UTF-8') as fp:
            json_data : Dict[str,List[str]] = json.loads(fp.read())
        return json_data

class CogHomeWork(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("Home Work Together")

    @commands.command(name='이름')
    async def _name(self,ctx)-> None:
        await ctx.send(ctx.author.name)

    @commands.command(name=f'점심')
    async def _name(self,ctx,arg1=None,arg2=None)-> None:
        # Create Lunch Instance 
        lunch = Lunch(menu1=arg1,menu2=arg2)

        # Return Menu Text
        text : str = lunch.random_choice()

        # Send Message To User
        await ctx.send(text)

def setup(client):
    client.add_cog(CogHomeWork(client=client))