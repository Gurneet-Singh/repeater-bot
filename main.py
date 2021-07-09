import discord
import os
import keep_alive
import random

client = discord.Client()

offending = ["stupid", "idiot", "idot", "nub", "noob"]
osecondary = ["im", "i'm", "i am"]
quoteonquotecomebacks = ["yea we know", "of course you are", "isnt it obvious?", "dude, even a bot knows thats true"]

@client.event
async def on_ready():
  print("What's up sub bots. I'm alive. Deal with it.")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("!repeat"):
    l1 = message.content.split()
    l1.remove("!repeat")
    msg = ""
    onum = 0
    osecnum = 0
    for i in l1:
      msg += i
      msg += " "

      if i.LOWER() in offending:
        onum += 1
      if i.LOWER() in osecondary:
        osecnum += 1

      
    if onum > 0 and osecnum > 0:
      await message.channel.send(quoteonquotecomebacks[random.randint(0, 3)])
    else:
      await message.channel.send(msg)

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))