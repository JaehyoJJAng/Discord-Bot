from discord.ext import commands
from config.config import get_token
from typing import List,Dict 
import discord
import os
import sys
import requests as rq
import asyncio

class Discord:
    def __init__(self)-> None:
        self._token : str = get_token(key='token')

    def return_bot(self):
        """ 봇 객체 리턴 메소드 """
        prefix = '!'

        # intents : 봇이 서버 멤버의 정보나 , 서버 멤버 리스트를 불러올 수 있도록 허용하는 설정이었음
        intents = discord.Intents.all()

        # Bot 객체 생성
        client = commands.Bot(command_prefix=prefix,intents=intents)
        return client

    def load_extensions(self,client):        
        for filename in os.listdir('cogs/'):
            if '.py' in filename:
                filename = filename.replace('.py','')
                client.load_extension(f"cogs.{filename}")

    def execute_bot(self,client:commands.Bot)-> None:
        """ 봇 실행하는 메소드 """
        client.run(self._token)

    def say_realtime_search_keyword(self,client:commands.Bot)-> None:
        """ 실시간 검색어 명령 """            
        @client.command(name='실시간검색어')
        async def _live(ctx):
            try :
                realtime = RealTimeSearchWord()
                item_list : list = realtime.get_items()
                for idx,item in enumerate(item_list,1):
                    title = item['title']
                    link  = item['link']

                    await ctx.send(f'순위 : {idx}\t검색명 : {title}\t링크 : {link}\n')
            except:
                sys.exit()

def main()-> None:
    # Create Discord Instance
    dico = Discord()

    # Return Discord Bot Instance
    client : commands.Bot = dico.return_bot()
    
    # Load Extensions
    dico.load_extensions(client=client)

    # 디스코드 봇 실행하기
    dico.execute_bot(client=client)
    
if __name__ == '__main__':
    main()