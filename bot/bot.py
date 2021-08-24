import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN=os.getenv('DiscordToken')

bot = commands.Bot(command_prefix='!', description='Bot de entretenimiento')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)