import discord
from discord.ext import commands
from config.config import get_token
import os
import sys
import requests as rq
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class ChromeDriver:
    @staticmethod
    def return_driver():
        # options 객체
        chrome_options = Options()

        # headless Chrome 선언
        chrome_options.add_argument('--headless')

        # 브라우저 꺼짐 방지
        chrome_options.add_experimental_option('detach', True)

        # 불필요한 에러메시지 없애기
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
        return browser

class RealTimeSearchWord:
    """ 실시간 검색어 크롤링 Class """
    def __init__(self) -> None:
        self.url : str = 'https://www.signal.bz/news'

        self.browser = ChromeDriver().return_driver()

    @staticmethod
    def get_soup_obj(page_source):
        return bs(page_source,'html.parser')

    def get_items(self)-> list:
        # URL 접속
        self.browser.get(url=self.url)

        # soup return
        soup = self.get_soup_obj(page_source=self.browser.page_source)

        # 아이템 길이
        item_length : int = len(soup.select('a.rank-layer'))
        
        item_list : list = []
        for idx in range(item_length):
            item_dic : dict = {}

            items : list =  soup.select('a.rank-layer')

            title : str = items[idx].select_one('.rank-text').text.strip()
            link  : str = items[idx].attrs['href']

            item_dic['title'] = title
            item_dic['link']  = link
            item_list.append(item_dic)
        return item_list

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
    
    def say_realtime_search_keyword(self,client:commands.Bot):
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


def main():
    # Create Discord Instance
    dico : Discord() = Discord()

    # Return Discord Bot Instance
    client : commands.Bot = dico.return_bot()

    dico.say_realtime_search_keyword(client=client)

    # Execute Discord Bot
    dico.execute_bot(client=client)

if __name__ == '__main__':
    main()