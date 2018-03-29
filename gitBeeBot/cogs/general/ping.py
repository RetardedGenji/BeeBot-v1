
import discord, asyncio
from utils import embed_gen

from discord.ext import commands


class Ping:
    def __init__(self, bot):
        self.bot = bot
        print(' > Ping has been added to Commands')

    @commands.command(pass_context=True, name='ping')
    @commands.guild_only()
    async def ping(self, ctx):

        embed = embed_gen.EmbedGenerator.auto_fill(self, ctx, '', ':pushpin: Pinging...', '', 'color_e')
        pre = await ctx.send(embed=embed)

        diff = pre.created_at - ctx.message.created_at

        text = ':inbox_tray: **Pong !** In ' + str(1000*diff.total_seconds()) + ' *ms*'
        embed = embed_gen.EmbedGenerator.auto_fill(self, ctx, '', '', text, 'color')
        await pre.edit(embed=embed)


def setup(bot):
    bot.add_cog(Ping(bot))
