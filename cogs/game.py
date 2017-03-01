from discord.ext import commands
from logic import TickToe
import discord.utils
import discord
import random

bot = commands.Bot(command_prefix = '!tick ')

class Game():
    def __init__(self,bot):
        self.bot = bot
        self.nots = None
        self.cross = None
        self.gameGrid = None
        self.game = TickToe()

    def flush(self):
        self.nots = None
        self.cross = None
        self.gameGrid = None

    @bot.command(pass_context=True)
    async def setNot(self,ctx):
        if self.nots == None:
            self.nots = str(ctx.message.author)
            await self.bot.say("You are an 'o' now")
        else:
            await self.bot.say("nots already taken by "+self.nots)

    @bot.command(pass_context=True)
    async def setCross(self,ctx):
        if self.cross == None:
            self.cross = str(ctx.message.author)
            await self.bot.say("You are an 'x' now")
        else:
            await self.bot.say("cross already taken by "+self.cross)

    @bot.command(pass_context=True)
    async def setItem(self,ctx,message:int):
        content = None
        if str(ctx.message.author) == self.cross:
            if self.game.returnWho() == 'x':
                try:
                    content = self.game.makeMove('x',message)
                    print(content)
                    if content[1]:
                        await self.bot.say(content)
                        # some fancy printing required
                    else:
                        await self.bot.say(content[0])
                        self.flush()
                except (TypeError,IndexError,ValueError):
                    await self.bot.say("range is b/w 0-9")
            else:
                await self.bot.say("ayyyyyy, it ain't your chance !!")
        elif str(ctx.message.author) == self.nots:
            if self.game.returnWho() == 'o':
                try:
                    content = self.game.makeMove('o',message)
                    if content[1]:
                        await self.bot.say(content)
                        # some fancy printing required
                    else:
                        await self.bot.say(content[0])
                        self.flush()
                except (IndexError,ValueError):
                    await self.bot.say("range is b/w 0-9")
            else:
                await self.bot.say("ayyyyyy, it ain't your chance !!")
        else:
            await self.bot.say("You are not a registered player smh")

def setup(bot):
    bot.add_cog(Game(bot))
