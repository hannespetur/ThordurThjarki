#!/usr/bin/env python3
import sys

async def kill_bot(client, message, name):
  bots_to_kill = message.content[5:].rstrip().lower().split(" ")

  if name.lower() in bots_to_kill:
    if name.lower() == "prime":
      await client.send_message(message.channel, "The decepticons win! :(")

    sys.exit(0)
