import sys,traceback
import asyncio

from discord.ext import commands
from textwrap import wrap

import utils.checkers as checkers
import configs.guildconfig as guildconfig

def divider(text:str = None) -> str:
    if text != None:
        str_text = str(text)
        len_massiwe = 0
        one_massiwe = []
        massive_in_massive = []
        massive_text = str_text.splitlines(keepends=True)
        for i in range(len(massive_text)):
            if len_massiwe + len(massive_text[i]) <= 1990:
                one_massiwe.append(massive_text[i])
                len_massiwe += len(massive_text[i])
            else:
                massive_in_massive.append(one_massiwe)
                one_massiwe = []
                len_massiwe = 0
                one_massiwe.append(massive_text[i])
                len_massiwe += len(massive_text[i])
        massive_in_massive.append(one_massiwe)
        return massive_in_massive

async def aexec(ctx,code):
    exec(
        f'async def __ex(ctx): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__ex'](ctx)

class Eval(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.command()
    @commands.check(checkers.is_owner)
    async def eval(self,ctx,*,arg):
        if ctx.message.author.id == guildconfig.owner_id:
            try:
                result = await aexec(ctx,arg)
                output = divider(result)
                if output != None:
                    if len(output) != 1:
                        for out in range(len(output)):
                            await ctx.send(f"""```py
{''.join(output[out])}
```""")
                    else:
                        await ctx.send(f"""```py
{''.join(output[0])}
```""") 
                else:
                    await ctx.send(f"""```py
{result}
```""") 
            except:
                error = traceback.format_exc(10)
                error_without_py = error.replace(f'await ctx.send(f"""```py','')
                await ctx.send(f"""```py
{error_without_py}
```""")
        else:
            await ctx.send("Низя")
def setup(client):
    client.add_cog(Eval(client))