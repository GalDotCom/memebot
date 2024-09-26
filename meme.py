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
    meme_files = os.listdir('images')
    img_name = random.choice(meme_files)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run('token')
