from discord.ext import commands
from main import TickToe
import discord.utils
import discord
import random

class Game():
    def __init__(self,bot):
        self.bot = bot
        self.nots = None
        self.cross = None
        self.gameGrid = None
        self.game = TickToe()

    @bot.command(pass_context=True)
    async def setNot(self,ctx):
        if self.nots != None:
            self.nots = str(ctx.message.user)
        else:
            await self.bot.say("nots already taken by "+self.nots)

    @bot.command(pass_context=True)
    async def setCross(self,ctx):
        if self.cross != None:
            self.cross = str(ctx.message.user)
        else:
            await self.bot.say("cross already taken by "+self.cross)

    @bot.command(pass_context=True)
    async def setItem(self,ctx):
        if str(ctx.message.user) == self.cross:
            self.game.main('x')
        elif str(ctx.message.user) == self.nots:
            self.game.main('o')
        else:
            await self.bot.say("You are not a registered player smh")


def setup(bot):
    bot.add_cog(Game(bot))
