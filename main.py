import os
import sys

from discord.ext import commands
from dotenv import load_dotenv
from asyncio import sleep

client = commands.Bot(command_prefix=".",is_owner=506438836943978496)

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    await ctx.message.delete()
    client.load_extension(f"cogs.{extension}")
    print(f"Модуль {extension} загружен")
    await ctx.send(f"Модуль **{extension}** загружен")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    await ctx.message.delete()
    client.unload_extension(f"cogs.{extension}")
    print(f"Модуль {extension} отключён")
    await ctx.send(f"Модуль **{extension}** отключён")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    await ctx.message.delete()
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    print(f"Модуль {extension} перезапущен")
    await ctx.send(f"Модуль **{extension}** перезапущен")

@client.command()
@commands.is_owner()
async def reloadall(ctx):
    await ctx.message.delete()
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f"cogs.{filename[:-3]}")
            client.load_extension(f"cogs.{filename[:-3]}")
            await ctx.send(f"Модуль **{filename}** перезапущен")
            await sleep(0.9)

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f"cogs.{filename[:-3]}")
        except BaseException as e:
            print(f"ERROR: Модуль {filename} не загружен")
            print(f"{filename} : {e}")
        else:
            print(f"Модуль {filename} загружен")

load_dotenv()
client.run(os.getenv("BOT_TOKEN"))