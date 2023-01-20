import discord
from discord.ext import commands

class commandMisc(commands.Cog):
    def __innit__(self, bot):
        self.bot = bot

    # converts meters to feet
    @commands.command(aliases=["meterstofeet","map"])
    async def mtf(self, ctx,meter):
        foot = int(meter)*3.281
        round(foot,2)
        await ctx.send(f"{meter} Metros son: {'%.2f'%foot} Pies")

    # converts feet to meters
    @commands.command(aliases=["feettometer","pam"])
    async def ftm(self, ctx,feet):
        meter = int(feet)/3.281
        round(meter,2)
        await ctx.send(f"{feet} Pies son: {'%.2f'%meter} Metros")
    
    #get user ID or say hi to user
    @commands.command()
    async def hi(self, ctx):
        #print(ctx.author.id)
        usrname = ctx.author.name
        await ctx.send(f"Hello there {usrname}")

    ##   flavour

    @commands.command(aliases=['<3'])
    async def luv(self, ctx):
        await ctx.send('<3')

    ## havel flip
    @commands.command(aliases=['hf'])
    async def havelflip(self, ctx):
        await ctx.send(file=discord.File("images/havelflip.gif"))

    ##      an example
    @commands.command(aliases=['smth'])
    async def xd(self, ctx):
        await ctx.send(':cyclone:')

async def setup(bot):
    await bot.add_cog(commandMisc(bot))