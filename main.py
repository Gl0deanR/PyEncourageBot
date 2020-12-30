import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  # prints message to console to verify the successful log in


@client.event
async def on_message(message):
    if message.author == client.user:  # check whether the bot sent the message or not, if it's the bot, do nothing
        return

    if message.content.startswith('$hello'):  # check for messages that start with "$hello" and respond
        await message.channel.send('Hello!')


client.run('YOUR_BOT_TOKEN_HERE')  # insert your bot token here, generated from Discord Developer Portal
