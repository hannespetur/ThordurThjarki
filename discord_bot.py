#!/usr/bin/env python3
import discord
import asyncio
import random


LOW_NUMBER_INSULTS = [
  "Your IQ",
  "Your swag level",
  "Your Facebook friend count",
  "Your bank account balance",
  "Your life expectancy",
  "Your salaries",
  "Your Twitter follower count",
  "Your maximum bench press weight"
]

HIGH_NUMBER_INSULTS = [
  "Yo' mama's weight",
  "Your BMI",
  "Your ego level",
  "Your weight",
  "Your golf handicap",
  "The age of your virginity loss"
]


def is_prime(number):
  if number <= 1 or number == 4 or number == 6 or number == 8:
    return False

  i = 3
  while i*i <= number:
    if number % i == 0:
      return False

    i += 2

  return True


client = discord.Client()

@client.event
async def on_ready():
  print ('Logged in as')
  print (client.user.name)
  print (client.user.id)
  print ('------')

@client.event
async def on_message(message):
  if message.content.startswith('!prime'):
    try:
      number = int(message.content[6:].strip())

      if number == 42:
        await client.send_message(message.channel, "This is the answer to life, the universe, and everything.")
        
      elif is_prime(number):
        if number <= 40:
          await client.send_message(message.channel, "Yes. {} is a prime number.".format(random.choice(LOW_NUMBER_INSULTS)))
        elif number > 150:
          await client.send_message(message.channel, "Yes. {} is a prime number.".format(random.choice(HIGH_NUMBER_INSULTS)))
        else:
          await client.send_message(message.channel, "Yes. {} is a prime number.".format(number))
      else:
        if number <= 40:
          await client.send_message(message.channel, "No. {} is not a prime number.".format(random.choice(LOW_NUMBER_INSULTS)))
        elif number > 150:
          await client.send_message(message.channel, "No. {} is not a prime number.".format(random.choice(HIGH_NUMBER_INSULTS)))
        else:
          await client.send_message(message.channel, "No. {} is not a prime number.".format(number))
    except:
      await client.send_message(message.channel, "Who taught you to type?")


with open(".discord_login") as f:
  email = f.readline().rstrip()
  password = f.readline().rstrip()
  client.run(email, password)
