import discord
from config import *
import time
from time import strftime

class EmbedGenerator:
    def __init__(self):
        print(' > EmbedGenerator has been introduced')

    def auto_fill(self, ctx, author, title, desc, color):
        if color == 'color':
            color = COLOR
        elif color == 'color_e':
            color = COLOR_E
        embed = discord.Embed(title=title, description=desc, color=color)

        if author != '':
            embed.set_author(name=author, url='https://github.com/RetardedGenji/')

        footer_text = 'Requested by ' + ctx.message.author.name + ' | ' + strftime("%H:%M:%S %d/%m/%Y", time.localtime())
        embed.set_footer(text=footer_text, icon_url = ctx.message.author.avatar_url)

        return embed

    def add_field(self, embed, name, value):
        embed.add_field(name=name, value=value)
        return embed
