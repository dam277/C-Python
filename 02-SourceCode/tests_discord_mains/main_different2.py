
import discord
from discord import app_commands
from discord.ext import commands

import logging
from colorama import Fore
import json

logging.basicConfig(level=logging.INFO)
CONFIGS = json.load(open("src/configs/configs.json", "r"))

#Declare intents
INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.guilds = True

bot = commands.Bot(command_prefix="+", intents=INTENTS)

client = discord.Client(intents=INTENTS)
tree = app_commands.CommandTree(client)

@bot.event
async def on_ready():
    logging.info(f"{Fore.GREEN}Logged on as {bot.user}")
    
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=1024725027691712572))
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        logging.error(f"{Fore.RED} {e}")

@bot.tree.command(guild=discord.Object(id=1024725027691712572), name="test", description="Test command")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("test")

@bot.event
async def on_message(message):
    print(f"{Fore.WHITE} -> {message.author}: {message.content}")
    
    if message.author == bot.user:
        return
    
    if message.content.startswith('/hello'):
        await message.reply(f'Hello {message.author.display_name}')

bot.run(CONFIGS["token"])