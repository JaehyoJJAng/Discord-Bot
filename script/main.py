from config import get_token
import discord
from discord.ext import commands

class Discord:
    def __init__(self):
        self._token : str = get_token(key='token')

    def return_bot(self)-> any:
        """ 봇 객체 리턴 메소드 """
        prefix = '!'

        # intents : 봇이 서버 멤버의 정보나 , 서버 멤버 리스트를 불러올 수 있도록 허용하는 설정이었음
        intents = discord.Intents.all()

        # Bot 객체 생성
        client = commands.Bot(command_prefix=prefix,intents=intents)
        return client

    def execute_bot(self,client):
        client.run(self._token)

def main():
    # Create Discord Instance
    dico = Discord()

    # Return Discord Bot Instance
    client : any = dico.return_bot()

    # Execute Discord Bot
    dico.execute_bot(client=client)

if __name__ == '__main__':
    main()