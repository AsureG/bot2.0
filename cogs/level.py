from http import client
import nextcord
from nextcord.ext import commands
import json

from Bot2.main import add_experience, level_up, update_data

class level(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

   
  @commands.Cog.listener()
  async def on_member_join(self, member):
    with open('users.json', 'r') as f:
        users = json.load(f)
    await update_data(users, member)
    with open('users.json', 'w') as f:
         json.dump(users, f, indent=4)
  
  
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users=json.load(f)
        await update_data(users, message.author)
        await add_experience(users, message.author, 2)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
    await client.process_commands(message)
  
  
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


  @commands.command(aliases=['level'])
  async def lvl(self, ctx, member: nextcord.Member = None): 
    if member == None:
      member = ctx.author
      id = ctx.message.author.id
      with open('users.json', 'r') as f:
         users = json.load(f)
      lvl = users[str(id)]['level']
      memberAvatar = member.avatar.url
      embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {lvl}!')
      embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
      embed.set_thumbnail(url = memberAvatar)
      await ctx.send(embed=embed)
    else:
      id = member.id
      with open('users.json', 'r') as f:
          users = json.load(f)
      lvl = users[str(id)]['level']
      memberAvatar = member.avatar.url
      embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {lvl}!')
      embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
      embed.set_thumbnail(url = memberAvatar)
      await ctx.send(embed=embed)


  @commands.command(aliases=['lvlset'])
  async def setlvl(self, ctx, member: nextcord.Member = None):
    if member == None:
      member = ctx.author
      id = ctx.message.author.id
      with open('users.json', 'r') as f:
         users = json.load(f)
      lvl = users[str(id)]['level']
      lvl + 10
      memberAvatar = member.avatar.url
      embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {lvl} now!')
      embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
      embed.set_thumbnail(url = memberAvatar)
      await ctx.send(embed=embed)
    else:
      id = member.id
      with open('users.json', 'r') as f:
        users = json.load(f)
      lvl = users[str(id)]['level']
      lvl + 10
      memberAvatar = member.avatar.url
      embed = nextcord.Embed(title="Levels", description=f'{member.mention} is at level {lvl} now!')
      embed.set_author(name=f"{member.name}", icon_url=memberAvatar)
      embed.set_thumbnail(url = memberAvatar)
      await ctx.send(embed=embed)


def setup(bot):  
  bot.add_cog(level(bot))