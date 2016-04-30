#!/usr/bin/env python3
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
  if number == 2:
    return True

  if number <= 1 or number % 2 == 0:
    return False

  i = 3
  while i*i <= number:
    if number % i == 0:
      return False

    i += 2

  return True

async def check_for_prime(client, message):
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
