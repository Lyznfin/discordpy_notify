from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands import Bot

import random

class Ping(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        print('ping.py is ready!')

    @commands.command()
    async def ping(self, ctx: Context):
        with open("statics/txt/ping.txt", "r") as f:
            random_response = f.readlines()
            response = random.choice(random_response)
        await ctx.send(response)

    @commands.command()
    async def kiss(self, ctx: Context):
        await ctx.send('Kisses you back!')

async def setup(bot: Bot):
    await bot.add_cog(Ping(bot))
