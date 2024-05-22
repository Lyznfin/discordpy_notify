import discord, os, asyncio
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
import os

load_dotenv()
# Load the token in the .env file
bot_credential = os.getenv('BOTCREDENTIAL')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

statuses = [
    "melodies that echo through the enchanted forests of Erendor!",
    "verses that dance in the halls of the ancient dwarven mines!",
    "tales of valor and heroism in the courts of the elven kingdoms!",
    "harmonies that resonate in the heart of the dragon's lair!",
    "rhythms that stir the spirits of the forgotten ruins of Azura!"
]

bot_status = cycle(statuses)

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))

@bot.event
async def on_ready():
    print('Ready for service!')
    change_status.start()

async def load():
    for filename in os.listdir(r"C:\Users\manzi\VSCoding\Discord.py\src\cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")

async def main():
    async with bot:
        await load()
        await bot.start(bot_credential)

if __name__ == "__main__":
    asyncio.run(main())