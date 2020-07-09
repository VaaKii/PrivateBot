from discord.ext import commands
from asyncio import sleep

from utils.database import select
from utils.database import insert

class Economy(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command()
    @commands.has_permissions(administrator= True)
    async def updeconomybd(self, ctx):
        """Обновляет список пользователей в БД
        Полезно когда бот долго был на тех. работах"""
        await ctx.message.delete()
        i = 0
        i_new = 0
        text = "Обновляем список пользователей\n"
        msg = await ctx.send(text)
        for member in ctx.guild.members:
            i += 1
            name = "Members"
            what = ["id"]
            criterion = f"id = '{member.id}'"
            rezults = select(name, what, criterion)

            if str(rezults) == "[]" and member.bot == False:
                name = "Members"
                into = ["id","xp","lvl","money"]
                values = [member.id, "0","1","0"]
                insert(name, into, values)
                i_new += 1
            else:
                name = "Members"
                into = ["id_bot"]
                values = [member.id]
                insert(name, into, values)
                i_new += 1
            if i%300 == 0:
                await msg.edit(text + f"Проверено {i} пользователей")
                await sleep(0.9)
        await msg.edit(f"Всего проверено: {i}\nДобавлено новых: {i_new}")
        text = "Второй этап. Удаляю лишних пользователей из бд\n"
        msg = await ctx.send(text)

        name = "Members"
        what = ["id"]
        rezults = select(name, what)

        bd_users = []
        for row in rezults:
            bd_users.append(int(row[0]))
        i = 0
        for member in ctx.guild.members:
            bd_users.remove(member.id)
        text += f"id людей которых нет на сервере, но есть в бд:\n{bd_users}\nудаление сделаю после проверки"
        await msg.edit(text)

    @commands.command()
    async def lvl_calc(self,ctx,arg : int):
        await ctx.send(f"Для {arg} уровня нужно {arg*(arg * 50)} xp")
        
def setup(client):
    client.add_cog(Economy(client))