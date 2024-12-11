import os
from http import client
import nextcord
from nextcord.ext import commands, application_checks
import json

from main import userData,Server_ID

class slashlevel(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  
  #slash command
  @nextcord.slash_command(description="Shows your level.", guild_ids=Server_ID)
  async def level(self, interaction: nextcord.Interaction, member: nextcord.Member = None): 
    if member == None:
      member = interaction.user
      
    id = interaction.user.id
    
    with open(userData, 'r') as f:
       users = json.load(f)
    
    lvl = users[str(id)]['level']
    
    memberAvatar = member.display_avatar.url
    embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {lvl}!')
    embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
    embed.set_thumbnail(url = memberAvatar)
    await interaction.response.send_message(embed=embed)


  @nextcord.slash_command(name="setlevel", description="Sets level of the user.", guild_ids=Server_ID)
  @application_checks.has_permissions(administrator=True)
  @application_checks.bot_has_permissions(administrator=True)
  async def setlvl(self, interaction: nextcord.Interaction, member: nextcord.Member, level: int):
    if member == None:
      member = interaction.user
    
    id = str(member.id)
      
    with open(userData, 'r') as f:
      users = json.load(f)
    
    if id not in users:
      await interaction.response.send_message(f"{member.mention} has no level data yet.", ephemeral=True)
      return
    
    users[str(id)]['level'] = level
    new_lvl = users[str(id)]['level']

    with open(userData, 'w') as f:
      json.dump(users, f, indent=4)
    
    memberAvatar = member.display_avatar.url
    embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {new_lvl} now!')
    embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
    embed.set_thumbnail(url = memberAvatar)
      
    await interaction.response.send_message(embed=embed)
    
  
  @nextcord.slash_command(name="resetlevel", description="resets level of the user.", guild_ids=Server_ID)
  @application_checks.has_permissions(administrator=True)
  @application_checks.bot_has_permissions(administrator=True)
  async def resetlvl(self, interaction: nextcord.Interaction, member: nextcord.Member):
    if member == None:
      member = interaction.user
    
    id = str(member.id)
      
    with open(userData, 'r') as f:
      users = json.load(f)
    
    if id not in users:
      await interaction.response.send_message(f"{member.mention} has no level data yet.")
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
      
    await interaction.response.send_message(embed=embed)

def setup(bot):  
  bot.add_cog(slashlevel(bot))