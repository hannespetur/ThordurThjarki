#!/usr/bin/env python3
import discord
import asyncio
import random
from prime import checkForPrime
from eightball import ask8ball
from spoilme import spoilme
from wisecracker import crack_a_joke
from trivia import Trivia

client = discord.Client()
trivia = Trivia()

@client.event
async def on_ready():
  print ('Logged in as')
  print (client.user.name)
  print (client.user.id)
  print ('------')

@client.event
async def on_message(message):
  if message.content.startswith('!prime'):
    await checkForPrime(client, message)
  elif message.content.startswith('!8ball'):
    await ask8ball(client, message)
  elif message.content.startswith('!spoilme'):
    await spoilme(client, message)
  elif message.content.startswith('!trivia') or message.content.startswith('!t'):
    await trivia.do_some_trivia(client, message)
  await crack_a_joke(client, message)

with open("discord.login") as f:
  email = f.readline().rstrip()
  password = f.readline().rstrip()
  client.run(email, password)
