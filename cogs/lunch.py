from typing import Dict,List
from discord.ext import commands
import random
import json
import discord

class Lunch:
    def __init__(self) -> None:
        self.lunch_list : Dict[str,List[str]] = self.get_json_data()

    def random_choice(self)-> str:
        """ 메뉴 랜덤 추천 """
        # 카테고리 추출하기
        categories : List[str] = self.get_categorys()
            
        # 카테고리 랜덤 추출
        category : str = random.choice(categories)
        
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

class CogLunchRecommend(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
        self.lunch = Lunch()

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("Lunch Cog is staring !") 
    
    @commands.command(name='점심추천')
    async def _lunch_rec(self,ctx)-> None:
        embed = discord.Embed(title='점심 추천서',description=self.lunch.random_choice(),color = discord.Color.blue())
        await ctx.send(embed=embed)

def setup(client)-> None:
    client.add_cog(CogLunchRecommend(client=client))