from secrets import *
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '/')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "you"))

@bot.command()
async def insult(ctx, user: discord.User):
    print("insult at " + str(ctx))
    await ctx.send("ok boomer "+ user.mention)

@bot.command(pass_context = True)
async def kick(ctx, user_name: discord.User):
    try:
        await ctx.guild.kick(user_name, reason = "hahaha loser you got kicked")
        await ctx.send("Kicked " + user_name.mention)
    except discord.Forbidden:
        await ctx.send("Insufficient permissions to kick " + user_name.mention)


bot.run(token)