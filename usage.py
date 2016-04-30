#!/usr/bin/env python3

# I have inserted one whitspace before each command to ensure that the new message does not trigger a infinite recursion!
EIGHT_BALL_USAGE = " !8ball <question> predicts the outcome of a question."
GIT_PULL_USAGE = " !gitpull pulls the latest files from git."
HELP_USAGE = " !help [cmd] or !usage [cmd] outputs help for command or all commands if no command was given."
KILL_USAGE = " !kill <bot1> [bot2]... kills a list of bots (or restarts them if they are running in daemon mode)."
PRIME_USAGE = " !prime <number> determines if the given number is a prime number or not."
SPOIL_ME_USAGE = " !spoilme outputs a movie spoiler."

LIST_OF_USAGES = [
  EIGHT_BALL_USAGE,
  GIT_PULL_USAGE,
  HELP_USAGE,
  KILL_USAGE,
  PRIME_USAGE,
  SPOIL_ME_USAGE
]

async def print_usage(client, message):
  split_msg = message.content.lower().rstrip().split(" ")

  if len(split_msg) == 2:
    if split_msg[1] == "8ball":
      await client.send_message(message.channel, EIGHT_BALL_USAGE)
    elif split_msg[1] == "help" or split_msg[1] == "usage":
      await client.send_message(message.channel, HELP_USAGE)
    elif split_msg[1] == "gitpull":
      await client.send_message(message.channel, GIT_PULL_USAGE)
    elif split_msg[1] == "kill":
      await client.send_message(message.channel, KILL_USAGE)
    elif split_msg[1] == "prime":
      await client.send_message(message.channel, PRIME_USAGE)
    elif split_msg[1] == "spoilme":
      await client.send_message(message.channel, SPOIL_ME_USAGE)
    else:
      await client.send_message(message.channel, "\n".join(LIST_OF_USAGES))
  else:
    await client.send_message(message.channel, "\n".join(LIST_OF_USAGES))
