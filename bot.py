import discord
import random
import requests
import asyncio
import math
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

    if message.content.startswith('!choose'):
        options = message.content[8:].split('|')
        if len(options) < 2:
            await message.channel.send("Give me options! e.g. `!choose pizza | burger | sushi`")
        else:
            pick = random.choice(options).strip()
            await message.channel.send(f"🎲 I choose: **{pick}**")

    if message.content.startswith('!remindme'):
        parts = message.content.split(' ', 2)
        if len(parts) < 3:
            await message.channel.send("Usage: `!remindme <time> <reminder>`\ne.g. `!remindme 10m Study for exam`")
        else:
            time_str = parts[1]
            reminder_text = parts[2]
            if time_str.endswith('m'):
                seconds = int(time_str[:-1]) * 60
            elif time_str.endswith('h'):
                seconds = int(time_str[:-1]) * 3600
            else:
                await message.channel.send("Use `m` for minutes or `h` for hours. e.g. `30m` or `2h`")
                return
            await message.channel.send(f"⏰ Got it {message.author.mention}! I'll remind you in **{time_str}**.")
            await asyncio.sleep(seconds)
            try:
                await message.author.send(f"⏰ **Reminder:** {reminder_text}")
            except:
                await message.channel.send(f"⏰ {message.author.mention} **Reminder:** {reminder_text}")

    if message.content.startswith('!calc'):
        expr = message.content[6:].strip()
        if not expr:
            await message.channel.send("Usage: `!calc <expression>` e.g. `!calc 25 * 4 + 10`")
        else:
            try:
                result = eval(expr, {"__builtins__": {}}, {"sqrt": math.sqrt, "pi": math.pi})
                await message.channel.send(f"🧮 `{expr}` = **{result}**")
            except:
                await message.channel.send("❌ Invalid expression.")

    if message.content.startswith('!define'):
        word = message.content[8:].strip()
        if not word:
            await message.channel.send("Usage: `!define <word>` e.g. `!define ephemeral`")
        else:
            response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
            if response.status_code != 200:
                await message.channel.send(f"❌ No definition found for **{word}**")
            else:
                data = response.json()[0]
                definition = data['meanings'][0]['definitions'][0]['definition']
                part_of_speech = data['meanings'][0]['partOfSpeech']
                await message.channel.send(
                    f"📖 **{word.capitalize()}** *({part_of_speech})*\n\n{definition}"
                )

    if message.content.startswith('!avatar'):
        if message.mentions:
            target = message.mentions[0]
        else:
            target = message.author
        await message.channel.send(f"🖼️ **{target.display_name}'s Avatar**\n{target.display_avatar.url}")

    if message.content == '!serverinfo':
        guild = message.guild
        await message.channel.send(
            f"🏠 **Server Info**\n\n"
            f"📛 Name: **{guild.name}**\n"
            f"👑 Owner: **{guild.owner}**\n"
            f"👥 Members: **{guild.member_count}**\n"
            f"📅 Created: **{guild.created_at.strftime('%d %B %Y')}**\n"
            f"💬 Channels: **{len(guild.channels)}**\n"
            f"🎭 Roles: **{len(guild.roles)}**"
        )

    if message.content.startswith('!userinfo'):
        if message.mentions:
            target = message.mentions[0]
        else:
            target = message.author
        await message.channel.send(
            f"👤 **User Info**\n\n"
            f"🪪 Name: **{target.name}**\n"
            f"🏷️ Display Name: **{target.display_name}**\n"
            f"🆔 ID: **{target.id}**\n"
            f"📅 Account Created: **{target.created_at.strftime('%d %B %Y')}**\n"
            f"📥 Joined Server: **{target.joined_at.strftime('%d %B %Y')}**\n"
            f"🎭 Top Role: **{target.top_role.name}**"
        )

    if message.content.startswith('!coinflip'):
        parts = message.content.split(' ', 1)
        if len(parts) < 2 or parts[1].lower() not in ['heads', 'tails']:
            await message.channel.send("Usage: `!coinflip heads` or `!coinflip tails`")
        else:
            guess = parts[1].lower()
            result = random.choice(['heads', 'tails'])
            if guess == result:
                await message.channel.send(f"🪙 It's **{result}**! {message.author.mention} guessed right! 🎉")
            else:
                await message.channel.send(f"🪙 It's **{result}**! {message.author.mention} guessed wrong! 💀")

    if message.content == '!number':
        response = requests.get('http://numbersapi.com/random/trivia')
        if response.status_code == 200:
            await message.channel.send(f"🔢 {response.text}")
        else:
            await message.channel.send("❌ Couldn't fetch a fact right now, try again!")

    if message.content.startswith('!age'):
        parts = message.content.split(' ', 1)
    if len(parts) < 2:
        await message.channel.send("Usage: `!age <birth year>` e.g. `!age 2003`")
    else:
        try:
            birth_year = int(parts[1].strip())
            age = 2026 - birth_year
            await message.channel.send(f"🎂 You are **{age} years old!**")
        except:
            await message.channel.send("❌ Enter a valid year e.g. `!age 2003`")

    if message.content.startswith('!horoscope'):
        sign = message.content[11:].strip().lower()
        horoscopes = {
        "aries": "The stars say you will trip today. Watch your step. 🐏",
        "taurus": "Mercury is in retrograde and so is your bank account. 🐂",
        "gemini": "You will send a text to the wrong person today. Good luck. 👯",
        "cancer": "The moon is crying. That's you. That's literally you. 🦀",
        "leo": "You looked in the mirror 14 times today. The stars counted. 🦁",
        "virgo": "You will make a to-do list and complete nothing on it. 📋",
        "libra": "You will spend 45 minutes choosing what to watch and then not watch it. ⚖️",
        "scorpio": "Someone is thinking about you. It's not good. 🦂",
        "sagittarius": "You will say 'I'm almost ready' for the next 3 hours. 🏹",
        "capricorn": "The grind never stops. Neither does your suffering. 🐐",
        "aquarius": "You will have a great idea and tell no one about it. 🪣",
        "pisces": "You will daydream so hard you miss your stop. 🐟",
    }
    if sign not in horoscopes:
        await message.channel.send("Usage: `!horoscope <sign>` e.g. `!horoscope leo`")
    else:
        await message.channel.send(f"🔮 **{sign.capitalize()} Horoscope:**\n\n{horoscopes[sign]}")

client.run(os.getenv('DISCORD_TOKEN'))