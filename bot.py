import discord
import random
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt

# Documentation - https://discordpy.readthedocs.io/en/stable/api.html#client

TOKEN = ""
client = commands.Bot(command_prefix=".")
# tx_channels = guild.text_channels

"""
To access the name of any user, use client.user
"""


@client.event
async def on_ready():
    print("-------------------------------")
    print(f"{client.user} is ready to rock!")
    print("-------------------------------")
    activity = discord.Game(name="Gigidi gigidigo")
    await client.change_presence(status=discord.Status.idle, activity=activity)


participants = {"key": []}


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    # check if bot is responding to itself
    if message.author == client.user:
        return

    if message.channel.name == "":
        if user_message.lower() == "!number":
            await message.channel.send(f"Your number is: {random.randint(1, 10000)}")
            return

    if message.channel.name == "":
        channel = client.get_channel()  # paste channel id here
        if user_message.lower() == "moln":
            await channel.send(file=discord.File("ssh.png"))
            return
    if message.channel.name == "":
        if user_message.lower() == "":
            await message.channel.send("")
            await message.channel.send("")
            return

    # Channels with purge activated

    if message.channel.name == "":
        channel = client.get_channel()  # paste channel id here
        if user_message.lower() == "pur":
            await channel.purge(limit=10)
            await message.channel.send("Purged 10 items!")
            return
    if message.channel.name == "":
        channel = client.get_channel()  # paste channel id here
        if user_message.lower() == "pur":
            await channel.purge(limit=20)
            await message.channel.send("Purged 20 items!")
            return

    # Contest channels

    if message.channel.name == "":
        if user_message.lower() == "play":
            participants["key"].append(message.author.name)
            await message.channel.send(
                f"@{username} has been added to the competition!"
            )
            return

    if message.channel.name == "":
        if user_message.lower() == "draw":
            winner = participants["key"][
                random.randint(0, len(participants["key"]) + 1)
            ]
            await message.channel.send(f"The winner is {winner}")
            return

    if message.channel.name == "":
        if user_message.lower() == "":
            await message.channel.send("")
            return


client.run(TOKEN)
