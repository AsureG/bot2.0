from http import client
import nextcord
from nextcord.ext import commands
import asyncio
import random


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Start a Giveaway", guild_ids=[650256982200156172])
    async def giveaway(self, interaction: nextcord.Interaction, time: str, *, prize: str):
        if not time or not prize:
            return await interaction.response.send_message(
                "```"
                "giveaway {time} {prize}"
                "```"
            )

        embed = nextcord.Embed(
            title=' New Giveaway! ',
            description=f"{interaction.user.mention} is giving away **{prize}**!",
        )
        embed.set_footer(text=f"Giveaway ends in {time}")

        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        try:
            gawtime = int(time[:-1]) * time_convert[time[-1].lower()]
        except (ValueError, KeyError):
            return await interaction.response.send_message("Invalid time format! Use `s` for seconds, `m` for minutes, `h` for hours, or `d` for days.")

        await interaction.response.send_message(embed=embed)
        gaw_msg = await interaction.original_message()
        await gaw_msg.add_reaction("✋")

        await asyncio.sleep(gawtime)

        new_gaw_msg = await interaction.channel.fetch_message(gaw_msg.id)
        reaction = new_gaw_msg.reactions[0]
        users = await reaction.users().flatten()

        valid_users = [user for user in users if user.id != self.bot.user.id]

        if len(valid_users) < 1:
            return await interaction.channel.send("No valid users in the giveaway!")

        winner = random.choice(valid_users)
        await interaction.channel.send(f"Congrats {winner.mention} has won the giveaway for **{prize}**! 🎉")

def setup(bot):
    bot.add_cog(Giveaway(bot))