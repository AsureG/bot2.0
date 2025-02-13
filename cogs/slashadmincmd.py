import nextcord
import datetime
import humanfriendly
from nextcord.ext import commands
from nextcord.ext import application_checks
from main import Server_ID

class slashadmincmd(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @nextcord.slash_command(description="Kick a member", guild_ids=Server_ID)
  @application_checks.has_permissions(kick_members=True)
  @application_checks.bot_has_permissions(kick_members=True)
  async def kick(self, ctx, member: nextcord.Member, *, reason: str = "no reason provided"):
    guild = ctx.guild
    await member.kick(reason=reason)
    embed = nextcord.Embed(title="Kicked", description=f"**{member.mention}** has been kicked:foot: \n\n__**Reason**__: {reason}")
    await ctx.send(embed=embed)
    dmembed = nextcord.Embed(title="Kicked", description=f"You have been kicked from **{guild.name}**\n\nReason: **{reason}**")
    await member.send(embed=dmembed)
  

  @nextcord.slash_command(description="Ban a member", guild_ids=Server_ID)
  @application_checks.has_permissions(ban_members=True)
  @application_checks.bot_has_permissions(ban_members=True)
  async def ban(self, ctx, member: nextcord.Member, *, reason: str = "no reason provided"):
    guild = ctx.guild
    await member.ban(reason=reason)
    embed = nextcord.Embed(title="Banned", description=f"**{member.mention}** has been banned:boom: \n\n__**Reason**__: {reason}")
    await ctx.send(embed=embed)
    dmembed = nextcord.Embed(title="Banned", description=f"You have been banned from **{guild.name}**\n\nReason: **{reason}**")
    await member.send(embed=dmembed)
  
  
  @nextcord.slash_command(description="Purge Messages", guild_ids=Server_ID)
  @application_checks.has_permissions(manage_messages=True)
  @application_checks.bot_has_permissions(manage_messages=True)
  async def purge(self, ctx, amount: int):
    purged_message_count = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Number of Messages deleted: `{len(purged_message_count)}`")
  
  
  @nextcord.slash_command(description="Mute the user", guild_ids=Server_ID)
  @application_checks.has_permissions(manage_messages=True)
  @application_checks.bot_has_permissions(manage_messages=True)
  async def mute(self, ctx, member: nextcord.Member, reason=None):
     mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted")
     if not mutedRole:
        await ctx.send("Please create a role named Muted with following things off and on\n\n1)Speak off\n2)Send Message off\n3)Read chat and read chat history off")
     await member.add_roles(mutedRole)
     dmembed = nextcord.Embed(title="Muted", description=f"You have been muted from **{ctx.guild.name}**\n\nReason: **{reason}**")
     await member.send(embed=dmembed)
     embed = nextcord.Embed(title="Muted", description=f"**{member.mention}** has been muted:mute:\n\n__**Reason**__: {reason}")
     await ctx.send(embed=embed)
  
  
  @nextcord.slash_command(description="Mute the user", guild_ids=Server_ID)
  @application_checks.has_permissions(manage_messages=True)
  @application_checks.bot_has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: nextcord.Member):
     mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted")
     await member.remove_roles(mutedRole)
     dmembed = nextcord.Embed(title="Unmuted", description=f"You have been unmuted from **{ctx.guild.name}**:speaker:")
     await member.send(embed=dmembed)
     embed = nextcord.Embed(title="Unmuted", description=f"**{member.mention}** has been unmuted:speaker:")
     await ctx.send(embed=embed)
  
  
  @nextcord.slash_command(description="Unban the user", guild_ids=Server_ID)
  @application_checks.has_permissions(ban_members=True)
  @application_checks.bot_has_permissions(ban_members=True)
  async def unban(self, ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
       await ctx.guild.unban(user)
       embed = nextcord.Embed(title="Unbanned", description=f"**{member}** has been unbanned")
       await ctx.send(embed=embed)


  # @nextcord.slash_command(description="Timeout the user", guild_ids=Server_ID)
  # @application_checks.has_permissions(kick_members=True)
  # @application_checks.bot_has_permissions(kick_members=True)
  # async def timeout(self, ctx, member: nextcord.Member, time, *, reason: str = "no reason provided"):
  #   time = humanfriendly.parse_timespan(time)
  #   await member.edit(timeout = nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
  #   dmembed = nextcord.Embed(title="Timed Out", description=f"You have been timedout from **{ctx.guild.name}**\n\nReason: **{reason}**")
  #   await member.send(embed=dmembed)
  #   embed = nextcord.Embed(title="Timed Out", description=f"**{member.mention}** has been timedout:mute:\n\n__**Reason**__: {reason}")
  #   await ctx.send(embed=embed)

  # @nextcord.slash_command(description="Untimeout the user", guild_ids=Server_ID)
  # @application_checks.has_permissions(kick_members=True)
  # @application_checks.bot_has_permissions(kick_members=True)
  # async def untimeout(self, ctx, member: nextcord.Member):
  #   await member.edit(timeout = None)
  #   dmembed = nextcord.Embed(title="Untimed Out", description=f"You have been untimed out from **{ctx.guild.name}**")
  #   await member.send(embed=dmembed)
  #   embed = nextcord.Embed(title="Untimed Out", description=f"**{member.mention}** has been untimed out:mute:")
  #   await ctx.send(embed=embed)


  #Errors
  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed()
      embed.set_author(name='Invalid Format')
      embed.add_field(name='.Kick @{user} {reason}', value="Helps admins to kick user", inline=False)
      await ctx.send(embed=embed)

  
  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed()
      embed.set_author(name='Invalid Format')
      embed.add_field(name='.ban @{user} {reason}', value="Helps admins to ban user", inline=False)
      await ctx.send(embed=embed)


  @purge.error
  async def purge_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed()
      embed.set_author(name='Invalid Format')
      embed.add_field(name='.purge {amount}', value="Helps admins to purge messages", inline=False)
      await ctx.send(embed=embed)


  @mute.error
  async def mute_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed()
      embed.set_author(name='Invalid Format')
      embed.add_field(name='.Mute @{user} {reason}', value="Helps admins to mute user", inline=False)
      await ctx.send(embed=embed)

  
  @unmute.error
  async def unmute_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed()
      embed.set_author(name='Invalid Format')
      embed.add_field(name='.Unmute @{user}', value="Helps admins to unmute user", inline=False)
      await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(slashadmincmd(bot))