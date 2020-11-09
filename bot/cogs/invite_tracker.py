import discord
from discord.ext import commands
import TRACKER

class InviteTracking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.track = TRACKER.TRACKER(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
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
        
    '''
    Everything above do not change.
    It will automatically Add and remove invites when there events are triggered
    Just change the event below to match your API
    '''

    @commands.Cog.listener()
    async def on_member_join(self, member):
        inviter = await self.track.GET_INVITER(member).id  # Returns the inviters ID
        '''
        You can do all your stuff below here now.
        the variable inviter has the ID as opposed to there name + discriminator 
        '''

def setup(bot):
    bot.add_cog(InviteTracking(bot))
