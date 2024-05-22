import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import Context
import asyncio

class Notify(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        print('notify.py is ready!')

    @commands.command()
    async def start(self, ctx: Context, interval: int = 20, times: int = 4, rest: int = 5):
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel!")
            return
        interval *= 60
        rest *= 60
        await ctx.send(f"Notifications will be sent every {interval / 60} minutes, {times} times with {rest / 60} minutes of rest in between")
        await self.notify_loop(ctx, interval, times, rest)

    async def notify_loop(self, ctx, interval, times, rest):
        isResting = 0
        for _ in range((times * 2) - 1):
            if isResting == 0:
                await self.notify(ctx, isResting)
                await ctx.send("Don't you dare getting distracted!")
                await asyncio.sleep(interval)
                isResting = 1
            elif isResting == 1:
                await self.notify(ctx, isResting)
                await ctx.send("Time to rest!")
                await asyncio.sleep(rest)
                isResting = 0
        isResting = 2
        await self.notify(ctx, isResting)
        await ctx.send("Congrats. Today session has ended.")

    @commands.command()
    async def notify(self, ctx: Context, isResting):
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        try:
            if isResting == 0:
                audio_source = discord.FFmpegPCMAudio('statics/sounds/alarm.mp3')
            elif isResting == 1:
                audio_source = discord.FFmpegPCMAudio('statics/sounds/yahoo.mp3')
            elif isResting == 2:
                audio_source = discord.FFmpegPCMAudio('statics/sounds/tut_turu.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(1)
        finally:
            await voice_client.disconnect()

async def setup(bot: Bot):
    await bot.add_cog(Notify(bot))