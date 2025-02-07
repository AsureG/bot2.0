import nextcord
from nextcord.ext import commands, application_checks
import random
from main import Server_ID

class funcmd(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  async def hello(self, ctx, member : nextcord.Member = None):
      if member == None:
       member = ctx.author
      await ctx.send(f"Hello there {member.mention} :wave:")

  
  @commands.command()
  async def say(self, ctx, text: str):
    await ctx.send(f"{text}")
  
  
  @commands.command()
  async def avatar(self, ctx, member : nextcord.Member = None):
    if member is None:
      member = ctx.author
    memberAvatar = member.display_avatar.url
    avEmbed = nextcord.Embed(title = f"{member.name}'s Avatar")
    avEmbed.set_image(url = memberAvatar)
    await ctx.send(embed = avEmbed)
  
  
  @commands.command()
  @commands.has_permissions(change_nickname=True)
  async def nick(self, ctx, member: nextcord.Member, nick):
      await member.edit(nick=nick)
      embed = nextcord.Embed(description=f"Nickname was changed for {member.mention}")
      await ctx.send(embed=embed)
  
  
  @commands.command()
  async def _8ball(self, ctx, question):
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
      await ctx.send(embed=embed)

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