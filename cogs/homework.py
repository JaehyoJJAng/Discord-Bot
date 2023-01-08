from discord.ext import commands

class HomeWork:
    def author(self,name:str='이두식'):
        return name

class CogHomeWork(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self)-> None:
        print("Home Work Together")

    @commands.command(name='이름')
    async def _name(self,ctx)-> None:
        await ctx.send(HomeWork().author(name='이재효'))
    
def setup(client):
    client.add_cog(CogHomeWork(client=client))