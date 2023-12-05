import discord
from discord import app_commands
from discord.ext import commands

import logging
from colorama import Fore
import json

class Bot(discord.Client):
    def __init__(self, CONFIGS):
        #Declare intents
        INTENTS = discord.Intents.default()
        INTENTS.message_content = True
        INTENTS.guilds = True

        #Set the bot variable
        self.bot = commands.Bot(command_prefix="+", intents=INTENTS)

        #Set the configs
        self.CONFIGS = CONFIGS

        #Set properties to parent
        super().__init__(intents=INTENTS)
        # self.tree = discord.app_commands.CommandTree(self)

    def setup(self):
        @self.bot.event
        async def on_ready():
            logging.info(f"{Fore.GREEN}Logged on as {self.bot.user}")

        @self.bot.event
        async def on_message(message):
            print(f"{Fore.WHITE} -> {message.author}: {message.content}")
            
            if message.author == self.user:
                return
            
            if message.content.startswith('/hello'):
                await message.reply(f'Hello {message.author.display_name}')
    
    def run_bot(self):
        self.bot.run(self.CONFIGS["token"])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    CONFIGS = json.load(open("src/configs/configs.json", "r"))

    client = Bot(CONFIGS)
    # tree = app_commands.CommandTree(client)
    client.setup()
    client.run_bot()
    