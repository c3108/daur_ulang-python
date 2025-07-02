import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Penting untuk bisa membaca pesan

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot berhasil login sebagai {bot.user}')

@bot.command()
async def info(ctx):
    await ctx.send('Halo! Sampah apa yang ingin kamu daur ulang? Ketik `!plastik`, `!kain`, atau `!kertas`.')

@bot.command()
async def plastik(ctx):
    ide = "\n- Pot tanaman dari botol bekas, \n- Lampu hias dari sendok plastik, \n- Tempat pensil dari galon kecil."
    await ctx.send(f'Ide daur ulang plastik: {ide}')

@bot.command()
async def kain(ctx):
    ide = "\n- Tas belanja dari kaos bekas, \n- Bantal kecil dari kain, \n- Kuncir rambut dari kain sisa."
    await ctx.send(f'Ide daur ulang kain: {ide}')

@bot.command()
async def kertas(ctx):
    ide = "\n- Bingkai foto dari karton bekas \n- Kertas daur ulang buatan sendiri \n- Origami dari majalah bekas."
    await ctx.send(f'Ide daur ulang kertas: {ide}')

bot.run("TOKEN")
