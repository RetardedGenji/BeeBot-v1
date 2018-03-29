import discord, asyncio
from utils import embed_gen
from config import initial_name, initial_commands, initial_extension

from discord.ext import commands


class Reload:
    def __init__(self, bot):
        self.bot = bot
        print(' > Reload has been added to Commands')

    @commands.command(pass_context=True, name='reload')
    @commands.is_owner()
    async def reload_commands(self, ctx, *, args:str = None):

        if args == None:
            await ctx.send(':x: *You must pass a module name to reload or <all>*')
            await ctx.send('These are available : ' + ', '.join(initial_name))
            return

        self.import_success = []
        self.import_fail = []

        if args == 'all':
            args = initial_name
        else:
            args = args.split(' ')

        for name in args:
            if name in initial_name:
                try:
                    self.bot.unload_extension(initial_commands[name][0])
                    self.bot.load_extension(initial_commands[name][0])
                    self.import_success.append(name)
                except Exception as e:
                    self.import_fail.append(name)
            else:
                self.import_fail.append(name)

        if len(self.import_success) == 0:
            self.pre = ':negative_squared_cross_mark: Didn\'t reload any commands'
        elif len(self.import_success) != 0:
            self.pre = ':dizzy: Reloaded : ' + ', '.join(self.import_success)
            if len(self.import_fail) == 0:
                self.aft = ''
            elif len(self.import_fail) != 0:
                self.aft = ':negative_squared_cross_mark: **But not : ' + ', '.join(self.import_fail) + '**'

        embed = embed_gen.EmbedGenerator.auto_fill(self, ctx, '', self.pre, self.aft, 'color')
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Reload(bot))
