from discord.ext import commands
from discord import Member

class Jokes(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def кол(self,ctx,arg : Member = None):
        author = ctx.message.author
        if arg == None:
            await ctx.send(f'\*<@!{arg}> был проткнут <@!{author.id}> с помощью кол*')
        else:
            await ctx.send(f'\*<@!{arg.id}> был проткнут <@!{author.id}> с помощью кол*')
    @commands.command()
    @commands.has_permissions(administrator= True)
    async def pizdec(self,ctx,jec_id : int,kol_ras : int):
        for i in range(kol_ras):
            mem_jec = ctx.guild.get_member(jec_id)
            voice1 = ctx.guild.get_channel(644234744879644682)
            voice2 = ctx.guild.get_channel(644234808029085729)
            await mem_jec.move_to(voice1)
            await mem_jec.move_to(voice2)
            i += 1
            
def setup(client):
    client.add_cog(Jokes(client))
