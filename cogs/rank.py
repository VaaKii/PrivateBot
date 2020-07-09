from discord.ext import commands
from discord import Member
from discord import Embed
from discord import Colour

from utils.database import select

class Rank_system(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def rank(self,ctx,member : Member = None):
        if member != None:
            what = ["xp","lvl","repo"]
            result = select("Members",what,f"id = '{member.id}'")
            for row in result:
                xp = int(row[0])
                lvl = int(row[1])
                repo = int(row[2])
            em = Embed(
                colour = Colour.purple()
            )
            em.set_author(name = member.name,icon_url = member.avatar_url)
            em.add_field(name='Уровень:',value=lvl)
            em.add_field(name='Xp:',value=xp)
            em.add_field(name="Осталось до следушего уровня:",value=str(lvl*(lvl * 50)- xp)+ ' xp')
            em.add_field(name='Количество "Спасибо":',value=repo)
            await ctx.send(embed = em)
        else:
            what = ["xp","lvl","repo"]
            result = select("Members",what,f"id = '{ctx.message.author.id}'")
            for row in result:
                xp = int(row[0])
                lvl = int(row[1])
                repo = int(row[2])
            em = Embed(
                colour = Colour.purple()
            )
            em.set_author(name = ctx.message.author.name,icon_url = ctx.message.author.avatar_url)
            em.add_field(name='Ваш уровень:',value=lvl)
            em.add_field(name='Ваш Xp:',value=xp)
            em.add_field(name="Вам осталось до следушего уровня:",value=str(lvl*(lvl * 50)- xp)+ ' xp')
            em.add_field(name='Ваше количество "Спасибо":',value=repo)
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Rank_system(client))