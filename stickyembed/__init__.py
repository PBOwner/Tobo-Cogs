"""Sticky - Sticky messages to a channel."""
import asyncio
from redbot.core.bot import Red

from .stickyembed import StickyEmbed


async def setup(bot: Red):
    """Load Sticky."""
    cog = StickyEmbed(bot)
    if asyncio.iscoroutinefunction(bot.add_cog):
        await bot.add_cog(cog)
    else:
        bot.add_cog(cog)
