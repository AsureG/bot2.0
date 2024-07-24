import nextcord
from nextcord.ext import commands

class helpcmd(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  async def help(self, ctx):
    embed = nextcord.Embed()
  
    embed.set_author(name='Fun cmds')
    embed.add_field(name='.Ping', value='Returns with a Pong!', inline=False)
    embed.add_field(name='.Hello', value='Returns with a Hello there!', inline=False)
    embed.add_field(name='.Purge {number}', value='purges messages', inline=False)
    embed.add_field(name='.Avatar @{user}', value="enlarge someone's avatar", inline=False)
    embed.add_field(name='.Enlarge {emoji}', value="enlarge a emoji", inline=False)
    embed.add_field(name='.lvl @{user}', value="shows someone's levels", inline=False)
    embed.add_field(name='\n\nAdmin cmds\n\n.Gcreate {time} {prize}', value='Helps admins to create giveaways', inline=False)
    embed.add_field(name='.Ban @{user} {reason}', value='Helps admins to ban someone bad', inline=False)
    embed.add_field(name='.Unban @{user}', value='Helps admins to unban someone', inline=False)
    embed.add_field(name='.kick @{user} {reason}', value='Helps admins to kick someone bad', inline=False)
    embed.add_field(name='.Timeout @{user} {time} {reason}', value='Helps admins to timeout someone', inline=False)
    embed.add_field(name='.Untimeout @{user}', value='Helps admins to untimeout someone', inline=False)
  
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(helpcmd(bot))