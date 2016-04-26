#!/usr/bin/env python3
import discord
import asyncio
import random

async def crack_a_joke(client, message):
  if "á morgun" in message.content:
    await client.send_message(message.channel, "Á morgun segir sá lati :)")
  elif "talva" in message.content:
    await client.send_message(message.channel, "*tölva")