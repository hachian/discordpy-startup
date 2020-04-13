import discord
import os
import traceback
import random

client = discord.Client()
bot = discord.ext.commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


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
    await ctx.send("{}".format(roll))


bot.run(token)
