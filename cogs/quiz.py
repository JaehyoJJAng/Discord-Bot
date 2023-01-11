from discord.ext import commands
from typing import Union,Dict,List
import discord 
import csv
import random 
import re
import asyncio

class CSV:
    def get_csv_data(self,file:str)-> Dict[str,str]:
        with open(file,'r',encoding='UTF-8') as fp:
            reader = csv.reader(fp)
            data : Dict[str,str] = {re.sub('[^ㄱ-ㅎ가-힣 ?]','',d[0]).strip():d[1] for d in reader}
        return data

class Quiz(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
        self.quiz_dict : Dict[str,str] = CSV().get_csv_data(file='cogs/data/quiz.csv')
    
    def get_answer(self)-> Dict[str,str]:
        problem_info : Dict[str,str] = dict()

        # 문제 리스트
        problem_list : List[str] = list(self.quiz_dict.keys())

        # 랜덤으로 문제 하나 뽑기
        problem : str = random.choice(problem_list)

        # 해당 문제에 대한 답 뽑기
        answer : str = self.quiz_dict[problem]

        problem_info['problem'] = problem
        problem_info['answer']  = answer
        
        return problem_info

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("Quiz !")
    
    @commands.command(name='퀴즈')
    async def _quiz(self,ctx)-> None:
        # answer 추출
        problem_info : Dict[str,str] = self.get_answer()
        answer : str   = problem_info['answer']
        problem : str  = problem_info['problem']

        # 퀴즈 문제 전송
        embed = discord.Embed(title='퀴즈',description=problem,color = discord.Color.blue())
        await ctx.send(embed=embed)

        # answer 유효성 체크
        def checkAnswer(message):
            if message.channel == ctx.channel and answer in message.content:
                return True
            else:
                return False

        try :
            # wat_for 함수의 리턴값 받기
            message = await self.client.wait_for('message',timeout=10.0,check=checkAnswer)

            # 메시지의 작성자(author)의 이름(name) 속성 사용
            name = message.author.name
            
            embed = discord.Embed(title = '정답', description = f'{name} 님, 정답이에요 !', color = discord.Color.blue())
            
            await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            embed = discord.Embed(title = '땡', description = f'땡! 시간초과에요\n\n정답은! \'{answer}\' 이었습니다 !~', color = discord.Color.blue())

            await ctx.send(embed=embed)

def setup(client)-> None:
    client.add_cog(Quiz(client=client))

