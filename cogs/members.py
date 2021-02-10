from discord.ext  import commands
from discord import Embed
from discord import Colour

from utils.database import insert
from utils.database import delete

#constants; maybe we need to move it to some config file?
CONNECT_LEAVE_CHAN_ID = 694229192551956491
AMOUNT_MEMBERS_CHAN_ID = 702501822278926348
ROLE_DEFAULT = 643902599661223951
ROLE_PROGRAMMER = 554918572783304714
RULES_CHAN_ID = 643947517473587200
ROLES_CHAN_ID = 643949209510215680

msg_greetings = """\
{name}! Добро пожаловать на сервер {this_guild}.\
Здесь ты найдешь себе друзей, помошь в коде, или просто хорошее общение.\n\
Так-же не забудь почитать правила({rules_chan}),\
а так же посмотреть роли этого сервера({roles_chan})\
"""
msg_leaved_server = "@everyone\n**{member}** увы... Ушел из сервера" 
msg_joined_server = "@everyone\n**{member}** зашел на сервер"

USER_LEAVED_COLOR = Colour.from_rgb(232,0,0)
USER_JOINED_COLOR = Colour.from_rgb(0,242,0)

#finally, some code:

mention = lambda id = f'<#{id}>'

class Members(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        connect_leave_channel = member.guild.get_channel(CONNECT_LEAVE_CHAN_ID)
        amount_members = member.guild.get_channel(AMOUNT_MEMBERS_CHAN_ID)
        role = member.guild.get_role(ROLE_DEFAULT)
        role_proggramer = member.guild.get_role(ROLE_PROGRAMMER)
        
        if member.bot == True:
            insert("Members",["id_bot"],[member.id])
        else:
            insert("Members",["id","xp","lvl","money"],[f"{member.id}","0","1","0"])
            
        await member.send(msg_greetings.format(
            name=member.name, 
            this_guild=member.guild, 
            rules_chan=mention(RULES_CHAN_ID),
            roles_chan=mention(ROLES_CHAN_ID),))
        
        await connect_leave_channel.send(embed = Embed(
            description = msg_joned_server.format(member=member), 
            colour = USER_JOINED_COLOR))
        await amount_members.edit(name=f'Людей на сервере: {len(member.guild.members)}')
        
        await member.add_roles(role)
        await member.add_roles(role_proggramer)
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        connect_leave_channel = member.guild.get_channel(CONNECT_LEAVE_CHAN_ID)
        amount_members = member.guild.get_channel(AMOUNT_MEMBERS_CHAN_ID)
        current_online = len(member.guild.members)
        await amount_members.edit(name=f'Людей на сервере: {current_online}')
        await connect_leave_channel.send(embed = Embed(
            description = msg_leaved_server.format(member=member), 
            colour = USER_LEAVED_COLOR))
        delete("Members",f"id = '{member.id}'")
    
def setup(client):
    client.add_cog(Members(client))
