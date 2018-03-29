
import discord, asyncio
from utils import embed_gen
from config import *

from discord.ext import commands
import fortniteapi


class Help:
    def __init__(self, bot):
        self.bot = bot
        print(' > Help has been added to Commands')

    @commands.command(pass_context=True, name='help')
    async def help_basic(self, ctx, *, args):

        argslist = args.split(' ')
        if argslist != list():
            command = argslist[0]
            if len(argslist) > 1:
                argument = argslist[1]

                print(command, argument)

        self.person = ctx.message.author

        e = embed_gen.EmbedGenerator()
        embed = e.auto_fill(ctx, '-= Here is my github =-', '', '**Owner** : Genjy#5987', 'color')
        name = ':bee: | General'
        value = value_general
        embed.add_field(name=name, value=value, inline=False)
        name = ':video_game: | Games'
        value = value_games
        embed.add_field(name=name, value=value, inline=False)
        name = ':tools: | Admin'
        value = value_admin
        embed.add_field(name=name, value=value, inline=False)
        await self.person.send(embed=embed)

        await ctx.send(':pencil: | **' + self.person.name + '** check your DM\'s')















def setup(bot):
    bot.add_cog(Help(bot))
