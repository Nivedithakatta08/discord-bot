import discord

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

client.run('MTUwOTE1NTAxNTk5NzI2Mzg5Mg.G1bBYM.5Bx4zQvcbjePg-4762_Avhv3n5lLxbfhWuy6BI')