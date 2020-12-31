import discord
import requests
import json
import random
from datetime import datetime


def get_part_of_day(hour):
    return (
        "morning" if 5 <= hour <= 11
        else
        "afternoon" if 12 <= hour <= 17
        else
        "evening" if 18 <= hour <= 17
        else
        "night"
    )


client = discord.Client()

# list of sad words to check, please feel free to add more
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

# list of encouragements for bot to say, please feel free to add more
starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!"
]

# list of ways so say 'hi', please feel free to add more
say_hello_words = [
    "Hi",
    "Hey there",
    "Whats up",
    "Good to see you",
    "Hey",
    "Yo!",
    "Sup"
]


# we use zenquotes API to receive a random quote and send it to the channel
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  # prints message to console to verify the successful log in


@client.event
async def on_message(message):
    if message.author == client.user:  # check whether the bot sent the message or not, if it's the bot, do nothing
        return

    msg = message.content
    msg_author = message.author

    h = datetime.now().hour
    m = datetime.now().minute
    say_part_of_day = get_part_of_day(h)
    country = 'Romania'

    if msg.startswith('!mornin') and say_part_of_day == 'morning':
        await message.channel.send(f'Morning {msg_author}')
    elif msg.startswith('!mornin') and say_part_of_day != 'morning':
        if 0 <= m <= 9:
            await message.channel.send(f'Here in {country} is {h}:0{m} so it is {say_part_of_day}')
        else:
            await message.channel.send(f'Here in {country} is {h}:{m} so it is {say_part_of_day}')
    elif msg.startswith('!afterno') and say_part_of_day == 'afternoon':
        await message.channel.send(f'Good afternoon {msg_author}')
    elif msg.startswith('!afterno') and say_part_of_day != 'afternoon':
        if 0 <= m <= 9:
            await message.channel.send(f'Here in {country} is {h}:0{m} so it is {say_part_of_day}')
        else:
            await message.channel.send(f'Here in {country} is {h}:{m} so it is {say_part_of_day}')
    elif msg.startswith('!eveni') and say_part_of_day == 'evening':
        await message.channel.send(f'Good evening {msg_author}')
    elif msg.startswith('!eveni') and say_part_of_day != 'evening':
        if 0 <= m <= 9:
            await message.channel.send(f'Here in {country} is {h}:0{m} so it is {say_part_of_day}')
        else:
            await message.channel.send(f'Here in {country} is {h}:{m} so it is {say_part_of_day}')
    elif msg.startswith('!night') and say_part_of_day == 'night':
        await message.channel.send(f'Good night {msg_author}. Sleep tight!')
    elif msg.startswith('!night') and say_part_of_day != 'night':
        if 0 <= m <= 9:
            await message.channel.send(f'Here in {country} is {h}:0{m} so it is {say_part_of_day}')
        else:
            await message.channel.send(f'Here in {country} is {h}:{m} so it is {say_part_of_day}')

    if msg.startswith('!time'):
        if 0 <= m <= 9:
            await message.channel.send(f'{country} time is {h}:0{m}')
        else:
            await message.channel.send(f'{country} time is {h}:{m}')

    if msg.startswith('!hi') or msg.startswith('!hello'):
        random_hi_message = random.choice(say_hello_words)
        await message.channel.send(f'{random_hi_message} {msg_author}')

    if msg.startswith('!inspire'):  # check for messages that start with "$inspire" and respond
        quote = get_quote()
        await message.channel.send(quote)

    # check if words in client message equal to those in our sad_words list and respond
    if any(word in msg for word in sad_words):
        cheer_up_item = random.choice(starter_encouragements)
        await message.channel.send(f'{cheer_up_item} {msg_author}')


# insert your bot token here, generated from Discord Developer Portal
client.run('INSERT_DISCORD_BOT_TOKEN_HERE')
