
import discord, asyncio
from config import *

from discord.ext import commands

class Engine:
    def init():
        loop = asyncio.get_event_loop()
        client = commands.Bot(command_prefix=PREFIX, loop=loop)
        return client

bot = Engine.init()


class EventHandler:

    @bot.event
    async def on_ready():
        print('     > Bot Started as: {0} , {0.id}'.format(bot.user))

        await bot.change_presence(activity=discord.Game(name=PREFIX+'help | '))


    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if not message.content.startswith(PREFIX):
            return

        try:
            await bot.process_commands(message)
            #add +1 to number of commands.
        except Exception as e:
            await ctx.send(e)


def setup(bot):
    bot.remove_command('help')
    for extension in initial_extension:
        bot.load_extension(extension)
        """except Exception as e:
            print(' Couldnt load module : ', extension, '\n   ', e)"""


if __name__ == '__main__':
    EventHandler()
    setup(bot)
    bot.run(TOKEN)
