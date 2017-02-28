from discord.ext import commands
from logic import TickToe
import discord.utils
import discord
import logging
import random
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
    if message.content.lower() == ';tick help':
        await bot.send_typing(message.channel)
        #await bot.send_message(message.channel,"Help is on it's way! Check your messages !!")

    await bot.process_commands(message)

def loadCreds():
    with open('creds.json') as f:
        return json.load(f)

if __name__ == '__main__':
    #creds = loadCreds()
    token = loadCreds()['token']

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    bot.run(token)
