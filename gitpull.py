import git

async def gitpull(client, message):
  g = git.cmd.Git()
  g.pull()
  await client.send_message(message.channel, "Latest changes have been pull from git.")