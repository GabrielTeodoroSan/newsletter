from email.mime import image
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
        try:
            embed = discord.Embed(title=notice[0], url=notice[1], color=0x32D5BC)
            embed.set_image(url=notices[2])
            print(f"{embed.title} // {embed.url} // {embed.image}")
            await ctx.send(embed=embed)
        except:
            ctx.send("Ocorreu um erro...")



bot.run(DISCORD['token'])
