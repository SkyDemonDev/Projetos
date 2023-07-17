import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.typing = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Online em {bot.user.name}')

@bot.command(name="escolher")
async def escolher(ctx, numero: int):
    numero_aleatorio = random.randint(1, 100)

    if numero == numero_aleatorio:
        await ctx.send(f"Você acertou, o número era {numero_aleatorio}!")
    else:
        await ctx.send(f"Você errou, o número era {numero_aleatorio}!")

bot.run('token')
