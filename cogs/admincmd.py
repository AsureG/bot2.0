import nextcord
import discord
import datetime
import humanfriendly
from nextcord.ext import commands
from discord.ext import commands

class admincmd(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  @commands.bot_has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason: str = "no reason provided"):
    guild = ctx.guild
    await member.kick(reason=reason)
    embed = discord.Embed(title="Kicked", description=f"**{member.mention}** has been kicked:foot: \n\n__**Reason**__: {reason}")
    await ctx.send(embed=embed)
    dmembed = discord.Embed(title="Kicked", description=f"You have been kicked from **{guild.name}**\n\nReason: **{reason}**")
    await member.send(embed=dmembed)
  

  @commands.command()
  @commands.has_permissions(ban_members=True)
  @commands.bot_has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason: str = "no reason provided"):
    guild = ctx.guild
    await member.ban(reason=reason)
    embed = discord.Embed(title="Banned", description=f"**{member.mention}** has been banned:boom: \n\n__**Reason**__: {reason}")
    await ctx.send(embed=embed)
    dmembed = discord.Embed(title="Banned", description=f"You have been banned from **{guild.name}**\n\nReason: **{reason}**")
    await member.send(embed=dmembed)
  
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  @commands.bot_has_permissions(manage_messages=True)
  async def purge(self, ctx, amount: int):
    purged_message_count = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Number of Messages deleted = `{len(purged_message_count)}`")
  
  
  @commands.command(description="Mutes a specified user.")
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: discord.Member, reason=None):
     mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
     if not mutedRole:
        await ctx.send("Please create a role named Muted with following things off and on\n\n1)Speak off\n2)Send Message off\n3)Read chat and read chat history off")
     await member.add_roles(mutedRole)
     dmembed = discord.Embed(title="Muted", description=f"You have been muted from **{ctx.guild.name}**\n\nReason: **{reason}**")
     await member.send(embed=dmembed)
     embed = discord.Embed(title="Muted", description=f"**{member.mention}** has been muted:mute:\n\n__**Reason**__: {reason}")
     await ctx.send(embed=embed)
  
  
  @commands.command(description="Unmutes a specified user.")
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: discord.Member):
     mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
     await member.remove_roles(mutedRole)
     dmembed = discord.Embed(title="Unmuted", description=f"You have been unmuted from **{ctx.guild.name}**:speaker:")
     await member.send(embed=dmembed)
     embed = discord.Embed(title="Unmuted", description=f"**{member.mention}** has been unmuted:speaker:")
     await ctx.send(embed=embed)
  
  
  @commands.command()
  async def unban(self, ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
       await ctx.guild.unban(user)
       embed = discord.Embed(title="Unbanned", description=f"**{member}** has been unbanned")
       await ctx.send(embed=embed)


  @commands.command()
  async def timeout(ctx, member: nextcord.Member, time, *, reason: str = "no reason provided"):
    time = humanfriendly.parse_timespan(time)
    await member.edit(timeout = nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
    dmembed = nextcord.Embed(title="Timed Out", description=f"You have been timedout from **{ctx.guild.name}**\n\nReason: **{reason}**")
    await member.send(embed=dmembed)
    embed = nextcord.Embed(title="Timed Out", description=f"**{member.mention}** has been timedout:mute:\n\n__**Reason**__: {reason}")
    await ctx.send(embed=embed)

  @commands.command()
  async def untimeout(ctx, member: nextcord.Member):
    await member.edit(timeout = None)
    dmembed = nextcord.Embed(title="Untimed Out", description=f"You have been untimed out from **{ctx.guild.name}**")
    await member.send(embed=dmembed)
    embed = nextcord.Embed(title="Untimed Out", description=f"**{member.mention}** has been untimed out:mute:")
    await ctx.send(embed=embed)


  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("```.Kick\n\n.Kick @{user} {reason}```")

  
  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("```.Ban\n\n.Ban @{user} {reason}```")


  @purge.error
  async def purge_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("```Please enter the amount to purge!```")


  @mute.error
  async def mute_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("```.mute\n\n.Mute @{user} {reason}```")

  
  @unmute.error
  async def unmute_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("```.unmute\n\n.Unmute @{user} {reason}```")


def setup(bot):
  bot.add_cog(admincmd(bot))