from secrets import *
import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('/hello'):
        await message.channel.send('Hello!')
    
    # if message.content.lower().startswith('/insult'):
    #     await message.channel.send('ok boomer!')

@bot.command()
async def asdf(ctx, member: discord.Member):
    print("insult at" + ctx)
    await ctx.send("ok boomer {0}".format(member))

client.run(token)