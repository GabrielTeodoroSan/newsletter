import discord
from news import getNews
from discord.ext import commands
from settings import DISCORD


bot = commands.Bot('!')

@bot.event
async def on_ready():
    print('Tudo certo')


bot.run(DISCORD['token'])
