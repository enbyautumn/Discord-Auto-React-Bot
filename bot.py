import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix='%')
 
@bot.event
async def on_ready():
    print("ready")
 
 
@bot.event
async def on_message(message):
    if(message.channel.id == "737807052625412208"):
        await bot.add_reaction(message, "✅")
        await bot.add_reaction(message, "❌")
 
 
bot.run("bot_token_here")
