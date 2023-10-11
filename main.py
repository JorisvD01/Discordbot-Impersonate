import discord
from discord import app_commands
import json
import requests
from discord import Webhook, SyncWebhook

with open('config.json', 'r') as file:
    data = json.load(file)
    token = data['token']
    webhook_url = data['webhook_url']
    guild_id = data['guild_id']

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)
guild = discord.Object(id=guild_id)

@client.event
async def on_ready():
    await tree.sync(guild=guild)

@tree.command(name= "impersonate", description= "Send a message as if it came from a different user", guild=guild)
async def impersonate(ctx,user:discord.User,message:str):
    await ctx.response.send_message("Sending message...",ephemeral=True)

    WEBHOOK_ID = webhook_url.split("/")[5]

    sendchannel = client.get_channel(ctx.channel.id)
    json = {"channel_id": sendchannel.id}
    headers = {"Authorization": "Bot " + token}

    requests.patch('https://discordapp.com/api/webhooks/' + WEBHOOK_ID, json=json, headers=headers)

    webhook = SyncWebhook.from_url(webhook_url)
    webhook.send(message, username=user.display_name, avatar_url=user.display_avatar.url)

client.run(token)