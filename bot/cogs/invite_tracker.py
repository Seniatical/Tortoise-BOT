import discord
from discord.ext import commands
import bot.utils import TRACKING

class InviteTracking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tracking = TRACKER.TRACKER(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.tracking.ALL_INVITES()

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        await self.tracking.UPDATE_INVITE(invite)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.tracking.CREATE_GUILD_INVITES(guild)

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        await self.tracking.REMOVE_INVITES(invite)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.tracking.REMOVE_INVITES(guild)
        
    '''
    Dont modify or remove anything above
    Otherwise it will interfere with the invite cache
    Modify the event below.
    '''

    @commands.Cog.listener()
    async def on_member_join(self, member):
        inviter_id = await self.tracking.GET_INVITER(member).id
        # Do stuff with there id

def setup(bot):
    bot.add_cog(InviteTracking(bot))
