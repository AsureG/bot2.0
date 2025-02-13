import os
from http import client
import nextcord
from nextcord.ext import commands, application_checks
import json

from main import userData,Server_ID

class level(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
    
  #prefix command
  @commands.command()
  async def level(self, ctx, member: nextcord.Member = None): 
    if member == None:
      member = ctx.author
      
    id = member.id
    
    with open(userData, 'r') as f:
       users = json.load(f)
    
    lvl = users[str(id)]['level']
    
    memberAvatar = member.display_avatar.url
    embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {lvl}!')
    embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
    embed.set_thumbnail(url = memberAvatar)
    await ctx.send(embed=embed)

  
  @commands.command()
  @commands.has_permissions(administrator=True)
  @commands.bot_has_permissions(administrator=True)
  async def setlvl(self, ctx, member: nextcord.Member, level: int):
    if member == None:
      member = ctx.user
    
    id = str(member.id)
      
    with open(userData, 'r') as f:
      users = json.load(f)
    
    if id not in users:
      await ctx.send(f"{member.mention} has no level data yet.", ephemeral=True)
      return
    
    users[str(id)]['level'] = level
    new_lvl = users[str(id)]['level']

    with open(userData, 'w') as f:
      json.dump(users, f, indent=4)
    
    memberAvatar = member.display_avatar.url
    embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {new_lvl} now!')
    embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
    embed.set_thumbnail(url = memberAvatar)
      
    await ctx.send(embed=embed)
    
    
  @commands.command()
  @commands.has_permissions(administrator=True)
  @commands.bot_has_permissions(administrator=True)
  async def resetlvl(self, ctx, member: nextcord.Member):
    if member == None:
      member = ctx.user
    
    id = str(member.id)
      
    with open(userData, 'r') as f:
      users = json.load(f)
    
    if id not in users:
      await ctx.send(f"{member.mention} has no level data yet.")
      return
    
    users[str(id)]['experience'] = 0
    users[str(id)]['level'] = 0
    new_lvl = users[str(id)]['level']

    with open(userData, 'w') as f:
      json.dump(users, f, indent=4)
    
    memberAvatar = member.display_avatar.url
    embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {new_lvl} now!')
    embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
    embed.set_thumbnail(url = memberAvatar)
      
    await ctx.send(embed=embed)
    
  #Errors

  @resetlvl.error
  async def unmute_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed()
      embed.set_author(name='Invalid Format')
      embed.add_field(name='.resetlvl @{user}', value="Helps admins to reset someone's levels", inline=False)
      await ctx.send(embed=embed)
      
  @setlvl.error
  async def unmute_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed()
      embed.set_author(name='Invalid Format')
      embed.add_field(name='.setlvl @{user} {amount}', value="Helps admins to set someone's levels", inline=False)
      await ctx.send(embed=embed)

def setup(bot):  
  bot.add_cog(level(bot))