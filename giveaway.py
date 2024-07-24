from http import client
import nextcord
from nextcord.ext import commands
import asyncio
import random
import os

class giveaway(commands.Cog):
  def __init__(self, bot):
      self.bot = client

  
  @commands.command(aliases=['gstart'])
  async def gcreate(ctx, time=None, *, prize=None):
    if time == None:
      return await ctx.send('```.Gcreate\n\n.gcreate {time} {prize}```')
    elif prize == None:
      return await ctx.send('```.Gcreate\n\n.gcreate {time} {prize}```')
    embed = nextcord.Embed(title ='New Giveaway!', description = f'{ctx.author.mention} is givingaway **{prize}**!')
    time_convert = {"s":1, "m":60, "h":3600, "d": 86400}
    gawtime = int(time[0]) * time_convert[time[-1]]
    embed.set_footer(text=f'Giveaway ends in {time}!')
    gaw_msg = await ctx.send(embed=embed)
    await gaw_msg.add_reaction("🎉")
    await asyncio.sleep(gawtime)
    new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)
    users = await new_gaw_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)
    await ctx.send(f"Congrats {winner.mention} has won the giveaway for **{prize}**🎉!")
  
  @gcreate.error
  async def gcreate_error(self, ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("```.Gcreate\n\n.gcreate {time} {prize}```")


def setup(bot):
  bot.add_cog(giveaway(bot))