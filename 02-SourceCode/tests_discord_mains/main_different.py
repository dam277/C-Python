import discord
from discord import app_commands
from discord.ext import commands

import logging
from colorama import Fore
import json

class Bot(commands.Bot):
    def __init__(self, CONFIGS):
        #Declare intents
        INTENTS = discord.Intents.default()
        INTENTS.message_content = True
        INTENTS.guilds = True

        #Set the configs
        self.CONFIGS = CONFIGS

        #Set the tree
        self.client = discord.Client(intents=INTENTS)
        self.commands_tree = discord.app_commands.CommandTree(self.client)

        #Set properties to parent
        super().__init__(command_prefix="+", intents=INTENTS)

    def setup(self):
        @self.tree.command(guild=discord.Object(id=1024725027691712572), name="test", description="Test command")
        async def test_command(interaction: discord.Interaction):
            await interaction.response.send_message("test")

        @self.event
        async def on_message(message):
            print(f"{Fore.WHITE} -> {message.author}: {message.content}")
            
            if message.author == self.user:
                return
            
            if message.content.startswith('/hello'):
                await message.reply(f'Hello {message.author.display_name}')

        @self.event
        async def on_ready():
            logging.info(f"{Fore.GREEN}Logged on as {self.user}")
            
            try:
                synced = await self.commands_tree.sync(guild=discord.Object(id=1024725027691712572))
                print(f"Synced {len(synced)} commands")
            except Exception as e:
                logging.error(f"{Fore.RED} {e}")
    
    def run_bot(self):
        self.run(self.CONFIGS["token"])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    CONFIGS = json.load(open("src/configs/configs.json", "r"))

    bot = Bot(CONFIGS)
    bot.setup()
    bot.run_bot()
    