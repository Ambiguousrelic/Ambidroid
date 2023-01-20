import discord
from discord.ext import commands



##TODO: Rework help command

class commandHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['hlp'])
    async def help(self, ctx):
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


async def setup(bot):
    await bot.add_cog(commandHelp(bot))