from discord.ext import commands
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from typing import Dict,List
import discord
import urllib.parse as rep

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

    def get_items(self)-> List[Dict[str,str]]:
        # URL 접속
        self.browser.get(url=self.url)

        # soup return
        soup = self.get_soup_obj(page_source=self.browser.page_source)

        # 아이템 길이
        item_length : int = len(soup.select('a.rank-layer',limit=10))
        
        item_list : List[Dict[str,str]] = []
        for idx in range(item_length):
            item_dic : Dict[str,str] = {}

            items : list =  soup.select('a.rank-layer',limit=10)

            title : str = items[idx].select_one('.rank-text').text.strip()
            link  : str = items[idx].attrs['href']

            item_dic['title'] = title
            item_dic['link']  = link
            item_list.append(item_dic)
        return item_list

class CogRealTimeSearchWord(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
        self.real_time_search_word : RealTimeSearchWord = RealTimeSearchWord()

    def query_to_quote(self,url:str):
        query : str = rep.quote_plus(url.split('query=')[-1])
        return query

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("Real Time Search Word")
    
    @commands.command(name='실시간검색어')
    async def _realtime_word(self,ctx)-> None:
        embed = discord.Embed(title='알림',description='실시간 검색어 수집을 시작합니다!',color = discord.Color.blue())
        await ctx.send(embed=embed)
        
        get_items : List[Dict[str,str]] = self.real_time_search_word.get_items()
        for item in get_items:
            # URL
            url : str = item['link']

            # Title
            title : str = item['title']

            # 쿼리 유니코드화
            query : str = self.query_to_quote(url=item['link'])
            
            # URL 재지정
            url : str = url.split('query=')[0] + f'query={query}'
            
            embed = discord.Embed(description=f"[{title}]({url})",color = discord.Color.blue())
            await ctx.send(embed=embed)

        embed = discord.Embed(title='알림',description='실시간 검색어 수집이 완료되었습니다',color = discord.Color.blue())
        await ctx.send(embed=embed)

def setup(client)-> None:
    client.add_cog(CogRealTimeSearchWord(client=client))