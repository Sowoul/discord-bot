#First version of the bot code, before the creation of my streaming project "BoredFlix", which was an inspiration for multiple other commands for the bot.
import discord
from discord.ext import commands
import asyncio
import os
import random as ra
import music
import youtube_dl
bot = commands.Bot(command_prefix = '$')
import random
from urllib.request import Request, urlopen
import re
import datetime
from discord import colour

cogs=[music]
for i in range(len(cogs)):
    cogs[i].setup(bot)

bot.sniped_messages = {}

bot.y = 1

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")


@bot.event
async def on_message_edit(message_before, message_after):
    bot.aut = message_before.author
    bot.cha = message_after.channel
    bot.pin = message_before.author.mention
    bot.bef = message_before.content
    bot.aft = message_after.content
    bot.ava = message_before.author.avatar_url

@bot.command(aliases= ["editsnipe"])
async def esnipe(ctx):
    embed= discord.Embed(description=("**Before**: {}\n **After**: {}".format(bot.bef,bot.aft)), color=0x00ff00)
    embed.set_author(name=f"{bot.aut}",icon_url=bot.ava)
    embed.set_footer(text=f"Edited in #{bot.cha}")
    await ctx.channel.send(embed=embed)
@bot.event
async def on_message_delete(message):
    bot.x = message.content
    bot.y = message.author
    bot.z = message.author.id
    bot.a= message.channel.id
    bot.kk = message.author.avatar_url
    bot.t= message.created_at
    bot.c=message.channel
    bot.png=message.author.mention

@bot.command()
async def snipe(ctx):
    if bot.y == 1:
        await ctx.channel.send("There is nothing to snipe")
    else:
        if bot.z == 896607621220536382:
            return
        else:
            if bot.a == 903662513474900038:
                return
            else:
                embed=discord.Embed(description=bot.x, color=0x00ff00, timestamp=bot.t)
                embed.set_author(name=f"{bot.y}", icon_url=bot.kk)
                embed.set_footer(text=f"Deleted in #{bot.c}")
                await ctx.channel.send(embed=embed)
@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    if avamember == None:
        avamember = ctx.author
        userAvatarUrl = avamember.avatar_url
    else:
        userAvatarUrl = avamember.avatar_url

    embed = discord.Embed(title="{}'s Avatar".format(avamember), color=0x00ff00)
    embed.set_image(url=userAvatarUrl)
    await ctx.channel.send(embed=embed)

@bot.command()
async def gayrate(ctx, *, gay : discord.Member=None):
    if gay == None:
        gay = ctx.author
    else:
        gay=gay
    gayra = ra.randint(1, 100)
    embed=discord.Embed(description=f"You are {gayra}% gay", color=0x00ff00)
    embed.set_author(name=gay, icon_url=gay.avatar_url)
    await ctx.channel.send(embed=embed)

@bot.command()
async def pp(ctx,*,pp : discord.Member=None):
    if pp == None:
        pp = ctx.author
    else:
        pp=pp
    ppsize= ra.randint(0,15)
    pen= ppsize*"="
    embed = discord.Embed(description=f"8{pen}D", color=0x00ff00)
    embed.set_author(name=pp, icon_url=pp.avatar_url)
    await ctx.channel.send(embed=embed)
@bot.command()
async def simprate(ctx, *, gay : discord.Member=None):
    if gay == None:
        gay = ctx.author
    else:
        gay=gay
    gayra = ra.randint(1, 100)
    embed=discord.Embed(description=f"You are {gayra}% simp", color=0x00ff00)
    embed.set_author(name=gay, icon_url=gay.avatar_url)
    await ctx.channel.send(embed=embed)
@bot.command(pass_context = True, aliases= ["blackjack"])
async def bj(ctx):
    cat =ctx.author.id
    a = ['Hearts', 'Club', 'Hearts', 'Spade']
    b = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    num1 = random.choice(b)
    num2 = random.choice(b)
    num3 = random.choice(b)
    num4 = random.choice(b)
    num5 = random.choice(b)
    num6 = random.choice(b)
    num7 = random.choice(b)
    num8 = random.choice(b)
    n1 = random.choice(a)
    n2 = random.choice(a)
    n3 = random.choice(a)
    n4 = random.choice(a)
    n5 = random.choice(a)
    n6 = random.choice(a)
    n7 = random.choice(a)
    n8 = random.choice(a)
    embed = discord.Embed(description=f"The dealer's hand:\n {num1} of {n1}\n?\n\nYour Hand:\n{num2} of {n2}\n{num3} of {n3}", color=0x00ff00)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)

    async def _command(ctx):
        await ctx.send(f"Hit or Stand?")

    def check(msg: discord.Message):
        return msg.author.id == ctx.author.id and msg.channel.id == ctx.channel.id and msg.content.lower() in ["hit", "stand"]

    msg = await bot.wait_for(event='message', check= check)
    if msg.author.id != cat:
        await bot.wait_for("message")

    elif msg.author.id == cat:
        pass

    if msg.content.lower() == "hit":
        n = 1
    elif msg.content.lower() == 'stand':
        n = 2


    dis = {
        'Ace': 10,
        'Queen': 10,
        'Jack': 10,
        'King': 10,
        0: 0,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10
    }


    if n == 2:
        num6 = 0
        if int(dis[num1]) + int(dis[num4]) < 17:
            if int(dis[num1]) + int(dis[num4]) + int(dis[num5]) >= 17:
                embed1 = discord.Embed(
                    description=f"The dealer's hand:\n {num1} of {n1}\n{num4} of {n4}\n{num5} of {n5}",
                    color=0x00ff00)
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed1)
        else:
            num5 = 0
            if int(dis[num1]) + int(dis[num4]) > 17:
                embed1 = discord.Embed(
                    description=f"The dealer's hand:\n {num1} of {n1}\n{num4} of {n4}",
                    color=0x00ff00)
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed1)
        if int(dis[num1]) + int(dis[num4]) + int(dis[num5]) < 17:
            embed1 = discord.Embed(
                description=f"The dealer's hand:\n {num1} of {n1}\n{num4} of {n4}\n{num5} of {n5}\n{num7} of {n7}",
                color=0x00ff00)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed1)
        else:
            num7 = 0
        embed= discord.Embed(
            description= f"Your hand\n{num2} of {n2}\n{num3} of {n3}",
            color=0x00ff00)
        await ctx.channel.send(embed=embed)
    elif n == 1:
        embed = discord.Embed(
            description=f"The dealer's hand:\n {num1} of {n1}\n?",
            color=0x00ff00)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
        embed = discord.Embed(
            description=f"Your hand\n{num2} of {n2}\n{num3} of {n3}\n{num6} of {n6}",
            color=0x00ff00)
        await ctx.channel.send(embed=embed)
    if int(dis[num2]) + int(dis[num3]) + int(dis[num6]) > 21:
        embed = discord.Embed(
            description=f"You busted, you lose",
            color=0xe74c3c
        )
        await ctx.channel.send(embed=embed)
    elif n == 2:
        if int(dis[num1]) + int(dis[num4]) + int(dis[num5]) + int(dis[num7]) > 21:
            embed = discord.Embed(
                description=f"The dealer busted, you win!",
                color=0xf1c40f
            )
            await ctx.channel.send(embed=embed)
            return
        if int(dis[num1]) + int(dis[num4]) + int(dis[num5]) + int(dis[num7]) > int(dis[num2]) + int(dis[num3]) + int(
                dis[num6]):
            embed = discord.Embed(
                description=f"You lose",
                color=0xe74c3c
            )
            await ctx.channel.send(embed=embed)
        elif int(dis[num2]) + int(dis[num3]) + int(dis[num6]) == int(dis[num1]) + int(dis[num4]) + int(dis[num5]) + int(
                dis[num7]):
            embed = discord.Embed(
                description=f"You tied!",
                color=0x1abc9c
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"You win!",
                color=0xf1c40f
            )
            await ctx.channel.send(embed=embed)
    elif n == 1:
        await ctx.send("Hit or stand")
        async def _command(ctx):
            await ctx.send(f"Hit or Stand?")

        def check(msg: discord.Message):
            return msg.author.id == ctx.author.id and msg.channel.id == ctx.channel.id and msg.content.lower() in [
                "hit", "stand"]

        msg = await bot.wait_for(event='message', check=check)
        if msg.author.id != cat:
            await bot.wait_for("message")

        elif msg.author.id == cat:
            pass

        if msg.content.lower() == "hit":
            cc = 1
        elif msg.content.lower() == 'stand':
            cc = 2

        if int(dis[num1]) + int(dis[num4]) < 17:
            if int(dis[num1]) + int(dis[num4]) + int(dis[num5]) >= 17:
                embed1 = discord.Embed(
                    description=f"The dealer's hand:\n {num1} of {n1}\n{num4} of {n4}\n{num5} of {n5}",
                    color=0x00ff00)
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed1)
        else:
            num5 = 0
            if int(dis[num1]) + int(dis[num4]) >= 17:
                embed1 = discord.Embed(
                    description=f"The dealer's hand:\n {num1} of {n1}\n{num4} of {n4}",
                    color=0x00ff00)
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed1)
        if int(dis[num1]) + int(dis[num4]) + int(dis[num5]) < 17:
            embed1 = discord.Embed(
                description=f"The dealer's hand:\n {num1} of {n1}\n{num4} of {n4}\n{num5} of {n5}\n{num7} of {n7}",
                color=0x00ff00)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed1)
        else:
            num7 = 0
        if cc == 1:
            embed = discord.Embed(
                description=f"Your hand\n{num2} of {n2}\n{num3} of {n3}\n{num6} of {n6}\n{num8} of {n8}",
                color=0x00ff00)
            await ctx.channel.send(embed=embed)
        elif cc == 2:
            embed = discord.Embed(
                description=f"Your hand\n{num2} of {n2}\n{num3} of {n3}\n{num6} of {n6}",
                color=0x00ff00)
            await ctx.channel.send(embed=embed)
            num8 = 0
        if int(dis[num2]) + int(dis[num3]) + int(dis[num6]) + int(dis[num8]) > 21:
            embed = discord.Embed(
                description=f"You busted, you lose",
                color=0xe74c3c
            )
            await ctx.channel.send(embed=embed)
        if int(dis[num1]) + int(dis[num4]) + int(dis[num5]) + int(dis[num7])>21:
            embed = discord.Embed(
                description=f"The dealer busted, you win",
                color=0xe74c3c
            )
            await ctx.channel.send(embed=embed)
        elif int(dis[num1]) + int(dis[num4]) + int(dis[num5]) + int(dis[num7]) > int(dis[num2]) + int(dis[num3]) + int(
                dis[num6]) + int(dis[num8]):
            embed = discord.Embed(
                description=f"You lose",
                color=0xe74c3c
            )
            await ctx.channel.send(embed=embed)

        elif int(dis[num1]) + int(dis[num4]) + int(dis[num5]) + int(dis[num7]) == int(dis[num2]) + int(dis[num3]) + int(
                dis[num6]) + int(dis[num8]):
            embed = discord.Embed(
                description=f"You tied!",
                color=0x1abc9c
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"You win!",
                color=0xf1c40f
            )
            await ctx.channel.send(embed=embed)

@bot.command()
async def stats(ctx, message= None):
    try:

        f = re.split('<ul id="TB">', urlopen(Request('https://blocksmc.com/player/{}'.format(message), headers={'User-Agent': 'Mozilla/5.0'})).read().decode())
        n6 = re.findall(('fa-clock-o"></i> (\S{8})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{7})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{6})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{5})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{4})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{3})'), f[0])
        n6 = n6[0]
        n1 = re.findall(r'id="Wins">(\S{8})', f[1])
        m1 = re.search("\d+", n1[0]).group()
        n2 = re.findall(r'id="Points">(\S{8})', f[1])
        m2 = re.search("\d+", n2[0]).group()
        n3 = re.findall(r'id="Kills">(\S{8})', f[1])
        m3 = re.search("\d+", n3[0]).group()
        n4 = re.findall(r'id="Deaths">(\S{8})', f[1])
        m4 = re.search("\d+", n4[0]).group()
        n5 = re.findall(r'id="Played">(\S{8})', f[1])
        m5 = re.search("\d+", n5[0]).group()

        aaa=int(m3)/int(m4)
        wl= int(m1)/(int(m5)-int(m1))
        embed = discord.Embed(description=f"Points: {m2}\nWins: {m1}\nLosses:{int(m5)-int(m1)}\nPlayed: {m5}\nKills:{m3}\nDeaths: {m4}\n" + "KDR: {:.2f}\nWin loss Ratio: {:.2f}".format(aaa,wl), color=0x00ff00)
        embed.set_author(name=message)
        embed.set_thumbnail(url= "https://minotar.net/helm/{}".format(message))
        embed.set_footer(text= f"Time Played: {n6} Hours")

        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(
            description=f"This player doesnt exist",
            color=0x00ff00
        )
        await ctx.channel.send(embed=embed)
@bot.command(aliases=["lb",'leaderboards'])
async def leaderboard(ctx, message= None):
    if message == None:
        k=1
    else:
        k=int(message)
    req = Request('https://blocksmc.com/the-bridge', headers={'User-Agent': 'Mozilla/5.0'})
    f = urlopen(req).read().decode()
    n = re.findall(('href="player/(\S{20})'), f)
    for i in range(0,49):
        n[i] = n[i].replace('">', ' ')
        n[i] = re.search("\w+", n[i]).group()
    try:
        embed = discord.Embed(
            title= "The Bridge Leaderboards: ",
            description=f"{n[0 + 10*(k-1)]}\n{n[1 + 10*(k-1)]}\n{n[2 + 10*(k-1)]}\n{n[3 + 10*(k-1)]}\n{n[4 + 10*(k-1)]}\n{n[5 + 10*(k-1)]}\n{n[6 + 10*(k-1)]}\n{n[7 + 10*(k-1)]}\n{n[8 + 10*(k-1)]}\n{n[9 + 10*(k-1)]}",
            timestamp=datetime.datetime.utcnow(),
            color = discord.Color.from_rgb(127, 255, 212)

        )
        embed.set_thumbnail(url="https://minotar.net/helm/{}".format(n[0 + 10*(k-1)]))
        embed.set_footer(text= f"Requested by {ctx.author}")

        await ctx.channel.send(embed=embed)

    except IndexError:
        embed = discord.Embed(
            title="The Bridge Leaderboards: ",
            description=f"{n[0 + 10 * (k - 1)]}\n{n[1 + 10 * (k - 1)]}\n{n[2 + 10 * (k - 1)]}\n{n[3 + 10 * (k - 1)]}\n{n[4 + 10 * (k - 1)]}\n{n[5 + 10 * (k - 1)]}\n{n[6 + 10 * (k - 1)]}\n{n[7 + 10 * (k - 1)]}\n{n[8 + 10 * (k - 1)]}",
            color=discord.Color.from_rgb(127,255,212),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url="https://minotar.net/helm/{}".format(n[0 + 10 * (k - 1)]))
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.channel.send(embed=embed)
# @bot.event
# async def dm_command(message):
#     if isinstance(message.channel, discord.channel.DMChannel):
#         @bot.command
#         async def winstart(message):
#             await message.channel.send("Enter the ign")
#             msg = await bot.wait_for("message")
#             f = re.split('<ul id="TB">', urlopen(Request('https://blocksmc.com/player/{}'.format(msg),
#                                                          headers={'User-Agent': 'Mozilla/5.0'})).read().decode())
#             n6 = re.findall(('fa-clock-o"></i> (\S{8})'), f[0])
#             if n6:
#                 pass
#             else:
#                 n6 = re.findall(('fa-clock-o"></i> (\S{7})'), f[0])
#             if n6:
#                 pass
#             else:
#                 n6 = re.findall(('fa-clock-o"></i> (\S{6})'), f[0])
#             if n6:
#                 pass
#             else:
#                 n6 = re.findall(('fa-clock-o"></i> (\S{5})'), f[0])
#             if n6:
#                 pass
#             else:
#                 n6 = re.findall(('fa-clock-o"></i> (\S{4})'), f[0])
#             if n6:
#                 pass
#             else:
#                 n6 = re.findall(('fa-clock-o"></i> (\S{3})'), f[0])
#             n6 = n6[0]
#             n1 = re.findall(r'id="Wins">(\S{8})', f[1])
#             m1 = re.search("\d+", n1[0]).group()
#             n2 = re.findall(r'id="Points">(\S{8})', f[1])
#             m2 = re.search("\d+", n2[0]).group()
#             n3 = re.findall(r'id="Kills">(\S{8})', f[1])
#             m3 = re.search("\d+", n3[0]).group()
#             n4 = re.findall(r'id="Deaths">(\S{8})', f[1])
#             m4 = re.search("\d+", n4[0]).group()
#             n5 = re.findall(r'id="Played">(\S{8})', f[1])
#             m5 = re.search("\d+", n5[0]).group()
#         async def winstreak(message):
#             if isinstance(message.channel, discord.channel.DMChannel):
#                 if message.content.lower == 'winstreak':
#                     f = re.split('<ul id="TB">', urlopen(Request('https://blocksmc.com/player/{}'.format(msg),
#                                                                  headers={
#                                                                      'User-Agent': 'Mozilla/5.0'})).read().decode())
#                     n6 = re.findall(('fa-clock-o"></i> (\S{8})'), f[0])
#                     if n6:
#                         pass
#                     else:
#                         n6 = re.findall(('fa-clock-o"></i> (\S{7})'), f[0])
#                     if n6:
#                         pass
#                     else:
#                         n6 = re.findall(('fa-clock-o"></i> (\S{6})'), f[0])
#                     if n6:
#                         pass
#                     else:
#                         n6 = re.findall(('fa-clock-o"></i> (\S{5})'), f[0])
#                     if n6:
#                         pass
#                     else:
#                         n6 = re.findall(('fa-clock-o"></i> (\S{4})'), f[0])
#                     if n6:
#                         pass
#                     else:
#                         n6 = re.findall(('fa-clock-o"></i> (\S{3})'), f[0])
#                     n6 = n6[0]
#                     n1 = re.findall(r'id="Wins">(\S{8})', f[1])
#                     d1 = re.search("\d+", n1[0]).group()
#                     n2 = re.findall(r'id="Points">(\S{8})', f[1])
#                     m2 = re.search("\d+", n2[0]).group()
#                     n3 = re.findall(r'id="Kills">(\S{8})', f[1])
#                     m3 = re.search("\d+", n3[0]).group()
#                     n4 = re.findall(r'id="Deaths">(\S{8})', f[1])
#                     m4 = re.search("\d+", n4[0]).group()
#                     n5 = re.findall(r'id="Played">(\S{8})', f[1])
#                     d5 = re.search("\d+", n5[0]).group()
#             if int(m4) - int(m1) == int(d5) - int(d1):
#                 await message.channel.send('Your current winstreak is of {}'.format(int(d1)-int(m1)))
#             else:
#                 print("You dont have an active winstreak")
@bot.command()
async def link(message):
    if isinstance(message.channel, discord.channel.DMChannel):
        await message.channel.send("Enter the ign")
        bot.auta =message.author.id
        bot.assa = await bot.wait_for("message")


@bot.command()
async def winstart(message):
    if isinstance(message.channel, discord.channel.DMChannel):

        await message.channel.send("Enter the ign")
        asda = await bot.wait_for("message")
        if message.author.id == bot.auta and bot.assa.content == asda.content:
            f = re.split('<ul id="TB">', urlopen(Request('https://blocksmc.com/player/{}'.format(asda.content),
                                                                     headers={'User-Agent': 'Mozilla/5.0'})).read().decode())

            n1 = re.findall(r'id="Wins">(\S{8})', f[1])
            bot.m1 = re.search("\d+", n1[0]).group()
            n2 = re.findall(r'id="Points">(\S{8})', f[1])
            m2 = re.search("\d+", n2[0]).group()
            n3 = re.findall(r'id="Kills">(\S{8})', f[1])
            m3 = re.search("\d+", n3[0]).group()
            n4 = re.findall(r'id="Deaths">(\S{8})', f[1])
            m4 = re.search("\d+", n4[0]).group()
            n5 = re.findall(r'id="Played">(\S{8})', f[1])
            bot.m5 = re.search("\d+", n5[0]).group()
            await message.channel.send('You have started a winstreak counter, your current wins are {}'.format(bot.m1))
        else:
            message.channel.send('Wrong person')

@bot.command()
async def spank(ctx,*, sp : discord.Member = None):
    if sp == None:
        sp = ctx.author
    embed = discord.Embed(color=0x00ff00, title=f'{ctx.author.name} spanked you')
    embed.set_image(url='https://c.tenor.com/V8vUcWo4dLIAAAAM/spank-peach.gif')
    embed.set_author(name=sp, icon_url=sp.avatar_url)
    await ctx.channel.send(embed=embed)



@bot.command()
async def winstreak(message):

    aasa = 1
    if isinstance(message.channel, discord.channel.DMChannel):
      await message.channel.send("Enter the ign")
      msg = await bot.wait_for("message")
      f = re.split('<ul id="TB">', urlopen(Request('https://blocksmc.com/player/{}'.format(msg.content),
                                                                 headers={
                                                                     'User-Agent': 'Mozilla/5.0'})).read().decode())

    n1 = re.findall(r'id="Wins">(\S{8})', f[1])
    d1 = re.search("\d+", n1[0]).group()
    n2 = re.findall(r'id="Points">(\S{8})', f[1])
    m2 = re.search("\d+", n2[0]).group()
    n3 = re.findall(r'id="Kills">(\S{8})', f[1])
    m3 = re.search("\d+", n3[0]).group()
    n4 = re.findall(r'id="Deaths">(\S{8})', f[1])
    m4 = re.search("\d+", n4[0]).group()
    n5 = re.findall(r'id="Played">(\S{8})', f[1])
    d5 = re.search("\d+", n5[0]).group()
    if int(bot.m5) - int(bot.m1) == int(d5) - int(d1) and int(d5)-int(d1) != 0:
      await message.channel.send('Your current winstreak is of {}'.format(int(d1)-int(bot.m1)))
    else:
      print("You dont have an active winstreak")

@bot.command()
async def quote(message):
    html = re.split('https://boredhumans.b-cdn.net/quotes/', urlopen(
        Request('https://boredhumans.com/quotes.php', headers={'User-Agent': 'Mozilla/5.0'})).read().decode())
    m = str(html[1]).partition(' ')[0]
    m = m.replace('"', '')
    url= 'https://boredhumans.b-cdn.net/quotes/'+ m
    embed= discord.Embed(color= 0x00ff00)
    embed.set_image(url= url)
    await message.channel.send(embed= embed)


@bot.command()
async def watch(ctx,*, message=None):
    if ctx.channel.id == 906801846205710356:
        pass
    else:
        embed = discord.Embed(description='Please head to <#906801846205710356>', color= 0x00ff00)
        await ctx.send(embed= embed)
        return
    a = message.replace(' ', '-')
    try:
        html = Request('https://www1.yts.gy/search/{}'.format(a), headers={'User-Agent': 'Mozilla/5.0'})
        f = urlopen(html).read().decode()
        m = re.split('<h2 class="film-name"><a', f)
        d = re.split('href="', m[3])
        n = re.split('<img data-src="', f)

        if len(n) <= 4:
            ala = len(n)
        else:
            ala = 4
        if ala >2:
            for i in range(1, ala):
                image = (str(n[i]).partition('"')[0])
                k = re.split('title="', n[i])[1].partition('"')[0]
                d = re.split('href="', m[i])
                link = ('https://www1.yts.gy' + d[1].partition(' ')[0].partition('"')[0])
                embed = discord.Embed(title=f"{k}", color=0x00ff00, url=link)
                embed.set_image(url=image)
                await ctx.channel.send(embed=embed)
        elif ala == 1:
            image = (str(n[ala]).partition('"')[0])
            k = re.split('title="', n[ala])[1].partition('"')[0]
            d = re.split('href="', m[ala])
            link = ('https://www1.yts.gy' + d[1].partition(' ')[0].partition('"')[0])
            embed = discord.Embed(title=f"{k}", color=0x00ff00, url=link)
            embed.set_image(url=image)
            await ctx.channel.send(embed=embed)
            return
    except IndexError:
        try:
            f = urlopen(html).read().decode()
            m = re.split('<h2 class="film-name"><a', f)
            d = re.split('href="', m[1])
            n = re.split('<img data-src="', f)
            for i in range(1, len(n)):
                image = (str(n[i]).partition('"')[0])
                k = re.split('title="', n[i])[1].partition('"')[0]
                d = re.split('href="', m[i])
                link = ('https://www1.yts.gy' + d[1].partition(' ')[0].partition('"')[0])
                embed = discord.Embed(title=f"{k}", color=0x00ff00, url=link)
                embed.set_image(url=image)
                await ctx.channel.send(embed=embed)
        except IndexError:
            try:
                f = urlopen(html).read().decode()
                m = re.split('<h2 class="film-name"><a', f)
                d = re.split('href="', m[2])
                n = re.split('<img data-src="', f)
                for i in range(1, len(n)):
                    image = (str(n[i]).partition('"')[0])
                    k = re.split('title="', n[i])[1].partition('"')[0]
                    d = re.split('href="', m[i])
                    link = ('https://www1.yts.gy' + d[1].partition(' ')[0].partition('"')[0])
                    embed = discord.Embed(title=f"{k}", color=0x00ff00, url=link)
                    embed.set_image(url=image)
                    await ctx.channel.send(embed=embed)
            except IndexError:
                embed= discord.Embed(description='I found no movies with that name.', color=0x00ff00)
                await ctx.send(embed=embed)

@bot.command()
async def monkey(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    embed = discord.Embed(color=0x00ff00, title=f'{ctx.author.name} thinks u a monke')
    embed.set_image(url='https://c.tenor.com/rKQF4Ue3z1cAAAAd/monkey-cool-monkey.gif')
    embed.set_author(name=member, icon_url=member.avatar_url)
    await ctx.channel.send(embed=embed)
@bot.command()
async def kmonkey(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    embed = discord.Embed(color=0x00ff00, title=f'{ctx.author.name} gave u a monke miss')
    embed.set_image(url='https://c.tenor.com/XQf30-va9WMAAAAd/monkey-kiss.gif')
    embed.set_author(name=member, icon_url=member.avatar_url)
    await ctx.channel.send(embed=embed)
@bot.command()
async def bwstats(ctx, message= None):
    try:

        f = re.split('<ul id="BW">', urlopen(Request('https://blocksmc.com/player/{}'.format(message), headers={'User-Agent': 'Mozilla/5.0'})).read().decode())
        n6 = re.findall(('fa-clock-o"></i> (\S{8})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{7})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{6})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{5})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{4})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{3})'), f[0])
        n6 = n6[0]
        n1 = re.findall(r'id="Wins">(\S{8})', f[1])
        m1 = re.search("\d+", n1[0]).group()
        n2 = re.findall(r'id="Points">(\S{8})', f[1])
        m2 = re.search("\d+", n2[0]).group()
        n3 = re.findall(r'id="Kills">(\S{8})', f[1])
        m3 = re.search("\d+", n3[0]).group()
        n4 = re.findall(r'id="Deaths">(\S{8})', f[1])
        m4 = re.search("\d+", n4[0]).group()
        n5 = re.findall(r'id="Played">(\S{8})', f[1])
        m5 = re.search("\d+", n5[0]).group()

        aaa=int(m3)/int(m4)
        wl= int(m1)/(int(m5)-int(m1))
        embed = discord.Embed(description=f"Points: {m2}\nWins: {m1}\nLosses:{int(m5)-int(m1)}\nPlayed: {m5}\nKills:{m3}\nDeaths: {m4}\n" + "KDR: {:.2f}\nWin loss Ratio: {:.2f}".format(aaa,wl), color=0x00ff00)
        embed.set_author(name=message)
        embed.set_thumbnail(url= "https://minotar.net/helm/{}".format(message))
        embed.set_footer(text= f"Time Played: {n6} Hours")

        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(
            description=f"This player doesnt exist",
            color=0x00ff00
        )
        await ctx.channel.send(embed=embed)
@bot.command(aliases=["bwlb",'bwleaderboards'])
async def bwleaderboard(ctx, message= None):
    if message == None:
        k=1
    else:
        k=int(message)
    req = Request('https://blocksmc.com/bed-wars', headers={'User-Agent': 'Mozilla/5.0'})
    f = urlopen(req).read().decode()
    n = re.findall(('href="player/(\S{20})'), f)
    for i in range(0, 48):
        n[i] = n[i].replace('">', ' ')
        n[i] = re.search("\w+", n[i]).group()
    try:
        embed = discord.Embed(
            title= "Bedwars Leaderboards: ",
            description=f"{n[0 + 10*(k-1)]}\n{n[1 + 10*(k-1)]}\n{n[2 + 10*(k-1)]}\n{n[3 + 10*(k-1)]}\n{n[4 + 10*(k-1)]}\n{n[5 + 10*(k-1)]}\n{n[6 + 10*(k-1)]}\n{n[7 + 10*(k-1)]}\n{n[8 + 10*(k-1)]}\n{n[9 + 10*(k-1)]}",
            color= discord.Color.from_rgb(139,0,139),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url="https://minotar.net/helm/{}".format(n[0 + 10*(k-1)]))
        embed.set_footer(text= f"Requested by {ctx.author}")

        await ctx.channel.send(embed=embed)
    except IndexError:
        embed = discord.Embed(
            title="Bedwars Leaderboards: ",
            description=f"{n[0 + 10 * (k - 1)]}\n{n[1 + 10 * (k - 1)]}\n{n[2 + 10 * (k - 1)]}\n{n[3 + 10 * (k - 1)]}\n{n[4 + 10 * (k - 1)]}\n{n[5 + 10 * (k - 1)]}\n{n[6 + 10 * (k - 1)]}\n{n[7 + 10 * (k - 1)]}",
            color= discord.Color.from_rgb(139,0,139),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url="https://minotar.net/helm/{}".format(n[0 + 10 * (k - 1)]))
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.channel.send(embed=embed)

@bot.command()
async def solobwstats(ctx, message= None):
    try:

        f = re.split('<ul id="BWS">', urlopen(Request('https://blocksmc.com/player/{}'.format(message), headers={'User-Agent': 'Mozilla/5.0'})).read().decode())
        n6 = re.findall(('fa-clock-o"></i> (\S{8})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{7})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{6})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{5})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{4})'), f[0])
        if n6:
            pass
        else:
            n6 = re.findall(('fa-clock-o"></i> (\S{3})'), f[0])
        n6 = n6[0]
        n1 = re.findall(r'id="Wins">(\S{8})', f[1])
        m1 = re.search("\d+", n1[0]).group()
        n2 = re.findall(r'id="Points">(\S{8})', f[1])
        m2 = re.search("\d+", n2[0]).group()
        n3 = re.findall(r'id="Kills">(\S{8})', f[1])
        m3 = re.search("\d+", n3[0]).group()
        n4 = re.findall(r'id="Deaths">(\S{8})', f[1])
        m4 = re.search("\d+", n4[0]).group()
        n5 = re.findall(r'id="Played">(\S{8})', f[1])
        m5 = re.search("\d+", n5[0]).group()

        aaa=int(m3)/int(m4)
        wl= int(m1)/(int(m5)-int(m1))
        embed = discord.Embed(description=f"Points: {m2}\nWins: {m1}\nLosses:{int(m5)-int(m1)}\nPlayed: {m5}\nKills:{m3}\nDeaths: {m4}\n" + "KDR: {:.2f}\nWin loss Ratio: {:.2f}".format(aaa,wl), color=0x00ff00)
        embed.set_author(name=message)
        embed.set_thumbnail(url= "https://minotar.net/helm/{}".format(message))
        embed.set_footer(text= f"Time Played: {n6} Hours")

        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(
            description=f"This player doesnt exist",
            color=0x00ff00
        )
        await ctx.channel.send(embed=embed)

@bot.command(aliases=["solobwlb",'solobwleaderboards'])
async def solobwleaderboard(ctx, message= None):
    if message == None:
        k=1
    else:
        k=int(message)
    req = Request('https://blocksmc.com/bed-wars-solo', headers={'User-Agent': 'Mozilla/5.0'})
    f = urlopen(req).read().decode()
    n = re.findall(('href="player/(\S{20})'), f)
    for i in range(0, 45):
        n[i] = n[i].replace('">', ' ')
        n[i] = re.search("\w+", n[i]).group()
    try:
        embed = discord.Embed(
            title= "Solo Bedwars Leaderboards: ",
            description=f"{n[0 + 10*(k-1)]}\n{n[1 + 10*(k-1)]}\n{n[2 + 10*(k-1)]}\n{n[3 + 10*(k-1)]}\n{n[4 + 10*(k-1)]}\n{n[5 + 10*(k-1)]}\n{n[6 + 10*(k-1)]}\n{n[7 + 10*(k-1)]}\n{n[8 + 10*(k-1)]}\n{n[9 + 10*(k-1)]}",
            color= discord.Color.from_rgb(139,0,139),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url="https://minotar.net/helm/{}".format(n[0 + 10*(k-1)]))
        embed.set_footer(text= f"Requested by {ctx.author}")

        await ctx.channel.send(embed=embed)
    except IndexError:
        embed = discord.Embed(
            title="Solo Bedwars Leaderboards: ",
            description=f"{n[0 + 10 * (k - 1)]}\n{n[1 + 10 * (k - 1)]}\n{n[2 + 10 * (k - 1)]}\n{n[3 + 10 * (k - 1)]}\n{n[4 + 10 * (k - 1)]}\n   ",
            color= discord.Color.from_rgb(139,0,139),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url="https://minotar.net/helm/{}".format(n[0 + 10 * (k - 1)]))
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.channel.send(embed=embed)
bot.run('ODk2NjA3NjIxMjIwNTM2Mzgy.YWJk6w.6yb2IA6s0yUVLEj3KCUeooTMcn0')
