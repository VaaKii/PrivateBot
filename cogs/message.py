from random import randint

from discord.ext import commands
from discord import Embed
from discord import Colour
from discord import Status

from utils.database import select
from utils.database import update

class Messages(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        if not message.author.bot:
            is_help = False
            ID_bot_mention = '<@!613269904963141643>'
            ID_bot_mention_without_exclamation_mark = '<@613269904963141643>'
            role_bot = '<@&698575036310618222>'
            was_already = False

            if ID_bot_mention or ID_bot_mention_without_exclamation_mark or role_bot in message.content:
                I = message.guild.get_member(506438836943978496) 
                if ID_bot_mention in message.content:
                    result =  select("Question",["question","answer"],f"question = '{message.content.replace(ID_bot_mention,'')}'")
                elif ID_bot_mention_without_exclamation_mark in  message.content:
                    result = select("Question",["question","answer"],f"question = '{message.content.replace(ID_bot_mention_without_exclamation_mark,'')}'")
                else:
                    result = select("Question",["question","answer"],f"question = '{message.content.replace(role_bot,'')}'")
            
                for row in result:
                    if row[0] == message.content.replace(ID_bot_mention,'') or message.content.replace(ID_bot_mention_without_exclamation_mark,'') or message.content.replace(role_bot,''):
                        was_already = True

                


            if message.content == ".rank" or message.content == ".card":
                is_help = True
            print(f"{message.author} : {message.content} channel {message.channel}")

            channel_logs = message.guild.get_channel(688373372945694725)
            em = Embed(description = f"{message.author} : `{message.content}` channel {message.channel}", colour = Colour.from_rgb(0, 0, 201))
            await channel_logs.send(embed = em)
            plus_lvl = 0
            if len(message.content) >= 5 and not is_help:
                result = select("Members",["xp","lvl"],f"id = {message.author.id}")

                for row in result:
                    if len(message.content) >= 15:
                        exp_plus = int(row[0]) + randint(10,19)

                        update("Members",["xp"],[f"{exp_plus}"],f"id = {message.author.id}")
                        lvl_up = exp_plus/(int(row[1]) * 50)

                        if int(row[1]) <= lvl_up:
                            plus_lvl = int(row[1]) + 1
                            await message.channel.send(f'Ура <@!{message.author.id}>, у тебя новый лвл. Теперь у тебя {plus_lvl} лвл. Ты можешь это проверить при помоши `.rank`.')

                            update("Members",["lvl"],[f"{plus_lvl}"],f"id = {message.author.id}")
                    else:
                        exp_plus = int(row[0]) + randint(3,7)

                        update("Members",["xp"],[f"{exp_plus}"],f"id = {message.author.id}")
                        lvl_up = exp_plus/(int(row[1]) * 50)

                        if int(row[1]) <= lvl_up:
                            plus_lvl = int(row[1]) + 1
                            await message.channel.send(f'Ура <@!{message.author.id}>, у тебя новый лвл. Теперь у тебя {plus_lvl} лвл. Ты можешь это проверить при помоши `.rank`.')

                            update("Members",["lvl"],[f"{plus_lvl}"],f"id = {message.author.id}")

                    if plus_lvl == 5:
                        mem5 = message.guild.get_member(message.author.id)
                        role5 = message.guild.get_role(643949984194101273)
                        role_del5 = message.guild.get_role(643902599661223951)
                        await mem5.add_roles(role5)
                        await mem5.remove_roles(role_del5)
                        await message.channel.send(f"Вам выдана роль `{str(role5).lower()}`")

                    if plus_lvl == 10:
                        mem6 = message.guild.get_member(message.author.id)
                        role6 = message.guild.get_role(643902599468285962)
                        role_del6 = message.guild.get_role(643949984194101273)
                        await mem6.add_roles(role6)
                        await mem6.remove_roles(role_del6)
                        await message.channel.send(f"Вам выдана роль `{str(role6).lower()}`")

                    if plus_lvl == 25:
                        mem7 = message.guild.get_member(message.author.id)
                        role7 = message.guild.get_role(680859240583266509)
                        role_del7 = message.guild.get_role(643902599468285962)
                        await mem7.add_roles(role7)
                        await mem7.remove_roles(role_del7)
                        await message.channel.send(f"Вам выдана роль `{str(role7).lower()}`")

                    if plus_lvl == 100:
                        mem8 = message.guild.get_member(message.author.id)
                        role8 = message.guild.get_role(643902598289686556)
                        role_del8 = message.guild.get_role(680859240583266509)
                        await mem8.add_roles(role8)
                        await mem8.remove_roles(role_del8)
                        await message.channel.send(f"Вам выдана роль `{str(role8).lower()}`")
            
            while True:
                try:
                    member = 0
                    members = message.guild.members
                    for i in range(len(members)):
                        if members[i].status == Status.online:
                            member += 1

                        elif members[i].status == Status.idle:
                            member += 1

                        elif members[i].status == Status.dnd:
                            member += 1

                        elif members[i].status == Status.invisible:
                            member += 1

                    in_online = message.guild.get_channel(703248000839057459)
                    await in_online.edit(name=f'Людей в сети: {member}')
                except:
                    pass

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        if not message.author.bot:
            print(f"{message.author} delete {message.content} channel {message.channel}")
            channel_logs = message.guild.get_channel(688373372945694725)
            await channel_logs.send(embed = Embed(description = f"{message.author} delete `{message.content}` channel {message.channel}", colour = Colour.from_rgb(207,192,0)))

    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
        if not before.author.bot:
            channel_logs = before.guild.get_channel(688373372945694725)
            await channel_logs.send(embed = Embed(description = f"{before.author} изменил сообщение `{before.content}` на `{after.content}`",colour = Colour.orange()))

def setup(client):
    client.add_cog(Messages(client))