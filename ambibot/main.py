import asyncio
import os
import discord
from discord.ext import commands

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix = '**', intents=intents)
client.remove_command('help')

#main and tech stuff
@client.event
async def on_ready():
    #set status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Vibing │ **help"))
    #print when logged in
    print(f"{client.user} has logged in.")
    print('bot ready...')

#ping command
@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: pong ;) {round(client.latency * 1000)}ms')

# @client.command(aliases=["apagar", "callate"])
# async def shutdown(ctx):
    # usrname = ctx.author.name
    # print(f"{usrname} apago el bot")
    
    await ctx.send(f"{usrname} Apago el bot")
    print("Apagando el bot...")
    await ctx.send("Shutting down...")
    await client.close()

#load cogs
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"loaded cog {filename}")

#start bot
async def main():
    await load()
    await client.start(TOKEN)

async def closebot():
    await client.close()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("exiting...")
    asyncio.run(closebot())

#token

#client.run('')

