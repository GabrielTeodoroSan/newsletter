import discord
from news import getNews
from discord.ext import commands
from settings import DISCORD

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Tudo certo')


bot.run(DISCORD['token'])
