import discord
from discord.ext import commands
from config.config import get_token
import os
import sys

class Hello:
    def say_hello(self,user:str)-> None:
        return "Hello"

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

    def execute_bot(self,client:commands.Bot)-> None:
        """ 봇 실행하는 메소드 """
        client.run(self._token)
    
    def say_hello(self,client:commands.Bot):
        @client.command(name='Hello')
        async def _Hello(ctx):
            try :
                await ctx.send(Hello().say_hello(user='JaehyoJJAng'))
            except:
                sys.exit()


def main():
    # Create Discord Instance
    dico : Discord() = Discord()

    # Return Discord Bot Instance
    client : commands.Bot = dico.return_bot()

    dico.say_hello(client=client)

    # Execute Discord Bot
    dico.execute_bot(client=client)

if __name__ == '__main__':
    main()