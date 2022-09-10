import discord
from discord.ext import commands
from settings import DISCORD
from news import generateNotices

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print('Tudo certo')


@bot.command()
async def news(ctx):
    notices = generateNotices()
    for notice in notices:
        try:    
            embed = discord.Embed(title=notice[0], url=notice[1], color=0x32D5BC)
            embed.set_image(url=notice[2])
            await ctx.send(embed=embed)
        except:
            ctx.send("Ocorreu um erro...")



bot.run(DISCORD['token'])
