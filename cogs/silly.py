from discord.ext import commands
from utils.utils import *
import random 

class Silly(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='say')
    async def say(self, ctx, *, message:str):
        """Make the bot say whatever you want it to say"""
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(strip_global_mentions(message, ctx))

    @commands.command()
    async def coinflip(self, ctx):
        choices = ["Heads", "Tails", "Your bitch-ass hands dropped the goddamn coin. Do it again."]
        rancoin = random.choice(choices)
        await ctx.send(rancoin)

def setup(bot):
    bot.add_cog(Silly(bot))