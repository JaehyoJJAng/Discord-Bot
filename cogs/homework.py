from discord.ext import commands
from typing import Dict,List
import random
import json
import sys
import csv
import re
import asyncio
import os

class HomeWorkLunch:
    @staticmethod
    def validation_check(obj,type)-> None:
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

class HomeWorkCSV:
    def get_csv_data(self,file:str)-> Dict[str,str]:
        """ Csv data 가져오기 """
        with open(file,'r',encoding='UTF-8') as fp:
            reader = csv.reader(fp)
            data : Dict[str,str] = {re.sub('[^ㄱ-ㅎ가-힣 ?]','',d[0]).strip():d[1] for d in reader}
        return data

    def get_answer(self,quiz_dict:Dict[str,str])-> Dict[str,str]:
        """ 랜덤으로 문제 뽑은 후 answer 값 추출하기 """
        problem_info : Dict[str,str] = dict()

        # 문제 리스트
        problem_list : List[str] = list(quiz_dict.keys())

        # 랜덤으로 문제 하나 뽑기
        problem : str = random.choice(problem_list)

        # 해당 문제에 대한 답 뽑기
        answer : str = quiz_dict[problem]

        problem_info['problem'] = problem
        problem_info['answer']  = answer
        return problem_info

    def json_to_dict(self,file:str)-> dict:
        """ Json => Dict """
        with open(file,'r',encoding='UTF-8') as fp:
            dic : dict = json.load(fp)
        return dic

    def dict_to_json(self,file:str,data:Dict[str,int])-> None:
        """ Dict => Json """
        with open(file,'w',encoding='UTF-8') as fp:
            json.dump(data,fp,ensure_ascii=False)

class CogHomeWork(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
        self.csv = HomeWorkCSV()
        self.file_path : str = r'C:\github\Discord-Bot\cogs\data'

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("Today's Home Work!")

    @commands.command(name='이름')
    async def _name(self,ctx)-> None:
        await ctx.send(ctx.author.name)

    @commands.command(name=f'숙제점심')
    async def _homeworkLunch(self,ctx,arg1=None,arg2=None)-> None:
        # Create Lunch Instance 
        lunch = HomeWorkLunch(menu1=arg1,menu2=arg2)

        # Return Menu Text
        text : str = lunch.random_choice()

        # Send Message To User
        await ctx.send(text)
    
    @commands.command(name='숙제퀴즈')
    async def _homeworkQuiz(self,ctx)-> None:
        # Score Dict 가져오기
        data : Dict[str,int] = self.csv.json_to_dict(file=self.file_path + '\score.json')

        # Score Dict 초기값 분기
        if ctx.author.name not in list(data.keys()):
            data[ctx.author.name] = 0


        # csv data 가져오기
        quiz_dict : Dict[str,str] = self.csv.get_csv_data(file=self.file_path + '\quiz.csv')

        # answer 값 추출
        problem_info : Dict[str,str] = self.csv.get_answer(quiz_dict=quiz_dict)

        # 퀴즈 문제 전송
        await ctx.send(problem_info['problem'])
        
        # answer 유효성 체크
        def checkAnswer(message):
            if message.channel == ctx.channel and problem_info['answer'] in message.content:
                return True
            else:
                return False

        try :
            await self.client.wait_for('message',timeout=10.0,check=checkAnswer)

            # 메시지 전송하기
            await ctx.send(f'{ctx.author.name} 님 정답이에요!')

            # 점수 올리기
            data[ctx.author.name] += 1

        except asyncio.TimeoutError:
            await ctx.send('땡! 시간초과에요!')
        
        # Dict To Json
        self.csv.dict_to_json(file=self.file_path + '\score.json',data=data)

def setup(client):
    client.add_cog(CogHomeWork(client=client))