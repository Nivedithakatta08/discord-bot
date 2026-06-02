import discord
import random
import requests
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
            await message.channel.send(f"{target.mention} {random.choice(roasts)}")
        else:
            await message.channel.send("Tag someone! e.g. `!roast @someone`")

    if message.content.startswith('!comeback'):
        comebacks = [
            "Debba adhurs kadhu?",
            "Builder handover chesada? Padmavathi happy eh na? Tiles esthunaru anta kadha!",
            "Athiga aavesha pade magaadu, athiga aashapade aadadhi baagupadinattu charitra lo ledhu!",
            "Evadu kodithe dimma tirigi mind block aipoddo vaade pandu gaadu!",
            "Veera Shankar Reddy, Mokke kada ani peekeste, peeka kosta.",
            "Current teegalekki aadukuntanu antav entayya? Kaaki la maadipothav!",
            "You Know...Guntur Bolke Ek Sheher Hain? Nenu ikkada Kotaananuko…Resound Udhar Aatha!!",
            "Chantigaadu LOCAL!",
            "Appal naidu...dadagiri ki vachchina dourjanyaaniki vachchina goondaisaniki vachchina grouplu katataniki vachchina rajakiyam tho vachchina rowdyisam tho vachchina...puta ko sevam lekkana chappuna port ki bali avuthaayi. Teeram lo keratalu la erupu rangu pusukoni potethutaiii!!!",
            "Doosukelle banam, race lo Gurram venakki chudavu!",
        ]
        if message.mentions:
            target = message.mentions[0]
            await message.channel.send(f"{target.mention} {random.choice(comebacks)}")
        else:
            await message.channel.send("Tag someone! e.g. `!comeback @someone`")

    if message.content.startswith('!toss'):
        result = random.choice(['Heads! 🪙', 'Tails! 🪙'])
        if message.mentions:
            target = message.mentions[0]
            await message.channel.send(f"{target.mention} {result}")
        else:
            await message.channel.send(f"{message.author.mention} {result}")

    elif message.content.startswith('!rps'):
        result = random.choice(['Rock! 🪨', 'Paper! 📄', 'Scissors! ✂️'])
        if message.mentions:
            target = message.mentions[0]
            await message.channel.send(f"{target.mention} {result}")
        else:
            await message.channel.send(f"{message.author.mention} {result}")

    if message.content == '!joke':
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        joke = response.json()
        await message.channel.send(f"{joke['setup']}\n\n||{joke['punchline']}||")

    if message.content.startswith('!poll'):
        question = message.content[6:].strip()
        if not question:
            await message.channel.send("Ask something! e.g. `!poll Is pineapple on pizza good?`")
        else:
            poll = await message.channel.send(f"📊 **{question}**\n\n✅ Yes\n❌ No")
            await poll.add_reaction('✅')
            await poll.add_reaction('❌')

    if message.content == '!truth':
        truths = [
            "What's the most embarrassing thing you've ever done?",
            "Have you ever lied to get out of trouble? What was it?",
            "What's your biggest fear?",
            "Have you ever had a crush on someone in this server?",
            "What's the worst gift you've ever received?",
            "Have you ever blamed someone else for something you did?",
            "What's the most childish thing you still do?",
            "Have you ever ghosted someone? Why?",
            "What's your most used emoji and what does that say about you?",
            "What's a secret you've never told anyone?",
        ]
        await message.channel.send(f"🎯 Truth for {message.author.mention}:\n\n**{random.choice(truths)}**")

client.run(os.getenv('DISCORD_TOKEN'))