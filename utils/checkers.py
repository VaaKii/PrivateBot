import configs.guildconfig as guildconfig

async def is_owner(ctx):
    if guildconfig.owner_id == ctx.author.id:
        return True
    await ctx.send('Тебе эта комадна запрешена!')
    return False