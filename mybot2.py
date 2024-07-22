import discord
from discord.ext import commands
from kodland_utils import *
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send(pass_gen(10))

@bot.command()
async def emoji(ctx):
    await ctx.send(random_emoji())

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def meme(ctx):
    selected = random.choice(os.listdir('images'))
    with open(f'images/{selected}', 'rb') as f:
        pictures = discord.File(f)
    await ctx.send(file=pictures)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#sampah
organik = ['sayur basi', 'kulit pisang', 'makanan basi', 'buah basi']
kertas = ['kardus', 'kertas gorengan', 'kertas', 'paperbag']
plastik = ['botol', 'kresek', 'cup', 'mangkok plastik']
logam = ['hp', 'kabel', 'kaleng', 'baterai', 'timah', 'besi berkarat']

@bot.command()
async def tanya_sampah(ctx):
    await ctx.send('Sampah apa yang anda ingin periksa')
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)  

    #pengecekan
    if message.lower() in organik:
        await ctx.send('ITU MAH SAMPAH JENIS ORGANIK BRO!')
        await ctx.send('Sebaiknya kalian jadikan itu sebagai PUPUK')
    elif message.lower() in kertas:
        await ctx.send('ITU MAH SAMPAH JENIS KERTAS BRO!')
        await ctx.send('Itu bisa di jadikan kerajinan unik')
        await ctx.send('Atau kalian bisa daur ulang lagi menjadi kertas')
    elif message.lower() in plastik:
        await ctx.send('ITU MAH SAMPAH JENIS PLASTIK BRO!')
        await ctx.send('Kalian bisa daur ulang')
        await ctx.send('Sapa tau kau mau jadiin mainan yakan')
    elif message.lower() in logam:
        await ctx.send('BRO ITU SAMPAH JENIS LOGAM!')
        await ctx.send('Lu bisa daur ulang biar lebih baik')
        await ctx.send('Setelah lu daur ulang lu bisa jadikan seperti perabotan rumah')
        await ctx.send('Lu juga bisa jadikan karya seni seperti patung')
    else:
        await ctx.send('LAH,,, ITUMAH BUKAN SAMPAH KOCAK!!')
