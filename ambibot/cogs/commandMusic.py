import discord
from discord.ext import commands
import youtube_dl
from time import sleep
import asyncio

myurls = []

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


class commandMusic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #--- voice stuff ---

    # ----old Play command

    # @commands.command(aliases=["p"])
    # async def play(self, ctx,url : str):
        # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        # voiceChannel = ctx.author.voice.channel
        # vc = await voiceChannel.connect()
        # if voice == None:
            # vc.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print('done', e))
        
        # else:
            # await voice.disconnect()
            # vc.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print('done', e))



    ## debug command
    @commands.command()
    async def music(self, ctx):
        await ctx.send("loaded")
        print(f"ctx is: {ctx}")
        Guild=ctx.guild
        print(f"guild is: {Guild}")
        voiceChannel = ctx.author.voice.channel
        print("voice channel is: \n", voiceChannel)
        print(f"voice is {ctx.guild.voice_client}")




    ## develper play command for testing


    ## main play command using yt_dl and ffmpeg
    ## --- PLAY ---
    @commands.command(aliases=["p"])
    async def play(self, ctx, url):
        voice = ctx.guild.voice_client
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



        print("done")

    ## --- JOIN ---
    @commands.command(aliases=["j"])
    async def join(self, ctx):
        voice = ctx.guild.voice_client
        print(voice)
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

    ## --- LEAVE ---- :c
    @commands.command(aliases=["l","dc","disconnect"])
    async def leave(self, ctx):
        voice = ctx.guild.voice_client
        if voice == None:
            await ctx.send("not in a voice channel")
        else:
            await voice.disconnect()


    ## --- STATE ---

    @commands.command()
    async def state(self, ctx):
        voice = ctx.guild.voice_client
        print(voice)
        if voice == None:
            await ctx.send("Disconnected")
        else:
            await ctx.send("Connected")

## cog setup
async def setup(bot):
    await bot.add_cog(commandMusic(bot))


