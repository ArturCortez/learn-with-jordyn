import discord
import re
from dotenv import load_dotenv
import os


def main():
    """
    this code makes the discord bot reacts when a link is posted on the channel. I believe that when
    a task is done, a link will be posted and the bot can alert the channel manager. The manager can then
    update tasks and rewards.
    """
    load_dotenv()
    bot_token = os.getenv('DISCORD_BOT_TOKEN')

    intents = discord.Intents.default()
    intents.messages = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        # Avoid the bot responding to its own messages
        if message.author == client.user:
            return

        # This regex matches URLs
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        if re.search(url_pattern, message.content):
            # If the message contains a URL, send an applause emoji or message
            await message.channel.send('👏 Great link! 👏')

    # Replace 'your_token_here' with your actual bot token
    client.run('your_token_here')


if __name__ == "__main__":
    main()
