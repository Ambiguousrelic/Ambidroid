import discord
import time
from discord import channel
from discord.ext import commands
from discord_together import DiscordTogether
import random
import asyncio
import youtube_dl
import pyttsx3
engine = pyttsx3.init()


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '**', intents=intents)
client.remove_command('help')

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}


ytdl = youtube_dl.YoutubeDL(ytdlopts)

#main and tech stuff
@client.event
async def on_ready():
    client.togetherControl = await DiscordTogether("NzUyNjg5Njc4MTg0MDg3Njgy.X1bS4w.H7X5H1c9dYupJ8BO8x-9Kimn-54")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Vibing │ **help"))
    print('bot ready...')


@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: pong ;) {round(client.latency * 1000)}ms')


@client.command(aliases=['hlp'])
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.dark_purple()
    )
    embed.set_author(name="Help")
    embed.add_field(name='ping', value='returns client latency', inline=True)
    embed.add_field(name='luv', value='<3', inline=True)
    embed.add_field(name='d20', value='roll a d20', inline=True)
    embed.add_field(name="dx", value="Roll a dx", inline=True)
    embed.add_field(name="youtube", value="youtube", inline=True)
    embed.add_field(name="poker", value="poker", inline=True)
    embed.add_field(name="chess", value="chess", inline=True)
    embed.add_field(name="betrayal", value="betrayal", inline=True)
    embed.add_field(name="fishing", value="fishing", inline=True)
    embed.add_field(name="letter-tile", value="lettertile", inline=True)
    embed.add_field(name="word-snack", value="wordsnack", inline=True)
    embed.add_field(name="doodle-crew", value="doodlecrew", inline=True)
    embed.add_field(name="spellcast", value="spellcast", inline=True)
    embed.add_field(name="awkword", value="awkword", inline=True)
    embed.add_field(name="checkers", value="checkers", inline=True)
    await ctx.send(embed=embed)

##   flavour

@client.command(aliases=['<3'])
async def luv(ctx):
    await ctx.send('<3')


@client.command(aliases=['hf'])
async def havelflip(ctx):
    await ctx.send(file=discord.File("images/havelflip.gif"))

@client.command(aliases=['smth'])
async def xd(ctx):
    await ctx.send(':cyclone:')

##   dice



@client.command(aliases=['DX','rd','roll','dice'])
async def dx(ctx,dice):
    await ctx.send(random.randint(1,int(dice)))


@client.command(aliases=['rolld20','rd20','r1d20'])
async def d20(ctx):
    await ctx.send(random.randint(1, 20))

@client.command(aliases=['rollf20','rf20','r1f20'])
async def f20(ctx):
    await ctx.send(random.randint(1, 20))

@client.command(aliases=['rolld4','rd4','r1d4'])
async def d4(ctx):
    await ctx.send(random.randint(1, 4))
    
@client.command(aliases=['rolld6','rd6','r1d6'])
async def d6(ctx):
    await ctx.send(random.randint(1, 6))

@client.command(aliases=['rolld8','rd8','r1d8'])
async def d8(ctx):
    await ctx.send(random.randint(1, 8))
    
@client.command(aliases=['rolld10','rd10','r1d10'])
async def d10(ctx):
    await ctx.send(random.randint(1, 10))
    
@client.command(aliases=['rolld12','rd12','r1d12'])
async def d12(ctx):
    await ctx.send(random.randint(1, 12))

@client.command(aliases=['rolld100','rd100','r1d100'])
async def d100(ctx):
    await ctx.send(random.randint(1, 100))

#--------discordtogether

@client.command()
async def youtube(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def poker(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def chess(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def betrayal(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def fishing(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def lettertile(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'letter-tile')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def wordsnack(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'word-snack')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def doodlecrew(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'doodle-crew')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def spellcast(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'spellcast')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def awkword(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'awkword')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def checkers(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'checkers')
    await ctx.send(f"Click the blue link!\n{link}")



# ----Utility i guess

# converts meters to feet
@client.command(aliases=["meterstofeet","map"])
async def mtf(ctx,meter):
    foot = int(meter)*3.281
    round(foot,2)
    await ctx.send(f"{meter} Metros son: {'%.2f'%foot} Pies")


@client.command(aliases=["feettometer","pam"])
async def ftm(ctx,feet):
    meter = int(feet)/3.281
    round(meter,2)
    await ctx.send(f"{feet} Pies son: {'%.2f'%meter} Metros")

#voice stuff

# ----Play

# @client.command(aliases=["p"])
# async def play(ctx,url : str):
    # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # voiceChannel = ctx.author.voice.channel
    # vc = await voiceChannel.connect()
    # if voice == None:
        # vc.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print('done', e))
    
    # else:
        # await voice.disconnect()
        # vc.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print('done', e))
    
 

@client.command(aliases=["p"])
async def play(ctx,url):

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voiceChannel = ctx.author.voice.channel
    if voice == None:
        await voiceChannel.connect()
    elif ctx.voice_client.is_playing():
        ctx.voice_client.stop()
    
    FFMPEG_OPTIONS = {"before_options":"-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5","options":"-vn"}
    YDL_OPTIONS={"format":"bestaudio", "noplaylist":"True"}
    
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info["formats"][0]["url"]
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        ctx.voice_client.play(source)


#----join


@client.command(aliases=["j"])
async def join(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voiceChannel = ctx.author.voice.channel

    print("---------")
    print("Command Join")
    print("voice = " + str(voice))
    print("user voiceChannel = " + str(voiceChannel))
    print("---------")
    if voice == None:
        await voiceChannel.connect()
    else:
        await voice.disconnect()
        await voiceChannel.connect()



#----Leave :c
@client.command(aliases=["l","dc","disconnect"])
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice == None:
        await ctx.send("not in a voice channel")
    else:
        await voice.disconnect()


#----State

@client.command()
async def state(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    print(voice)
    if voice == None:
        await ctx.send("Disconnected")
    else:
        await ctx.send("Connected")

#get user ID
@client.command()
async def hi(ctx):
    print(ctx.author.id)
    usrname = ctx.author.name
    
    await ctx.send(f"Hello there {usrname}")

#tts
@client.command(aliases=["t","speak"])
async def tts(ctx):
    #0 ES-Helena, 1 EN-David, 2 EN-Zira, 3 EN-Hazel, 4 ES-Sabina, 5 JP-Haruka, 6 KR-Heami
    usrid = ctx.author.id
    usrname = ctx.author.name
    
    text = ctx.message.content
    print(f"{usrname} said: {text[5:]}")
    
    rate = engine.getProperty('rate')       # getting details of current speaking rate
    print (f" current voice rate {rate}")  #printing current voice rate
    engine.setProperty('rate', 150)         # setting up new voice rate
    
    #volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    #print (f" current voice rate {volume}")#printing current volume level
    #engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)

    if usrid == 349245657997115413:
        engine.setProperty('voice', voices[0].id)


    #engine.say('Buenas tardes')
    engine.save_to_file(text[5:], 'output.mp3')
    
    engine.runAndWait()
    
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voiceChannel = ctx.author.voice.channel
    
    if voice == None:
        vc = await voiceChannel.connect()
        vc.play(discord.FFmpegPCMAudio('output.mp3'), after=lambda e: print('done', e))
    
    else:
        vc = ctx.voice_client
        vc.play(discord.FFmpegPCMAudio('output.mp3'), after=lambda e: print('done', e))


#token
client.run('NzUyNjg5Njc4MTg0MDg3Njgy.X1bS4w.H7X5H1c9dYupJ8BO8x-9Kimn-54')

