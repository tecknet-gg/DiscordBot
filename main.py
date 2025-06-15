import asyncio
from importlib.metadata import always_iterable

import discord
from discord.ext import commands
from discord.ext.commands import bot_has_role
from prawcore.util import authorization_error_class

from CustomGeneration import *

# Define intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def sendMessage(message, type, ctx):
    author = ctx.author.id
    # Logic to check cooldown
    await ctx.send(message)


@bot.commands(name="roast")
async def roast(ctx, target: discord.Member):
    roast = generateRoast(ctx.author)
    await sendMessage(roast, "roast", ctx)
