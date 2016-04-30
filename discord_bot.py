#!/usr/bin/env python3
import discord
from usage import print_usage
from prime import check_for_prime
from eightball import ask8ball
from spoilme import spoilme
from kill import kill_bot
from wisecracker import crack_a_joke
from gitpull import gitpull

client = discord.Client()


@client.event
async def on_ready():
  print ('Logged in as')
  print (client.user.name)
  print (client.user.id)
  print ('------')


@client.event
async def on_message(message):
  if message.content.startswith('!8ball'):
    await ask8ball(client, message)
  elif message.content.startswith("!gitpull"):
    await gitpull(client, message)
  elif message.content.startswith('!help') or message.content.startswith('!usage'):
    await print_usage(client, message)
  elif message.content.startswith('!kill'):
    await kill_bot(client, message, client.user.name)
  elif message.content.startswith('!prime'):
    await checkForPrime(client, message)
  elif message.content.startswith('!spoilme'):
    await spoilme(client, message)

  await crack_a_joke(client, message)


with open("discord.login") as f:
  email = f.readline().rstrip()
  password = f.readline().rstrip()
  client.run(email, password)
