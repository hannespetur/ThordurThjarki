#!/usr/bin/env python3
import discord
import asyncio
import random
import time
import traceback

EIGHTBALLANSWERS = [
"It is certain",
"It is decidedly so",
"Without a doubt",
"Yes, definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful",
"Yes, in due time.",
"My sources say no.",
"Definitely not.",
"Yes.",
"You will have to wait.",
"I have my doubts.",
"Outlook so so.",
"Looks good to me!",
"Who knows?",
"Looking good!",
"Probably.",
"Are you kidding?",
"Go for it!",
"Don't bet on it.",
"Forget about it."]

async def ask8ball(client, message):
  try:
	  question = str(message.content[6:].strip())
	  await client.send_message(message.channel, "The magic 8-Ball is thinking...")
	  time.sleep(2)
	  await client.send_message(message.channel, "...")
	  time.sleep(3)
	  await client.send_message(message.channel, "{}: {}".format(question, random.choice((EIGHTBALLANSWERS))))
  except err:
    print(err)
    await client.send_message(message.channel, "The magic 8-Ball doesn't understand your question!")