from discord.ext import commands
from main import TickToe
import discord.utils
import discord
import logging
import random
import json

# gloabal stuff
help_attrs = dict(hidden=True)
client = discord.Client ()
description = ''' TickTackToe: Play tick tack toe on discord !! '''
bot = commands.Bot(command_prefix = '!tick',pm_help = True, description = description, help_attrs=help_attrs)

# logger stuff
logger = logging.getLogger('discord')
logger.setLevel(logging.CRITICAL)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# event handelers
@bot.event
async def on_ready ():
    await bot.change_presence(game=discord.Game(name='nots and crosses'),status=discord.Status.online)
    print ('ready \a')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().find(';help') != -1:
        await bot.send_typing(message.channel)
        await bot.send_message(message.channel,"Help is on it's way! Check your messages !!")
    await bot.process_commands(message)
