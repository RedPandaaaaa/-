# --------------------------------------------------
# WikiBot (Version 2.1)
# by Sha-chan~
# last version released on the 23 of May 2021
#
# code provided with licence :
# GNU General Public Licence v3.0
# --------------------------------------------------

import discord
import os
from random import randint

client = discord.Client()
__version__ = "1.2.1"

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'בדיקה' in message.content.lower():
        await message.channel.send('שלום :)')
    if 'שלום עולם' in message.content.lower():
        await message.channel.send('עולם: שלום גם לך')
    if 'אמא של שמעון פרס' in message.content.lower():
        await message.channel.send('https://www.youtube.com/watch?v=ayhRQMljhyk')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="▶ ^עזרה ◀"))
    print("Online.")

client.run('')