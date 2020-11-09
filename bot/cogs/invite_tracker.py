import discord
from discord.ext import commands
import TRACKER

class InviteTracking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.track = TRACKER.TRACKER(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        print('I am loaded')
        await self.track.ALL_INVITES()

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        await self.track.UPDATE_INVITE(invite)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.track.CREATE_GUILD_INVITES(guild)

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        await self.track.REMOVE_INVITES(invite)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.track.REMOVE_INVITES(guild)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        inviter = await self.track.GET_INVITER(member)
        invter = inviter.id

def setup(bot):
    bot.add_cog(InviteTracking(bot))
