
import discord, asyncio
from utils import embed_gen
from config import TRACKER_KEY

from discord.ext import commands
import fortniteapi


class FortniteTracker:
    def __init__(self, bot):
        self.bot = bot
        self.key = TRACKER_KEY
        self.authorized_mode = ['solo', 'duo', 'squad']
        self.authorized_platform = ['pc', 'xbl', 'psn']
        self.desc = [
            "**Wins** - ",
            "**Top 3** - ",
            "**Top 5** - ",
            "**Top 6** - ",
            "**Top 10** - ",
            "**Top 12** - ",
            "**Top 25** - ",
            "**Kills** - ",
            "**Ratio K/D** - ",
            "**Kills per match** - ",
            "**Win Chance** - ",
            "**Total time played** - "
        ]
        print(' > FortniteTracker has been added to Commands')

    @commands.command(pass_context=True, name='fortnite')
    async def fortnite_tracker(self, ctx, *, args):

        #^^fortnite <mode> <epic games username> <platform>
        #<mode> includes solo, duo and squad
        #<platform> includes pc, xbl (for xbox) and psn (for playstation)
        self.args = args.split(' ')
        self.mode = self.args[0]
        self.user = self.args[1]
        self.platform = self.args[2]

        if self.mode not in self.authorized_mode:
            await ctx.send('You need to enter a correct mode either "solo", "duo" or "squad"')
            return
        if self.platform not in self.authorized_platform:
            await ctx.send('You need to enter a correct platform either "pc", "xbl" (xbox) or "psn" (playstation)')
            return

        #try:
        self.tracker = fortniteapi.tracker(self.key, user=self.user, platform=self.platform)
        self.tracker.get_stats()
        """except Exception as e:
            await ctx.send(e)
            return"""

        if self.mode == 'solo':
            result = self.track_solo()
        if self.mode == 'duo':
            result = self.track_duo()
        if self.mode == 'squad':
            result = self.track_squad()
        result.append(self.tracker.TOTAL_TIME_PLAYED)

        author = '-= FORTNITE STATS =-'
        title = ' > Stats from '+self.user+' on '+self.platform+' for the '+self.mode+' mode\n'
        description = '\n '.join(self.desc) + '\n'.join(result)
        embed = embed_gen.EmbedGenerator.auto_fill(self, ctx, author, title, description, 'color')
        await ctx.send(embed=embed)


    def track_solo(self):
        result = [
            self.tracker.ALL_SOLO_WINS,
            self.tracker.ALL_SOLO_TOP3,
            self.tracker.ALL_SOLO_TOP5,
            self.tracker.ALL_SOLO_TOP6,
            self.tracker.ALL_SOLO_TOP10,
            self.tracker.ALL_SOLO_TOP12,
            self.tracker.ALL_SOLO_TOP25,
            self.tracker.ALL_SOLO_KILLS,
            self.tracker.ALL_SOLO_KD,
            self.tracker.ALL_SOLO_KPG,
            self.tracker.ALL_SOLO_WIN_CHANCE
        ]
        return result

    def track_duo(self):
        result = [
            self.tracker.ALL_DUO_WINS,
            self.tracker.ALL_SOLO_TOP3,
            self.tracker.ALL_SOLO_TOP5,
            self.tracker.ALL_SOLO_TOP6,
            self.tracker.ALL_SOLO_TOP10,
            self.tracker.ALL_DUO_TOP12,
            self.tracker.ALL_DUO_TOP15,
            self.tracker.ALL_DUO_KILLS,
            self.tracker.ALL_DUO_KD,
            self.tracker.ALL_DUO_KPG,
            self.tracker.ALL_DUO_WIN_CHANCE
        ]
        return result

    def track_squad(self):
        result = [
            self.tracker.ALL_SQUAD_WINS,
            self.tracker.ALL_SOLO_TOP3,
            self.tracker.ALL_SOLO_TOP5,
            self.tracker.ALL_SOLO_TOP6,
            self.tracker.ALL_SQUAD_TOP10,
            self.tracker.ALL_SQUAD_TOP12,
            self.tracker.ALL_SOLO_TOP25,
            self.tracker.ALL_SQUAD_KILLS,
            self.tracker.ALL_SQUAD_KD,
            self.tracker.ALL_SQUAD_KPG,
            self.tracker.ALL_SQUAD_WIN_CHANCE
        ]
        return result


def setup(bot):
    bot.add_cog(FortniteTracker(bot))
