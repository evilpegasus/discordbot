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
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "you /mingbot"))

@bot.command()
async def mingbot(ctx):
    """
    Use this website to generate embeded message
    https://cog-creators.github.io/discord-embed-sandbox/
    """
    embed=discord.Embed(title="mingbot Commands Help", url="https://github.com/evilpegasus/discordbot", color=0x00ff00)
    embed.add_field(name="/mingbot", value="displays help for mingbot commands (this message)", inline=False)
    embed.add_field(name="/ping", value="pong", inline=False)
    embed.add_field(name="/votekick @user", value="votes to kick the mentioned @user", inline=False)
    embed.add_field(name="/insult @user", value="insults the mentioned @user", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def insult(ctx, user: discord.User):
    await ctx.send("ok boomer "+ user.mention)

# @bot.command(pass_context = True)
# async def kick(ctx, user_name: discord.User):
#     try:
#         await ctx.guild.kick(user_name, reason = "hahaha loser you got kicked")
#         await ctx.send("Kicked " + user_name.mention)
#     except discord.Forbidden:
#         await ctx.send("Insufficient permissions to kick " + user_name.mention)

# TODO remove votes and just count voters
votes = {} # key is person being voted, values is number of votes
voters = {} # key is person being voted, values is list of voters
VOTES_TO_KICK = 4

@bot.command(pass_context = True)
async def votekick(ctx, user_name: discord.User):
    if user_name not in votes:
        votes[user_name] = 0
        voters[user_name] = []
    if ctx.message.author not in voters[user_name]:
        votes[user_name] = votes.get(user_name, 0) + 1
        voters[user_name].append(ctx.message.author)
    else:
        await ctx.send(str(votes[user_name]) + "/" + str(VOTES_TO_KICK) + " " + ctx.message.author.mention + " has already voted to kick " + user_name.mention)
        return
    if votes[user_name] >= VOTES_TO_KICK:
        try:
            await ctx.guild.kick(user_name, reason = "You were votekicked")
            embed = discord.Embed(color = discord.Color.red())
            embed.set_image(url = "https://media1.tenor.com/images/f5ef212aa1e15d3f903ee4df41902753/tenor.gif")
            await ctx.send(str(votes[user_name]) + "/" + str(VOTES_TO_KICK) + " " + user_name.mention + " was " + random.choice(["", "not "]) + "the imposter.", embed = embed)
            votes.pop(user_name, 0)
            voters.pop(user_name, 0)
        except discord.Forbidden:
            await ctx.send(str(votes[user_name]) + "/" + str(VOTES_TO_KICK) + " " + user_name.mention + " is too powerful to be kicked")
            votes.pop(user_name, 0)
            voters.pop(user_name, 0)
    else:
        await ctx.send(str(votes[user_name]) + "/" + str(VOTES_TO_KICK) + " votes to kick " + user_name.mention)

bot.run(token)