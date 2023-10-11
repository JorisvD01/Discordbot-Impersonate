# Discordbot-Impersonate-script
 Send a message as if it came from a different user

# Start using the bot

Download main.py and config.json and put both together in a folder.
Create a discord bot account and place the token of your server in the config.json.
In your server settings, go to intergrations > webhooks and create a webhook (name and channel don't matter). Copy the URL and place it in the config.json
Using /impersonale <username> <message> you can send a message as it it came from the specified user (there will be a bot tag, this is not changeable)

# Requirements

This bot is created using discord.py 2.0 in python 3.
PIP packages used: discord.py, requests and json
