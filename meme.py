import discord
from discord.ext import commands
import os
import random
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} ha iniciado sesión.')
@bot.command()
async def mem(ctx):
    memes = os.listdir('images')
    selected_meme = random.choice(memes)
    with open(f'images/{selected_meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run('token')
