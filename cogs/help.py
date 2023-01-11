from discord.ext import commands
import discord
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Cog is Ready")
        
    @commands.command(name="도움말",description = "명령어 목록을 보여줍니다.")
    async def _help(self, ctx):
        embed = discord.Embed(title = '명령어 도움말', color = discord.Color.blue())
        cogs = self.client.cogs
        for name, cog in cogs.items():
            commandList = ""
            for command in cog.walk_commands():
                commandList += f"```!{command.name} {command.signature}```{command.description}\n"
            embed.add_field(name = name, value = commandList, inline=False)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Help(client))