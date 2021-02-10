import os
from os import listdir
from os.path import isfile, join
import discord
import sys
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands 

scheduler = AsyncIOScheduler()
this = sys.modules[__name__]
this.running = False

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')
COMMAND = os.getenv('COMMAND_PREFIX')
#############################################################################

cogs  = ["cogs.silly", "cogs.insult"]
client = commands.Bot(command_prefix=COMMAND, description="Roz's Bot")
activity_status = "Looking down on you."

@client.event
async def on_ready():
    # Types of Activities: Playing, Streaming, Listening, Watching.
    
    # > For more info: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Bot.change_presence
    
    # They're commented out, you can only choose one. You can't have 2 running at a time.
    
    # await client.change_presence(activity=discord.Game(name=activity_status))
    # await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_status))
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
    
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

    for cog in cogs: # Looks for the cogs,
        client.load_extension(cog) # Loads the cogs.
    return

client.run(TOKEN) # Using the value stored in variable 'TOKEN'