from secrets import *
import discord
from discord.ext import commands
import random
from datetime import datetime, date
from collections import OrderedDict

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
    embed.add_field(name="/mingbot", value="🤖 displays help for mingbot commands (this message)", inline=False)
    embed.add_field(name="/ping", value="🏓 pong", inline=False)
    embed.add_field(name="/votekick <@user>", value="🗳️ votes to kick the mentioned <@user>", inline=False)
    embed.add_field(name="/insult <@user>", value="♿ insults the mentioned <@user>", inline=False)
    embed.add_field(name="/shot <n>", value="🥃 take a shot and adds <n> to your shot counter", inline=False)
    embed.add_field(name="/clear", value="🚫 clears your shot counter", inline=False)
    embed.add_field(name="/leaderboard", value="🥇 displays the shots leaderboard", inline=False)
    embed.add_field(name="/uptime", value="🕒 shows how long the bot has been running", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

start_time = datetime.now()

@bot.command()
async def uptime(ctx):
    await ctx.send("```\nmingbot has been running since " + str(start_time) + "\nTotal uptime: " + str((datetime.now() - start_time)) + "\n```")

@bot.command()
async def insult(ctx, user: discord.User):
    await ctx.send("ok boomer "+ user.mention)

shot_counts = {}

@bot.command()
async def shot(ctx, n = 1):
    if n == 1:
        word = "a shot"
    else:
        word = str(n) + " shots"
    if ctx.message.author not in shot_counts:
        shot_counts[ctx.message.author] = 0
    shot_counts[ctx.message.author] += n
    await ctx.send(ctx.message.author.mention + " took " + word + "! Shots taken: " + str(shot_counts[ctx.message.author]))

@bot.command()
async def leaderboard(ctx):
    leaderboard = OrderedDict(sorted(shot_counts.items(), key = lambda v: v[1], reverse = True))
    leaderboard_string = "```\n🥃Shots leaderboard🥃\n--------------------\n"
    for x, y in leaderboard.items():
        leaderboard_string = leaderboard_string + str(x) + "\t" + str(y) + "\n"
    leaderboard_string += "\n```"
    await ctx.send(leaderboard_string)

@bot.command()
async def clear(ctx):
    if ctx.message.author in shot_counts and shot_counts[ctx.message.author] > 0:
        shot_counts[ctx.message.author] = 0
        await ctx.send(ctx.message.author.mention + " cleared their shot count. Round two when?")
    else:
        await ctx.send(ctx.message.author.mention + " didn't have any shots to clear... weak")

@bot.command()
async def trickortreat(ctx):
    if random.choice([True, False]) or ctx.message.author == "anitazma#3447":
        img_url = "https://media1.tenor.com/images/5825c44d1dbd0771cba9f13d5eb1791a/tenor.gif"
        text = "Get spooked " + ctx.message.author.mention
    else:
        img_url = "https://media1.tenor.com/images/8b10408f29a0e6b90f06e13af8c63af9/tenor.gif"
        text = "You get a treat " + ctx.message.author.mention
    await ctx.send(text + "\n" + img_url)

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