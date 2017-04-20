from discord.ext import commands
from logic import TickToe
import discord.utils
import discord
import logging
import json

# gloabal stuff
client = discord.Client ()
description = ''' TickTackToe: Play tick tack toe on discord !! '''
bot = commands.Bot(command_prefix = '!tick ',pm_help = False, description = description)

# logger stuff
logger = logging.getLogger('discord')
logger.setLevel(logging.CRITICAL)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# extentions / cogs
initial_extensions = [ 'cogs.game' ]

# event handelers
@bot.event
async def on_ready ():
    await bot.change_presence(game=discord.Game(name='nots and crosses'),status=discord.Status.dnd)
    print ('ready \a')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
<<<<<<< Updated upstream
    if message.content.lower() == "!tick who's that pokemon":
        await bot.send_message(
            message.channel,
            """```
            ░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
            ░░▀▄░░░▀░░░░░▀░░░▄▀
            ░░░░▌░▄▄░░░▄▄░▐▀▀
            ░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
            ░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
            ▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
            █░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
            ░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
            ░░░█░░░░░░░░░░░▄▀▄░▀▄
            ░░░█░░░░░░░░░▄▀█░░█░░█
            ░░░█░░░░░░░░░░░█▄█░░▄▀
            ░░░█░░░░░░░░░░░████▀
            ░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀﻿
            ░░░PIKA PIKA░░░░░░
            ```
            """
        )
    if message.content.lower() == '!tick help':
        await bot.send_typing(message.channel)
    if message.content.lower() == '<@285777147807793153> help':
        await bot.send_typing(message.channel)
        await bot.send_message(message.channel,'command prefix is ``!tick``, type ``!tick help`` for help.')
    if message.content.lower() == '<@285777147807793153>':
=======
    if message.content.lower() == ';tick help':
>>>>>>> Stashed changes
        await bot.send_typing(message.channel)
        #await bot.send_message(message.channel,"Help is on it's way! Check your messages !!")

<<<<<<< Updated upstream
@bot.command()
async def help():
    embed = discord.Embed (
        title = '{}'.format(description),
        description = """
        **Pre-Game**:
        --: setCross: select 'x' as player
        --: setSize: set grid size 3 -> 5
        --: setNot: select 'o' as player
        **Game**:
        --: setItem: set either 'o' or 'x' in the grid
        """,
        colour = discord.Colour(0x71368a)
    ).set_author(name = bot.user.name)
    await bot.say(embed=embed)
=======
    await bot.process_commands(message)
>>>>>>> Stashed changes

def loadCreds():
    with open('creds.json') as f:
        return json.load(f)

@bot.command()
async def invite():
    rl = loadCreds()['invite_Link']
    msg = discord.Embed (
            title = 'Invite Link',
            description = 'Invite me to yer server with this >.<',
            image = self.bot.user.avatar_url,
            url = rl
        ).set_author(name = self.bot.user.name,url = rl, icon_url = self.bot.user.avatar_url )
    await self.bot.say(embed=msg)

if __name__ == '__main__':
    #creds = loadCreds()
    token = loadCreds()['token']

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    bot.run(token)
