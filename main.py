# Imports
import nextcord
from nextcord.ext import commands
import os
import json

# Bots
client = commands.Bot(
    command_prefix=".", 
    status=nextcord.Status.online, 
    activity = nextcord.Game(name="with u (.help)")
)
client.remove_command('help')
TOKEN = os.environ.get("TOKEN")
os.chdir(r'D:/Works/Codes/Bot 2.0/files')


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
    with open('users.json', 'r') as f:
        users = json.load(f)
  
    await update_data(users, member)
  
    with open('users.json', 'w') as f:
         json.dump(users, f)
  
  
@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users=json.load(f)
        await update_data(users, message.author)
        await add_experience(users, message.author, 2)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f)
    await client.process_commands(message)
  
  
async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1
  
  
async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp
  
  
async def level_up(users, user, message):
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        memberAvatar = user.avatar_url
        embed = nextcord.Embed(title="Level up", description=f'{user.mention} has leveled up to level {lvl_end}'.format(user.mention, lvl_end))
        embed.set_thumbnail(url = memberAvatar)
        await message.channel.send(embed=embed)
        users[f'{user.id}']['level'] = lvl_end


# Commands
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! (`{round(client.latency*1000)}ms` latency)")


extensions = ['cogs.admincmd', 'cogs.funcmd', 'cogs.helpcmd', 'cogs.level', 'cogs.music']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

client.run(TOKEN)