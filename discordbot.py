import os
import traceback
import random

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    ch = client.get_channel('638744494610841603')
    await ch.send("Wah Gwaan!")

    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def dice(ctx):
    roll = random.randint(1, 6)
    await ctx.send(f"{roll}")


@bot.command()
async def debug(ctx):
    dbgmsg = "this is debug message!!"
    await ctx.send(f"{dbgmsg}")


bot.run(token)
