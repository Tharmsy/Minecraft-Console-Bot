import discord
import asyncio
import valve.rcon

# do pip install py-rcon and pip install discord.py

DISCORD_TOKEN = "your-discord-bot-token-here"
RCON_PASSWORD = "your-game-server-rcon-password-here"
RCON_ADDRESS = ("localhost", 27015)

client = discord.Client()
rcon = valve.rcon.RCON(*RCON_ADDRESS, password=RCON_PASSWORD)

async def send_rcon_command(command):
    await rcon.connect()
    response = await rcon.execute(command)
    await rcon.disconnect()
    return response

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!"):
        command = message.content[1:]
        response = await send_rcon_command(command)

        await message.channel.send(f"Command sent: {command}\nResponse: {response}")

client.run(DISCORD_TOKEN)
