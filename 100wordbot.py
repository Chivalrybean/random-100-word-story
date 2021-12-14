import discord
import requests as r
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

from tokens import token, guild_ids

client = commands.Bot(command_prefix="/")
slash = SlashCommand(client, sync_commands=True)
headers = {'user-agent': "100 Word Stories Bot by Chivalrybean"}

@client.event
async def on_ready():
    print('The bot has logged in as {0.user}'.format(client))

@slash.slash(name="100word", description="Get a random 100 word story by Laurence Simon")
async def _100word(ctx: SlashContext):
   await ctx.send(r.get("https://oneadayuntilthedayidie.com/?page_id=26987", headers=headers).content.decode("utf-8"))

client.run(token)
