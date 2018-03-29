import discord, asyncio
from utils import embed_gen
from discord.ext import commands


class Shutdown:
    def __init__(self, bot):
        self.bot = bot
        print(' > Shutdown has been added to Commands')

    @commands.command(pass_context=True, name='sd')
    @commands.is_owner()
    async def shutdown_without_params(self, ctx):
        
        embed = embed_gen.EmbedGenerator.auto_fill(self, ctx, '', ':crescent_moon: I\'m Out !', '', 'color')
        await ctx.send(embed=embed)
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Shutdown(bot))
