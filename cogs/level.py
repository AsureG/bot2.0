import os
from http import client
import nextcord
from nextcord.ext import commands
from nextcord import integrations
import json


from main import add_experience, level_up, update_data, userData

class level(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

   
  @commands.Cog.listener()
  async def on_member_join(self, member):
    with open(userData, 'r') as f:
        users = json.load(f)
    await update_data(users, member)
    with open(userData, 'w') as f:
         json.dump(users, f, indent=4)
  
  
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot == False:
        with open(userData, 'r') as f:
            users=json.load(f)
        await update_data(users, message.author)
        await add_experience(users, message.author, 2)
        await level_up(users, message.author, message)
        with open(userData, 'w') as f:
            json.dump(users, f, indent=4)
    await self.bot.process_commands(message)
  
  
  async def update_data(self, users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1
  
  
  async def add_experience(self, users, user, exp):
    users[f'{user.id}']['experience'] += exp
  
  
  async def level_up(self, users, user, message):
    with open('levels.json', 'r') as g:
      levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        memberAvatar = user.avatar.url
        embed = nextcord.Embed(title="Level up", description=f'{user.mention} has leveled up to level {lvl_end}'.format(user.mention, lvl_end))
        embed.set_thumbnail(url = memberAvatar)
        await message.channel.send(embed=embed)
        users[f'{user.id}']['level'] = lvl_end


  @nextcord.slash_command(description="Shows your level.", guild_ids=[650256982200156172])
  async def level(self, interaction: nextcord.Interaction, member: nextcord.Member): 
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


  @nextcord.slash_command(description="Sets level of the user.", guild_ids=[650256982200156172])
  async def setlvl(self, interaction: nextcord.Interaction, member: nextcord.Member, Level: int = 1):
    if member == None:
      member = interaction.user
    
    id = str(member.id)
      
    with open(userData, 'r') as f:
      users = json.load(f)
    
    if id not in users:
      await interaction.response.send_message(f"{member.mention} has no level data yet.", ephemeral=True)
      return
    
    users[str(id)]['level'] = Level
    new_lvl = users[str(id)]['level']

    with open(userData, 'w') as f:
      json.dump(users, f, indent=4)
    
    memberAvatar = member.display_avatar.url
    embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {new_lvl} now!')
    embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
    embed.set_thumbnail(url = memberAvatar)
      
    await interaction.response.send_message(embed=embed)
    
  
  @nextcord.slash_command(description="Sets level of the user.", guild_ids=[650256982200156172])
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
  bot.add_cog(level(bot))