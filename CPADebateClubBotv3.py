import discord
from discord.ext import commands
import time as t

#Bot Token
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

#Command Prefix for bot "Client"
client = commands.Bot(command_prefix = "+")

#When activated and connected
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

#Help Command
@client.command()
async def bothelp(context):
    await context.send(
        "+ is bot command prefix.\n+stop will stop any ongoing debate command.\nCurrent commands include:\n+JHI\n+JHILO\n+SHI\n+SHILO\nNote: Do not initiate two debates at once."
        )

#Start debate
@client.command()
async def JHI(context,minutes):
    #Invalid Time Corner Case
    if int(minutes) < 2 or int(minutes) > 12:
        await context.send("Invalid Time. Must be atleast 2 to 12 minutes.")
        raise Exception("Invalid Time")
    
    if int(minutes) == 2:

        strings = (
            f"Debate has started.\nThere are {minutes} minutes remaining.",
            "15 Seconds Left - Grace.",
            "10 Seconds Left.",
            "5 Seconds Left",
            "Grace Over.\nThe speech ended and lasted 2 minutes."
        )
        intervals = (
            0,
            120,
            5,
            5,
            5
        )

        true_initial = t.time()
        initial_time = t.time()
        
        section = 0
        section2 = 1
        running = True

        while running:
            current_time = t.time()
            
            if current_time - true_initial >= 60*section2: #If a minute has elapsed
                await context.send(f"There are {int(minutes) - section2} minutes remaining.")
                section2 += 1

            #If a stop is detected from first message history
            messages = await context.channel.history(limit=1,oldest_first=False).flatten()

            if messages[0].content == "+stop":
                await context.send(f"The debate ended early and lasted {round((t.time()-true_initial)/60,2)} minute(s).")
                running = False

            else:
                #No stop detected Stop
                if current_time - initial_time >= intervals[section]: 
                    await context.send(strings[section])
                    section += 1
                    initial_time = current_time
            #This will automatically go index out of range and end itself

    elif int(minutes) == 3:

        strings = (
            f"Debate has started.\nThere are {minutes} minutes remaining.",
            "POI Open.",
            "POI Closed.",
            "15 Seconds Left - Grace.",
            "10 Seconds Left.",
            "5 Seconds Left",
            "Grace Over.\nThe speech ended and lasted 3 minutes."
            )
        
        intervals = (
            0,
            30,
            120,
            30,
            5,
            5,
            5
        )

        true_initial = t.time()
        initial_time = t.time()
        
        section = 0
        section2 = 1
        running = True

        while running:
            current_time = t.time()

            if current_time - true_initial >= 60*section2: #If a minute has elapsed
                await context.send(f"There are {int(minutes) - section2} minutes remaining.")
                section2 += 1
            #If a stop is detected from first message history
            messages = await context.channel.history(limit=1,oldest_first=False).flatten()

            if messages[0].content == "+stop":
                await context.send(f"The debate ended early and lasted {round((t.time()-true_initial)/60,2)} minute(s).")
                running = False

            else:
                #No stop detected Stop
                if current_time - initial_time >= intervals[section]: 
                    await context.send(strings[section])
                    section += 1
                    initial_time = current_time
            #This will automatically go index out of range and end itself

    else:

        strings = (
            f"Debate has started.\nThere are {minutes} minutes remaining.",
            "POI Open.",
            "POI Closed.",
            "15 Seconds Left - Grace.",
            "10 Seconds Left.",
            "5 Seconds Left",
            f"Grace Over.\nThe speech ended and lasted {minutes} minutes."
            )
        
        intervals = (
            0,
            60,
            int(minutes)*60-120,
            60,
            5,
            5,
            5
        )

        true_initial = t.time()
        initial_time = t.time()
        
        section = 0
        section2 = 1
        running = True

        while running:
            current_time = t.time()
            if current_time - true_initial >= 60*section2: #If a minute has elapsed
                await context.send(f"There are {int(minutes) - section2} minutes remaining.")
                section2 += 1
            #If a stop is detected from first message history
            messages = await context.channel.history(limit=1,oldest_first=False).flatten()
            
            #Checked most recent message
            if messages[0].content == "+stop":
                await context.send(f"The debate ended early and lasted {round((t.time()-true_initial)/60,2)} minute(s).")
                running = False

            else:
                #No stop detected Stop
                if current_time - initial_time >= intervals[section]: 
                    await context.send(strings[section])
                    section += 1
                    initial_time = current_time
            #This will automatically go index out of range and end itself

#Start debate
@client.command()
async def JHILO(context,minutes):
    #Invalid Time Corner Case
    if int(minutes) < 5 or int(minutes) > 12:
        await context.send("Invalid Time. Must be atleast 5 to 12 minutes.")
        raise Exception("Invalid Time")

    strings = (
        f"Debate has started.\nThere are {minutes} minutes remaining.",
        "POI Open.",
        "POI Closed.",
        "15 Seconds Left - Grace.",
        "10 Seconds Left.",
        "5 Seconds Left",
        f"Grace Over.\nThe speech ended and lasted {minutes} minutes."
        )
    
    intervals = (
        0,
        60,
        int(minutes)*60-180,
        120,
        5,
        5,
        5
    )

    true_initial = t.time()
    initial_time = t.time()
    
    section = 0
    section2 = 1
    running = True

    while running:
        current_time = t.time()
        if current_time - true_initial >= 60*section2: #If a minute has elapsed
            await context.send(f"There are {int(minutes) - section2} minutes remaining.")
            section2 += 1
        #If a stop is detected from first message history
        messages = await context.channel.history(limit=1,oldest_first=False).flatten()
        
        #Checked most recent message
        if messages[0].content == "+stop":
            await context.send(f"The debate ended early and lasted {round((t.time()-true_initial)/60,2)} minute(s).")
            running = False

        else:
            #No stop detected Stop
            if current_time - initial_time >= intervals[section]: 
                await context.send(strings[section])
                section += 1
                initial_time = current_time
        #This will automatically go index out of range and end itself

#Start debate
@client.command()
async def SHI(context,minutes):
    #Invalid Time Corner Case
    if int(minutes) < 3 or int(minutes) > 12:
        await context.send("Invalid Time. Must be atleast 3 to 12 minutes.")
        raise Exception("Invalid Time")

    #If 3 everything is protected
    #If 5 30 seconds first and last
    
    if int(minutes) == 3:

        strings = (
            f"Debate has started.\nThere are {minutes} minutes remaining.",
            "15 Seconds Left - Grace.",
            "10 Seconds Left.",
            "5 Seconds Left",
            "Grace Over.\nThe speech ended and lasted 3 minutes."
        )
        intervals = (
            0,
            180,
            5,
            5,
            5
        )

        true_initial = t.time()
        initial_time = t.time()
        
        section = 0
        section2 = 1
        running = True

        while running:
            current_time = t.time()
            if current_time - true_initial >= 60*section2: #If a minute has elapsed
                await context.send(f"There are {int(minutes) - section2} minutes remaining.")
                section2 += 1
            #If a stop is detected from first message history
            messages = await context.channel.history(limit=1,oldest_first=False).flatten()

            if messages[0].content == "+stop":
                await context.send(f"The debate ended early and lasted {round((t.time()-true_initial)/60,2)} minute(s).")
                running = False

            else:
                #No stop detected Stop
                if current_time - initial_time >= intervals[section]: 
                    await context.send(strings[section])
                    section += 1
                    initial_time = current_time
            #This will automatically go index out of range and end itself

    elif int(minutes) == 5:

        strings = (
            f"Debate has started.\nThere are {minutes} minutes remaining.",
            "POI Open.",
            "POI Closed.",
            "15 Seconds Left - Grace.",
            "10 Seconds Left.",
            "5 Seconds Left",
            "Grace Over.\nThe speech ended and lasted 5 minutes."
            )
        
        intervals = (
            0,
            30,
            240,
            30,
            5,
            5,
            5
        )

        true_initial = t.time()
        initial_time = t.time()
        
        section = 0
        section2 = 1
        running = True

        while running:
            current_time = t.time()
            if current_time - true_initial >= 60*section2: #If a minute has elapsed
                await context.send(f"There are {int(minutes) - section2} minutes remaining.")
                section2 += 1
            #If a stop is detected from first message history
            messages = await context.channel.history(limit=1,oldest_first=False).flatten()

            if messages[0].content == "+stop":
                await context.send(f"The debate ended early and lasted {round((t.time()-true_initial)/60,2)} minute(s).")
                running = False

            else:
                #No stop detected Stop
                if current_time - initial_time >= intervals[section]: 
                    await context.send(strings[section])
                    section += 1
                    initial_time = current_time
            #This will automatically go index out of range and end itself

    else:

        strings = (
            f"Debate has started.\nThere are {minutes} minutes remaining.",
            "POI Open.",
            "POI Closed.",
            "15 Seconds Left - Grace.",
            "10 Seconds Left.",
            "5 Seconds Left",
            f"Grace Over.\nThe speech ended and lasted {minutes} minutes."
            )
        
        intervals = (
            0,
            60,
            int(minutes)*60-120,
            60,
            5,
            5,
            5
        )

        true_initial = t.time()
        initial_time = t.time()
        
        section = 0
        section2 = 1
        running = True

        while running:
            current_time = t.time()
            if current_time - true_initial >= 60*section2: #If a minute has elapsed
                await context.send(f"There are {int(minutes) - section2} minutes remaining.")
                section2 += 1
            #If a stop is detected from first message history
            messages = await context.channel.history(limit=1,oldest_first=False).flatten()
            
            #Checked most recent message
            if messages[0].content == "+stop":
                await context.send(f"The debate ended early and lasted {round((t.time()-true_initial)/60,2)} minute(s).")
                running = False

            else:
                #No stop detected Stop
                if current_time - initial_time >= intervals[section]: 
                    await context.send(strings[section])
                    section += 1
                    initial_time = current_time
            #This will automatically go index out of range and end itself

#Start debate
@client.command()
async def SHILO(context,minutes):
    #Invalid Time Corner Case
    if int(minutes) < 8 or int(minutes) > 12:
        await context.send("Invalid Time. Must be atleast 8 to 12 minutes.")
        raise Exception("Invalid Time")

    strings = (
        f"Debate has started.\nThere are {minutes} minutes remaining.",
        "POI Open.",
        "POI Closed.",
        "15 Seconds Left - Grace.",
        "10 Seconds Left.",
        "5 Seconds Left",
        f"Grace Over.\nThe speech ended and lasted {minutes} minutes."
        )
    
    intervals = (
        0,
        60,
        int(minutes)*60-240,
        180,
        5,
        5,
        5
    )

    true_initial = t.time()
    initial_time = t.time()
    
    section = 0
    section2 = 1
    running = True

    while running:
        current_time = t.time()
        if current_time - true_initial >= 60*section2: #If a minute has elapsed
            await context.send(f"There are {int(minutes) - section2} minutes remaining.")
            section2 += 1
        #If a stop is detected from first message history
        messages = await context.channel.history(limit=1,oldest_first=False).flatten()
        
        #Checked most recent message
        if messages[0].content == "+stop":
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
