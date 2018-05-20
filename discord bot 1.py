#imports
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
#clients
Client = discord.Client()
client = commands.Bot(command_prefix = ".")

#ready text
@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
#self roles module
    if message.content.upper().startswith(".IAM UBER"):
        find_role = discord.utils.get(message.server.roles, name="[Uber]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Uber role")
    elif message.content.upper().startswith(".IAM TRYHARD"):
        find_role = discord.utils.get(message.server.roles, name="[Tryhard]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Tryhard role")
    elif message.content.upper().startswith(".IAM SPY"):
        find_role = discord.utils.get(message.server.roles, name="[Spy]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Spy role")
    elif message.content.upper().startswith(".IAM WARRIOR"):
        find_role = discord.utils.get(message.server.roles, name="[Warrior]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Warrior role")
    elif message.content.upper().startswith(".IAM MEDIC"):
        find_role = discord.utils.get(message.server.roles, name="[Medic]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Medic role")
    elif message.content.upper().startswith(".IAM NOODLE"):
        find_role = discord.utils.get(message.server.roles, name="[Noodle]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Noodle role")
    elif message.content.upper().startswith(".IAM NUGGET"):
        find_role = discord.utils.get(message.server.roles, name="[Nugget]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Nugget role")
    elif message.content.upper().startswith(".IAM NOOB"):
        find_role = discord.utils.get(message.server.roles, name="[Noob]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Noob role")
    elif message.content.upper().startswith(".IAM OMEGA"):
        find_role = discord.utils.get(message.server.roles, name="[Omega Rank Ω]")
        await client.add_roles(message.author, find_role)@client.event
        await client.send_message(message.channel, "You have self asigned the Omega role")
    elif message.content.upper().startswith(".IAM DELTA"):
        find_role = discord.utils.get(message.server.roles, name="[Delta Rank Δ]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Delta role")
    elif message.content.upper().startswith(".IAM ALPHA"):
        find_role = discord.utils.get(message.server.roles, name="[Alpha Rank α]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Alpha role")
    elif message.content.upper().startswith(".IAM ALLY"):
        find_role = discord.utils.get(message.server.roles, name="[Ally]")
        await client.add_roles(message.author, find_role)
        await client.send_message(message.channel, "You have self asigned the Ally role")
#yesno module
    elif message.content.upper().startswith(".YESNO"):
        coin = random.randint(1, 2)
        if coin == 1:
            coin = "Yes"
            await client.send_message(message.channel, coin)
        else:
            coin = "No"
            await client.send_message(message.channel, coin)
#faces module
    elif message.content.upper() == "SHRUG":
            await client.send_message(message.channel, "¯\_(ツ)_/¯")
    elif message.content.upper() == "FLIP":
            await client.send_message(message.channel, "(╯°□°）╯︵ ┻━┻")
    elif message.content.upper() == "UNFLIP":
            await client.send_message(message.channel, "┬─┬﻿ノ( ゜-゜ノ)")
    elif message.content.upper() == "LENNY":
            await client.send_message(message.channel, "( ͡° ͜ʖ ͡°)") 
    elif message.content.upper() == "FITE":
            await client.send_message(message.channel, "(ง’̀-‘́)ง")
#change status
    elif message.content.upper().startswith(".STATUS CHANGE"):
            await client.change_presence(game=discord.Game(name='Playing on The Minecraft Server Omegarealm.com'))
            await client.send_message(message.channel, "You have changed the bot status (this is a bot admin only command therefore it will only change the status if you are the host and have changed the code)")





#bot login
client.run("NDM5ODY3NzU4MjM1MDkwOTY0.Dccb8Q.Oc9i_bcO-ZK4X-txceVE5sGbgic")
