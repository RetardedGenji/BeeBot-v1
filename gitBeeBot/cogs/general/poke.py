
import discord, asyncio

from discord.ext import commands


class WakeUp:
    def __init__(self, bot):
        self.bot = bot
        print(' > Spam has been added to Commands')

    @commands.command(pass_context=True, name='poke')
    @commands.guild_only()
    async def poking(self, ctx, *, args):

        spliting = args.split(' ')
        self.person = self.bot.get_user(int(spliting[0]))

        if self.person == None:
            await ctx.send(' Can\'t find this guy, sorry')
            return

        await self.person.send('**Hey, `wake up`**')

        embed = discord.Embed(title=str(self.person) + ' has been poked', colour=0x28ff64)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(WakeUp(bot))
