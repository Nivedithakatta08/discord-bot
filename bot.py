import discord
import random
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!hello':
        await message.channel.send('Hello! I am alive!')

    if message.content.startswith('!roast'):
        roasts = [
            "You're the reason we have warning labels on everything.",
            "I'd roast you but my mom said I'm not allowed to burn trash.",
            "You're not stupid, you just have bad luck thinking.",
            "I'd explain it to you but I don't have crayons with me.",
            "You're like a cloud. When you disappear, it's a beautiful day.",
        ]
        
        if message.mentions:
            target = message.mentions[0]
            roast = random.choice(roasts)
            await message.channel.send(f"{target.mention} {roast}")
        else:
            await message.channel.send("Who do you want me to roast? Tag someone! e.g. `!roast @someone`")

client.run(os.getenv('DISCORD_TOKEN'))