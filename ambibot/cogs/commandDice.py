from discord.ext import commands
import random

class commandDice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    ##   dice
    @commands.command(aliases=['DX','rd','roll','dice'])
    async def dx(self, ctx,dice):
        await ctx.send(random.randint(1,int(dice)))

    @commands.command(aliases=['rolld20','rd20','r1d20'])
    async def d20(self, ctx):
        await ctx.send(random.randint(1, 20))

    @commands.command(aliases=['rollf20','rf20','r1f20'])
    async def f20(self, ctx):
        await ctx.send(random.randint(1, 20))

    @commands.command(aliases=['rolld4','rd4','r1d4'])
    async def d4(self, ctx):
        await ctx.send(random.randint(1, 4))
        
    @commands.command(aliases=['rolld6','rd6','r1d6'])
    async def d6(self, ctx):
        await ctx.send(random.randint(1, 6))

    @commands.command(aliases=['rolld8','rd8','r1d8'])
    async def d8(self, ctx):
        await ctx.send(random.randint(1, 8))
        
    @commands.command(aliases=['rolld10','rd10','r1d10'])
    async def d10(self, ctx):
        await ctx.send(random.randint(1, 10))
        
    @commands.command(aliases=['rolld12','rd12','r1d12'])
    async def d12(self, ctx):
        await ctx.send(random.randint(1, 12))

    @commands.command(aliases=['rolld100','rd100','r1d100'])
    async def d100(self, ctx):
        await ctx.send(random.randint(1, 100))

async def setup(bot):
    await bot.add_cog(commandDice(bot))

