# Imports
import os
import nextcord
from nextcord.ext import commands
import json

# Bot settings
intents = nextcord.Intents.default()
intents.message_content = True
Server_ID=["PUT UR SERVER ID HERE BY REMOVE QUOTES"]
TOKEN = " PUT UR BOT TOKEN HERE INSIDE THE QUOTES "
userData = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'IMP_FILES', 'users.json')


# Main Bots
client = commands.Bot(
    command_prefix=".",
    intents=intents,
    status=nextcord.Status.online, 
    activity = nextcord.Game(name="with ur mom (/help)")
)
client.remove_command('help')


# Events
@client.event
async def on_ready():
  print(f"{client.user} is online and ready to go!")


@client.event
async def on_guild_join(guilds):
  channel = await client.fetch_channel(947354590901338132)
  await channel.send(f"{client.user} was added to **{guilds.name}**.\nNumber of server: `{len(client.guilds)}`")


@client.event
async def on_guild_remove(guilds):
  channel = await client.fetch_channel(947354590901338132)
  await channel.send(f"{client.user} was removed from **{guilds.name}**.\nNumber of server: `{len(client.guilds)}`.")


@client.event
async def on_member_join(member):
    with open(userData, 'r') as f:
        users = json.load(f)
    await update_data(users, member)
    with open(userData, 'w') as f:
         json.dump(users, f)
  
  
#Levels
@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
      if os.path.exists(userData):
        with open(userData, 'r') as f:
          users = json.load(f)
      else:
          users = {}
      await update_data(users, message.author)
      await add_experience(users, message.author, 2)
      await level_up(users, message.author, message)
      with open(userData, 'w') as f:
        json.dump(users, f)
      await client.process_commands(message)
  
  
async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1
  
  
async def add_experience(users, user, exp):
    if str(user.id) not in users:
        users[str(user.id)] = {"experience": 0, "level": 1}
    users[str(user.id)]['experience'] += 1


async def level_up(users, user, message):
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    
    if lvl_start < lvl_end:
        memberAvatar = user.display_avatar.url
        embed = nextcord.Embed(title="Level up", description=f'{user.mention} has leveled up to level {lvl_end}'.format(user.mention, lvl_end))
        embed.set_thumbnail(url = memberAvatar)
        await message.channel.send(embed=embed)
        users[f'{user.id}']['level'] = lvl_end


# slash commands
@client.slash_command(description="Responds with Pong!", guild_ids=[650256982200156172])
async def ping(ctx):
    await ctx.send(f"Pong! (`{round(client.latency * 1000)}ms`)")


# prefix commands
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! (`{round(client.latency * 1000)}ms`)")


# loading cogs
extensions = ['cogs.admincmd', 'cogs.funcmd', 'cogs.giveaway', 'cogs.helpcmd', 'cogs.level']

for ext in extensions:
    try:
        client.load_extension(ext)
        print(f"Loaded {ext} successfully!")
    except Exception as e:
        print(f"Failed to load extension {ext}: {e}")

client.run(TOKEN)