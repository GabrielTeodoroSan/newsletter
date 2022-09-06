import discord
from news import getNews
from discord.ext import commands
from settings import DISCORD

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print('Tudo certo')


@bot.command()
async def news(ctx):
    notices = getNews()
    for notice in notices:
            await ctx.send(notice[1])



bot.run(DISCORD['token'])
