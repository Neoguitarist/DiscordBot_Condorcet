# coding: utf-8
import locale

import asyncio
from discord import Intents
from discord.ext import commands
from base import DISCORD_LOCALE, DISCORD_OPERATOR, DISCORD_TOKEN
from condorcet import Condorcet
from birthday import HappyBirthday
from rolemanager import RoleManager
from economy import Economy
from emulator import Emulator

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, DISCORD_LOCALE)
    intents = Intents.all()
    bot = commands.Bot(command_prefix=DISCORD_OPERATOR, intents=intents)
    asyncio.run(bot.add_cog(Condorcet(bot)))
    # bot.add_cog(HappyBirthday(bot))
    # bot.add_cog(RoleManager(bot))
    # bot.add_cog(Economy(bot))
    # bot.add_cog(Emulator(bot))
    bot.run(DISCORD_TOKEN)
