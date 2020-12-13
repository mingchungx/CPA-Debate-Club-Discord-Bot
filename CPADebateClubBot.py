import discord
from discord.ext import commands
import time as t

#Bot Token
TOKEN = "XXXXXXXXXXXXXXXXXXXXX"

#Command Prefix for bot "Client"
client = commands.Bot(command_prefix = "+")

#When activated and connected
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

#Help Command
@client.command()
async def bothelp(context):
    await context.send("+ is the command-prefix.\n+start n initiates an n minute timer.\n+stop ends the timer initiated by +start.")

#Start debate
@client.command()
async def start(context,minutes):
    #Invalid Time Corner Case
    if int(minutes) <= 0 or int(minutes) > 12:
        await context.send("Invalid Time. Must be atleast 1 to 12 minutes.")
        raise Exception("Invalid Time")

    strings = (
        "Debate has started.",
        "POI Open.",
        "POI Closed.",
        "15 Seconds Left - Grace.",
        "10 Seconds Left.",
        "5 Seconds Left",
        f"Grace Over.\nThe speech ended and lasted {minutes} minute(s)."
        )
    
    intervals = (
        0,
        15,
        int(minutes)*60-30,
        15,
        5,
        5,
        5
    )

    true_initial = t.time()
    initial_time = t.time()
    
    section = 0
    running = True

    while running:
        current_time = t.time()
        #If a stop is detected from first message history
        messages = await context.channel.history(limit=1,oldest_first=False).flatten()

        if messages[0].content == "+stop": ##
            await context.send(f"The debate ended early and lasted {round((t.time()-true_initial)/60,2)} minute(s).")
            running = False

        else:
            #No stop detected Stop
            if current_time - initial_time >= intervals[section]: 
                await context.send(strings[section])
                section += 1
                initial_time = current_time
        #This will automatically go index out of range and end itself

client.run(TOKEN)