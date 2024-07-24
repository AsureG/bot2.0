from http import client
import nextcord
from nextcord.ext import commands
import wavelink
from wavelink.ext import spotify

class music(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(aliases=['j'])
  async def join(self, ctx):
      voicetrue = ctx.author.voice
      if voicetrue is None:
        return await ctx.send('`You are not in a voice channel!`')
      await ctx.author.voice.channel.connect()
      embed = nextcord.Embed(title="Joined", description="Asurey has joined the vc!")
      await ctx.send(embed=embed)

  
  @commands.command(aliases=['dc', 'disconnect'])
  async def leave(self, ctx):
      voicetrue = ctx.author.voice
      mevoicetrue = ctx.guild.me.voice
      if voicetrue is None:
        return await ctx.send('`You are not in a voice channel!`')
      if mevoicetrue is None:
        return await ctx.send('`I am not in a voice channel!`')
      await ctx.voice_client.disconnect()
      embed = nextcord.Embed(title="Left", description="Asurey has left the vc!")
      await ctx.send(embed=embed)

  
  @commands.command()
  async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
      if not ctx.voice_client:
          vc: wavelink.Player = await       ctx.author.voice.channel.connect(cls=wavelink.Player)
      elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.send("`Please join a voice channel first!`")
      else:
        vc: wavelink.Player = ctx.voice_client

      await vc.play(search)
      embed = nextcord.Embed(title="Now Playing!", description=f"{search.title}")
      await ctx.send(embed=embed)


  @commands.command()
  async def pause(ctx: commands.Context):
      if not ctx.voice_client:
        return await ctx.send("`Nothing is playing right now!`")
      elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.send("`Please join a voice channel first!`")
      else:
        vc: wavelink.Player = ctx.voice_client

      await vc.pause()
      embed = nextcord.Embed(title="Paused", description="Paused the playing song!")
      await ctx.send(embed=embed)


  @commands.command()
  async def resume(ctx: commands.Context):
      if not ctx.voice_client:
        return await ctx.send("`Nothing is playing right now!`")
      elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.send("`Please join a voice channel first!`")
      else:
        vc: wavelink.Player = ctx.voice_client

      await vc.resume()
      embed = nextcord.Embed(title="Resumed", description="Resumed the playing song!")
      await ctx.send(embed=embed)


  @commands.command()
  async def skip(ctx: commands.Context):
    if not ctx.voice_client:
      return await ctx.send("`Nothing is playing right now!`")
    elif not getattr(ctx.author.voice, "channel", None):
      return await ctx.send("`Please join a voice channel first!`")
    else:
      vc: wavelink.Player = ctx.voice_client

    await vc.stop()
    embed = nextcord.Embed(title="Skipped", description="Skipped the playing song!")
    await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(music(bot))