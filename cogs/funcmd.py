import nextcord
from nextcord.ext import commands, application_checks
import random
from main import Server_ID

class funcmd(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @nextcord.slash_command(description="Sends back Hello", guild_ids=Server_ID)
  async def hello(self, interaction: nextcord.Interaction, member : nextcord.Member = None):
      if member == None:
       member = interaction.user
      await interaction.response.send_message(f"Hello there {member.mention} :wave:")

  
  @nextcord.slash_command(description="Repeats the message", guild_ids=Server_ID)
  async def say(self, interaction: nextcord.Interaction, text: str):
    await interaction.response.defer()
    await interaction.channel.send(f"{text}")
  
  
  @nextcord.slash_command(description="Check out your avatar", guild_ids=Server_ID)
  async def avatar(self, interaction: nextcord.Interaction, member : nextcord.Member = None):
    if member is None:
      member = interaction.user
    memberAvatar = member.display_avatar.url
    avEmbed = nextcord.Embed(title = f"{member.name}'s Avatar")
    avEmbed.set_image(url = memberAvatar)
    await interaction.response.send_message(embed = avEmbed)
  
  
  @nextcord.slash_command(description="Change nicknames!", guild_ids=Server_ID)
  @application_checks.has_permissions(change_nickname=True)
  async def nick(self, interaction: nextcord.Interaction, member: nextcord.Member, nick):
      await member.edit(nick=nick)
      embed = nextcord.Embed(description=f"Nickname was changed for {member.mention}")
      await interaction.response.send_message(embed=embed)
  
  
  @nextcord.slash_command(name="8ball", description="Ask the question and let the ball decide!", guild_ids=Server_ID)
  async def _8ball(self, interaction: nextcord.Interaction, question):
      responses = ['As I see it, yes.',
                   'Yes.',
                   'Positive',
                   'From my point of view, yes',
                   'Convinced.',
                   'Most Likley.',
                   'Chances High',
                   'No.',
                   'Negative.',
                   'Not Convinced.',
                   'Perhaps.',
                   'Not Sure',
                   'Mayby',
                   'I cannot predict now.',
                   'Im to lazy to predict.',
                   'I am tired. *proceeds with sleeping*']
      response = random.choice(responses)
      embed=nextcord.Embed(title="The Magic 8 Ball says!")
      embed.add_field(name='Question: ', value=f'{question}', inline=True)
      embed.add_field(name='Answer: ', value=f'{response}', inline=False)
      await interaction.response.send_message(embed=embed)

  @say.error
  async def say_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("```.say\n\n.say {message}```")

  
  @_8ball.error
  async def eightball_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("```.8ball\n\n.8ball {question}```")
  
      
def setup(bot):
  bot.add_cog(funcmd(bot))