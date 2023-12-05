import discord
from discord import app_commands
from discord.ext import commands

import logging
from colorama import Fore
import json

class Bot(discord.Client):
    def __init__(self, CONFIGS):
        """ Init the bot instance """
        #Declare intents
        INTENTS = discord.Intents.default()
        INTENTS.message_content = True
        INTENTS.guilds = True

        #Set the bot variable
        self.bot = commands.Bot(command_prefix="+", intents=INTENTS)
        print("prefix", self.bot.command_prefix)
        #Set the configs
        self.CONFIGS = CONFIGS

        #Set properties to parent
        super().__init__(intents=INTENTS)

    def setup(self):
        """ Setup the bot commands and events """
        @self.bot.event
        async def on_ready():
            """ Execute when the bot is ready """
            logging.info(f"{Fore.GREEN}Logged on as {self.bot.user}")
            try:
                # Get the commands to sync
                synced = await self.bot.tree.sync(guild=discord.Object(id=1024725027691712572))
                print(f"Synced {len(synced)} commands")
            except Exception as e:
                logging.error(f"{Fore.RED} {e}")

        @self.bot.event
        async def on_message(message):
            """ Execute when a message is sended
            $param -> message : Message sended
            """
            print(f"{Fore.WHITE} -> {message.author}: {message.content}")
            
            # Check if the author is the bot himself
            if message.author == self.user:
                return
            
            # Check the command to send the message
            if message.content.startswith('$hello'):
                await message.reply(f'Hello {message.author.display_name}')

        @self.bot.tree.command(guild=discord.Object(id=1024725027691712572), name="test", description="Test command")
        async def test_command(interaction: discord.Interaction):
            """ Execute when the command /test is sended
            $param -> interaction(discord.Interaction) : interaction of the user with the command
            """
            await interaction.response.send_message("test")
    
    def run_bot(self):
        """ Run the bot """
        self.bot.run(self.CONFIGS["token"])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    CONFIGS = json.load(open("src/configs/configs.json", "r"))

    client = Bot(CONFIGS)
    client.setup()
    client.run_bot()
    