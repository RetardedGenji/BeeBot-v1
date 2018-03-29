
import discord, asyncio
from utils import embed_gen

from discord.ext import commands


class Clear:
    def __init__(self, bot):
        self.bot = bot
        print(' > Clear has been added to Commands')

    @commands.command(pass_context=True, name='clear')
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge_tchat(self, ctx, number:int):

        try:
            deleted = await ctx.channel.purge(limit=number)
        except Exception as e:
            await ctx.send(e)



def setup(bot):
    bot.add_cog(Clear(bot))
