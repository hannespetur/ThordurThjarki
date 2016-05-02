import os
import subprocess

async def gitpull(client, message):
  local_dir = str(os.path.dirname(os.path.realpath(__file__)))
  await client.send_message(message.channel, "Starting to pull changes from Github...")
  proc = subprocess.Popen(["git", "pull"], shell=True, cwd=local_dir, stdout=subprocess.PIPE)
  await client.send_message(message.channel, "Latest changes have been pull from git.")
