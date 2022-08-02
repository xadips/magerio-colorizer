import os
import random
import time

import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild_id = os.getenv('GUILD_ID')
mager_id = os.getenv('MAGER_ID')

bot = commands.Bot(command_prefix='.sus.')


@bot.event
async def on_ready():
    guild = bot.get_guild(int(guild_id))
    user = await guild.fetch_member(int(mager_id))
    while True:
        color = random.choice(open('colors.txt').readlines())
        await user.edit(nick='Magerio' + ' ' + color)
        time.sleep(86400)


bot.run(token)