# Probotlib

A small library that helps verify credit transfers.

# How to use

You must first install the discord.py library.

```sh

pip install discord.py

```

You must first install the library.

```sh

pip install probotlib

```
# Note

You should make credit command in probot in short c and the propbot is in English.

# Code example

```py

import discord
from discord.ext import commands
from probotlib import Transfer

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.command()
async def buy(ctx):

    role = ctx.guild.get_role() 
    user = ctx.author

    #Add transfer data
    trans = Transfer(owner_id="add owner id", probot_id="add probot id", amount="add amount", server_id="add server id")

    #Get transfer embed 
    embed = trans.trans_embed(bot=client)
    await ctx.send(embed=embed)

    #Transfer process started
    role_buy = await trans.trans_amount(ctx=ctx)

    if role_buy:
        await user.add_roles(role)
    else:
        await ctx.send("time is up")

```