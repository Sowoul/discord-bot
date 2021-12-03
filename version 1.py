import discord
import os
import random as ra
from discord.ext import commands
from music_cog import music_cog
from datetime import date, datetime
import time
import asyncio




bot = commands.Bot(command_prefix='$')

client = discord.Client()
bot_prefix="$"
bot = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print('Started as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.lower() == '':
        n=1
        while n >1:
            await message.channel.send('<@398005535275876352>')
    if message.author == client.user:
        return
    if message.author.id == 1:
        await message.delete()
        return
    if (message.channel.id == 910126701516836864) :
        await message.delete()
        embed = discord.Embed(description=message.content, color=0x00ff00)
        await message.channel.send(embed=embed)
        return
    if message.content.lower() == ('$cog'):
        await message.channel.send('<a:coggers:866321258199121940>')
        await message.delete()
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('3hf'):
        await message.channel.send('But did you know that 3hf is gay?')
    elif message.content.startswith('dog'):
        await message.channel.send('Thats cool but dog123 is still the best doge')

    elif message.content.lower() == "$gaycica":
        await message.channel.send('https://cdn.discordapp.com/attachments/866069060734418978/896793256799658034/gay.png')
    elif message.content.lower() == 'yafay':
        await message.channel.send('https://cdn.discordapp.com/attachments/866069060734418978/892991870039392286/image0.png')
    elif message.content.lower() == 'Yafay':
        await message.channel.send('https://cdn.discordapp.com/attachments/866069060734418978/892991870039392286/image0.png')
    elif message.content.lower() == 'everyone':
        await message.channel.send('https://www.youtube.com/watch?v=E5I6WH0DLSw&ab_channel=vanceman2009')
    if (message.content.lower() == "atom" or message.content.lower() == "Atom"):
        await message.channel.send("https://www.youtube.com/channel/UC2r6JGiZHCRMUctSvFvLuhg")
        time.sleep(3)
        return
    if message.content.startswith('https://media.giphy.com/media/d4FzLpEs7didEdWbUe/giphy.gif'):
        await message.delete()
    if (message.content.startswith('https://tenor.com/view/epilepsi-patates-pattes-denemepattes-gif-13248094') or message.content.startswith('https://cdn.discordapp.com/attachments/866069060734418978/899284696729522206/yes.gif') or message.content.startswith('cdn')):
        await message.delete()
    if message.content.startswith('falling woman'):
        await message.channel.send('https://tenor.com/view/slipped-slip-fat-fall-fail-gif-12554495')
    if message.content.startswith('phat ass'):
        await message.channel.send('https://cdn.discordapp.com/attachments/887936107226988544/897166273824313404/unknown-19.png')
    if message.content.startswith('$hug'):
        if message.content.lower() == "$hug":
            await message.channel.send("Enter who to hug dummy")
        else:
            await message.channel.send('{} hugged you!\nAww :3\nhttps://tenor.com/view/puuung-cute-hug-love-gif-13113601'.format(message.author.mention))
    if message.content.startswith("$kill"):
        if message.content.lower() == "$kill":
            await message.channel.send("Mention who you wanna kill dumbass")
        elif message.content.lower() == "$kill <@882142995875512340>":
            await message.channel.send('You dare defy my master?')
        else:
            await message.channel.send("{} Just killed you\nOh no!\nhttps://tenor.com/view/runover-kid-child-road-kill-running-over-gif-5744950".format(message.author.mention))

    if str(client.user.id) in message.content:
        await message.channel.send('Fuk off, im doing ur mom')

    if message.content.lower() == ('$coinflip'):
        if ra.randint(1,2) == 1:
            await message.channel.send('Its a heads')
        else:
            await message.channel.send('Its a tails')

@bot.command()
async def say(ctx,arg):
    await ctx.send(arg)
@client.event
async def on_member_join(member):
    await member.send('Welcome to gaymers kid')


client.run('ODk2NjA3NjIxMjIwNTM2Mzgy.YWJk6w.6yb2IA6s0yUVLEj3KCUeooTMcn0')
