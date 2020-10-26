from secrets import *
import discord
from discord.ext import commands
import random

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

# @bot.command(pass_context = True)
# async def kick(ctx, user_name: discord.User):
#     try:
#         await ctx.guild.kick(user_name, reason = "hahaha loser you got kicked")
#         await ctx.send("Kicked " + user_name.mention)
#     except discord.Forbidden:
#         await ctx.send("Insufficient permissions to kick " + user_name.mention)

votes = {}
VOTES_TO_KICK = 1

@bot.command(pass_context = True)
async def votekick(ctx, user_name: discord.User):
    if user_name not in votes:
        votes[user_name] = 1
    else:
        votes[user_name] = votes.get(user_name, 0) + 1
    if votes[user_name] >= VOTES_TO_KICK:
        try:
            await ctx.guild.kick(user_name, reason = "You were votekicked")
            await ctx.send(str(votes[user_name]) + "/" + str(VOTES_TO_KICK) + " " + user_name.mention + " was " + random.choice(["", "not "]) + "the imposter.")
            votes[user_name] = 0
        except discord.Forbidden:
            await ctx.send(str(votes[user_name]) + "/" + str(VOTES_TO_KICK) + " " + user_name.mention + " is too powerful to be kicked")
    else:
        await ctx.send(str(votes[user_name]) + "/" + str(VOTES_TO_KICK) + " votes to kick " + user_name.mention)

bot.run(token)