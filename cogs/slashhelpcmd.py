import nextcord
from nextcord.ext import commands
from main import Server_ID

class slashhelpcmd(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @nextcord.slash_command(description="Lists commands", guild_ids=Server_ID)
  async def help(self, ctx):
    embed = nextcord.Embed()
    embed.set_author(name='Fun cmds')
    embed.add_field(name='.Ping', value='Returns with a Pong!', inline=False)
    embed.add_field(name='.Hello', value='Returns with a Hello there!', inline=False)
    embed.add_field(name='.say {message}', value='Returns with the message', inline=False)
    embed.add_field(name='.Purge {number}', value='purges messages', inline=False)
    embed.add_field(name='.Avatar @{user}', value="enlarge someone's avatar", inline=False)
    embed.add_field(name='.lvl @{user}', value="shows someone's levels (Currently)", inline=False)
    embed.add_field(name='.8ball {qustion}', value="8ball will reply to ur question", inline=False)
    await ctx.send(embed=embed)
    
    
  @nextcord.slash_command(description="Lists commands", guild_ids=Server_ID)
  async def adminhelp(self, ctx):
    embed = nextcord.Embed()
    embed.set_author(name='Admin cmds')
    embed.add_field(name='.Gcreate {time} {prize}', value='Helps admins to create giveaways', inline=False)
    embed.add_field(name='.Ban @{user} {reason}', value='Helps admins to ban someone bad', inline=False)
    embed.add_field(name='.Unban @{user}', value='Helps admins to unban someone', inline=False)
    embed.add_field(name='.kick @{user} {reason}', value='Helps admins to kick someone bad', inline=False)
    embed.add_field(name='.setlvl @{user} {amount}', value="Helps admins set someone's level", inline=False)
    embed.add_field(name='.resetlvl @{user}', value="Helps admins reset someone's levels to 0", inline=False)
    embed.add_field(name='.nick @{user} {nickname}', value="Helps admins set someone's nickname", inline=False)
    embed.add_field(name='.Timeout @{user} {time} {reason}', value='Helps admins to timeout someone', inline=False)
    embed.add_field(name='.Untimeout @{user}', value='Helps admins to untimeout someone', inline=False)
    await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(slashhelpcmd(bot))