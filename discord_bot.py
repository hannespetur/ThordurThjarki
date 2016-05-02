#!/usr/bin/env python3
import discord
import sys
from usage import print_usage
from prime import check_for_prime
from eightball import ask8ball
from spoilme import spoilme
from kill import kill_bot
from wisecracker import crack_a_joke
from trivia import Trivia
from gitpull import gitpull

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
  if message.content.startswith('!8ball'):
    await ask8ball(client, message)
  elif message.content.startswith("!gitpull"):
    await gitpull(client, message)
  elif message.content.startswith('!help') or message.content.startswith('!usage'):
    await print_usage(client, message)
  elif message.content.startswith('!kill'):
    await kill_bot(client, message, client.user.name)
  elif message.content.startswith('!prime'):
    await check_for_prime(client, message)
  elif message.content.startswith('!spoilme'):
    await spoilme(client, message)
  elif message.content.startswith('!trivia') or message.content.startswith('!t'):
    await trivia.do_some_trivia(client, message)
  await crack_a_joke(client, message)


login_file = "discord.login"

if len(sys.argv) == 2:
  login_file = str(sys.argv[1])

with open(login_file) as f:
  email = f.readline().rstrip()
  password = f.readline().rstrip()
  client.run(email, password)
