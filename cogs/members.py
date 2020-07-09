from discord.ext  import commands
from discord import Embed
from discord import Colour

from utils.database import insert
from utils.database import delete

class Members(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        connect_leave_channel = member.guild.get_channel(694229192551956491)
        amount_members = member.guild.get_channel(702501822278926348)
        role = member.guild.get_role(643902599661223951)
        role_proggramer = member.guild.get_role(554918572783304714)
        if member.bot == True:
            insert("Members",["id_bot"],[member.id])
        else:
            insert("Members",["id","xp","lvl","money"],[f"{member.id}","0","1","0"])
        await member.send(f"Привет {member.name}! Добро пожаловать на сервер {member.guild}. Здесь ты найдешь себе друзей, помошь в коде, или просто хорошее общение.\nТак-же не забудь почитать правила(<#643947517473587200>), а так же посмотреть роли этого сервера(<#643949209510215680>)")
        await connect_leave_channel.send(embed = Embed(description = f"@everyone\n**{member}** зашел на сервер", colour = Colour.from_rgb(0,242,0)))
        await amount_members.edit(name=f'Людей на сервере: {len(member.guild.members)}')
        await member.add_roles(role)
        await member.add_roles(role_proggramer)
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        connect_leave_channel = member.guild.get_channel(694229192551956491)
        amount_members = member.guild.get_channel(702501822278926348)
        await amount_members.edit(name=f'Людей на сервере: {len(member.guild.members)}')
        await connect_leave_channel.send(embed = Embed(description = f"@everyone\n**{member}** увы... Ушел из сервера", colour = Colour.from_rgb(232,0,0)))
        delete("Members",f"id = '{member.id}'")
    
def setup(client):
    client.add_cog(Members(client))