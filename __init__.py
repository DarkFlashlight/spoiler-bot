import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!spoiler '):
        message.content = message.content[9:]
        await client.delete_message(message)
        await client.send_message(message.channel, message.content)

client.run(os.environ['discord_api_key'])