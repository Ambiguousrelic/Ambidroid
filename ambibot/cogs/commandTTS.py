import discord
from discord.ext import commands
import pyttsx3

##initialize engine
engine = pyttsx3.init()



class commandtts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    ##tts
    @commands.command(aliases=["t","speak"])
    async def tts(self, ctx):
        ##0 ES-Helena, 1 EN-David, 2 EN-Zira, 3 EN-Hazel, 4 ES-Sabina, 5 JP-Haruka, 6 KR-Heami
        usrid = ctx.author.id
        usrname = ctx.author.name
        text = ctx.message.content
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')       # getting details of current speaking rate
        volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)

        print(f"{usrname} said: {text[5:]}")
        print (f" current voice rate {rate}")  #printing current voice rate
        print (f" current voice rate {volume}")#printing current volume level

        engine.setProperty('voice', voices[4].id)
        engine.setProperty('rate', 250)         # setting up new voice rate
        engine.setProperty('volume',1.5)        # setting up volume level  between 0 and 1
        
        ##if user is x set voice to helena
        # if usrid == exampleid:
            # engine.setProperty('voice', voices[0].id)
        


        ## save the mp3 file
        engine.save_to_file(text[5:], 'output.mp3')
        engine.runAndWait()
        #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice = ctx.guild.voice_client
        voiceChannel = ctx.author.voice.channel
        
        if voice == None:
            await voiceChannel.connect()

        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        vc = ctx.voice_client
        vc.play(discord.FFmpegPCMAudio('output.mp3'), after=lambda e: print('done', e))


async def setup(bot):
    await bot.add_cog(commandtts(bot))