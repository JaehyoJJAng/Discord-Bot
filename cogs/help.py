from discord.ext import commands
class Help(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Cog is ready")

def setup(client):
    client.add_cog(Help(client=client))