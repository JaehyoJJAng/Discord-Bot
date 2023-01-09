from bs4 import BeautifulSoup as bs
from typing import Dict
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from discord.ext import commands
import discord
import requests as rq
import os

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

class GetPageViews:
    def __init__(self) -> None:
        self.base_url : str = 'http://www.histats.com/viewstats/?sid=4661640&ccid=306'
        self.headers : Dict[str,str] = {'user-agent':'Mozilla/5.0'}

    @staticmethod
    def get_soup_obj(page_source):
        return bs(page_source,'html.parser')

    def parsing(self)-> int:
        browser = ChromeDriver().return_driver()        
        browser.get(url=self.base_url)
        browser.implicitly_wait(time_to_wait=15)

        soup = self.get_soup_obj(page_source=browser.page_source)
        
        views : int = int(soup.select_one('font#UPD_tod_v').text.strip())
        return views

class SendMessage(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
        self.get_page_views = GetPageViews()

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("Get Home Page View (WTT)")

    @commands.command(name='조회수')
    async def _views(self,ctx)-> None:
        embed = discord.Embed(title='WTT 조회수',description='조회수 측정 중 ..',color = discord.Color.blue())
        await ctx.send(embed=embed)

        views : int = self.get_page_views.parsing()

        embed = discord.Embed(title='WTT 조회수',description=f'Today\'s Views : {views}',color = discord.Color.blue())
        await ctx.send(embed=embed)

def setup(client)-> None:
    client.add_cog(SendMessage(client=client))