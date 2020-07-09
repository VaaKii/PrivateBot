from subprocess import check_output
import os
from discord.ext import commands

import utils.checkers as checkers

class Shell(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    @commands.check(checkers.is_owner)
    async def shell(self,ctx,*,arg : str):
        try:
            output = check_output(arg)
            await ctx.send(output.decode("utf-8"))
            await ctx.send(f"Команда {arg} выполена")
        except:
            os.system(arg)
            await ctx.send(f"Команда {arg} выполена")
def setup(client):
    client.add_cog(Shell(client))