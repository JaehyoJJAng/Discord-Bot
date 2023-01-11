from discord.ext import commands
from typing import Dict,List
import requests as rq
import discord
import json
import asyncio
import time

def get_secrets(key:str):
    file : str = r'C:\github\Discord-Bot\cogs\data\.secrets.json'
    with open(file,'r',encoding='UTF-8') as fp:
        secrets : Dict[str,Dict[str,str]] = json.loads(fp.read())    
    try:
        return secrets[key]
    except:
        raise EnvironmentError(f'Set the {key}')

class GetImage:
    def __init__(self) -> List[str]:
        self._headers : Dict[str,str] = get_secrets(key='headers')        

    def main(self,query:str)-> None:
        # API URL
        api_urls : str = f'https://openapi.naver.com/v1/search/image?query={query}&display=5'

        with rq.Session() as session:
            return self.fetch(url=api_urls,session=session)

    def fetch(self,url:str,session)-> List[str]:
        with session.get(url=url,headers=self._headers) as response:
            if response.ok:
                items : List[Dict[str,str]] = response.json()['items']                
                img_links : List[str] = [item['link'] for item in items]            
                return img_links

class SendImage(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

        self.get_image = GetImage()

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("Naver Image Crawling !")
    
    @commands.command(name='이미지')
    async def _image_crawling(self,ctx,arg1=None)-> None:
        # 봇 메시지 전송하기
        embed = discord.Embed(title='이미지 크롤링',description='이미지 크롤링을 시작 합니다!',color = discord.Color.green())
        await ctx.send(embed=embed)
                
        time.sleep(1.0)
                
        # 이미지 링크 가져오기
        img_links : List[str] = self.get_image.main(query=arg1)
        
        # embed 커스텀
        for img_link in img_links:
            embed = discord.Embed(title=arg1,description='',color = discord.Color.blue())
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)        

def setup(client)-> None:
    client.add_cog(SendImage(client=client))