import discord
import requests
import json
import random

client = discord.Client()

# list of sad words to check
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

# list of encouragements for bot to say
starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!"
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

    if msg.startswith('$inspire'):  # check for messages that start with "$inspire" and respond
        quote = get_quote()
        await message.channel.send(quote)

    # check if words in client message equal to those in our sad_words list and respond
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))


client.run('YOUR_BOT_TOKEN_HERE')  # insert your bot token here, generated from Discord Developer Portal
