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
            comeback = random.choice(comebacks)
            await message.channel.send(f"{target.mention} {comeback}")
    

    if message.content.startswith('!toss'):
        result = random.choice(['Heads! 🪙', 'Tails! 🪙'])
    
    if message.mentions:
        target = message.mentions[0]
        await message.channel.send(f"{target.mention} {result}")
    else:
        await message.channel.send(f"{message.author.mention} {result}")

    if message.content.startswith('!rock-paper-scissors'):
        result = random.choice(['Rock!','Paper!','Scissors!'])

        if message.mentions:
            target = message.mentions[0]
            await message.channel.send(f"{target.mention} {result}")
        else:
            await message.channel.send(f"{message.author.mention} {result}")


client.run(os.getenv('DISCORD_TOKEN'))