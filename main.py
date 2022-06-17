import os
import discord
import random
from keep_alive import keep_alive
keep_alive()
TOKEN = os.environ['BOT_TOKEN']
GUILD_ID_A = os.environ['DISCORD_GUILD_A']
GUILD_ID_B = os.environ['DISCORD_GUILD_B']

random.seed(5)

client = discord.Client()

counter = 0

limit = random.randint(1, 60)

list_msg = []
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  global limit
  global counter
  global list_msg
  if message.author == client.user:
    return
  if message.channel.id != int(os.environ['DISCORD_CHANNEL_A']) and message.channel.id != int(os.environ['DISCORD_CHANNEL_B']) and message.channel.id != int(os.environ['DISCORD_CHANNEL_C']):
    return
  counter = counter + 1
  list_msg.append(message.content)
  
  if counter >= limit:
    if counter % 2 == 0:
      await message.channel.send('SIUUUUUU')
    else:
      await message.channel.send(random.choice(list_msg))
    counter = 0
    list_msg.clear()
    limit = random.randint(1, 60)
    print("SIUUU")
    return
  
  rate = random.randint(1,100)
  print(rate)
  if (rate > 95):
    await message.channel.send(file=discord.File('ronaldo-drinking.jpg'))
  
client.run(TOKEN)