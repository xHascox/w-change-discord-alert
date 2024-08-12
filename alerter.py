import discord
from discord.ext import commands
import time
import subprocess

def send_msg_to_user(w):

    TOKEN = DISCORD_API_TOKEN

    # Create a bot instance with command prefix "!"
    intents = discord.Intents(messages=True, guilds=True)
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Event that is triggered when the bot is ready
    @bot.event
    async def on_ready():
        print(f'Bot is ready! Logged in as {bot.user}')

        # User ID you want to send a message to
        user_id = DISCORD_USER_ID_TO_BE_ALERTED
        user = await bot.fetch_user(user_id)
        print(user)

        if user:
            await user.send("Konnichiwa! 🌸 It's your girl here! 💌\n There was a new Login:")
            await user.send(w)
            print(f'Message sent to {user.name}!')
        else:
            print('User not found! 😢')
        await bot.close()
        print("closed")

    # Run the bot with your token
    bot.run(TOKEN)
    

REMINDER = 864000 # sec = 10 days

SLEEPER = 10 # sec

iterations = 0

old_w = ""
while 1:
    w = subprocess.run("w -h", shell=True, capture_output=True, text=True).stdout
    if w.count("\n") != old_w.count("\n"):
        send_msg_to_user(w)
        old_w = w
    
    time.sleep(10)
    iterations+= 1
    if iterations>=REMINDER/SLEEPER:
        send_msg_to_user("🌸 Guard-Girl still watching, remember to do some updates 💌")
        iterations = 0
