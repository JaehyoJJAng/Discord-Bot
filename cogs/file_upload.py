from discord.ext import commands
from typing import List,Dict,Union
import discord
import os
import random

class FileUpload(commands.Cog):
    def __init__(self,client) -> None:
        # Client
        self.client = client
        
        # Upload Path
        self.upload_path : str = r'cogs\images'
    
    def get_file_list(self,keyword:str)-> List[str]:
        """ 파일 목록 출력 """
        for path,dir,file_name in os.walk(os.path.join(self.upload_path,keyword)):
            return [os.path.join(path,file) for file in file_name]

    def random_choice_any_pic(self,file_list:List[str])-> str:
        """ 파일 랜덤 초이스 """
        return random.choice(file_list)

    def random_choice_any_text(self,text_list:list[str])-> str:
        return random.choice(text_list)

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("File Upload !")

    @commands.command(name='사진')
    async def _picture_upload(self,ctx,arg1=None)-> None:
        if not os.path.isdir(os.path.join(self.upload_path,arg1)):
            # 경로 미 존재시 아래 메시지 전송
            embed = discord.Embed(title=f'{arg1} : Error',description='죄송합니다. 해당 인물에 대한 사진 기록이 서버에 존재하지 않습니다.',color = discord.Color.red())
            await ctx.send(embed=embed)
            return 0 # 함수 종료
        
        if arg1 == '고윤정':
            # 파일 리스트 목록
            file_list : List[str] = self.get_file_list(keyword=arg1)

            # 파일 랜덤 추출 (우선 1개만)
            file : str = self.random_choice_any_pic(file_list=file_list)

            # 디스코드에 올릴 파일 지정
            image = discord.File(file,filename='image.png')

            # 랜덤 텍스트 메시지 작성
            text_list : List[str] = [
                '모가지가 떨어져 내린다하여 낙수',
                '멋지지 않느냐?',
                '장욱 !',
                '나는 절세미인이다.'
            ]
            
            # 텍스트 메시지 랜덤 추출 (1개)
            text : str = self.random_choice_any_text(text_list=text_list)

            # Embed 메시지 구성
            embed = discord.Embed(title=arg1,description=f"{text[0:3]} ..",color=0x00ff56)

            # 아까 지정한 파일이름으로 파일 지정
            embed.set_thumbnail(url='attachment://image.png')
            embed.add_field(name='', value=text, inline=True)

            # 메시지 보내기
            await ctx.send(embed=embed,file=image)

        else:
            pass


def setup(client)-> None:
    client.add_cog(FileUpload(client=client))