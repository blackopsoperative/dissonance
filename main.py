# --- Imports. --- #

import discord
import json
import os
from discord.ext import commands, tasks
from fmt import out
from colorama import Fore as c, Style as s
from rich.console import Console

# --- Config load. --- #

with open('boilerplate.conf') as f:
	config = json.load(f)

# --- Constants. --- #

console = Console()
token = config.get('token')
prefix = config.get('prefix')
intents = discord.Intents.all()
boilerplate = commands.Bot(command_prefix=prefix, intents=intents)

# --- Checking if you're retarded. --- #
if token == "PLACE-TOKEN-IN-QUOTES-HERE":
  out.error("You forgot to put your bot\'s token in your configuration file.")
elif prefix == "PLACE-PREFIX-IN-QUOTES-HERE":
  out.error("You forgot to put your bot\'s prefix in your configuration file.")

# --- Events. --- #

@boilerplate.event
async def on_connect():
  out.success("Status: Connected")
  
@boilerplate.event
async def on_ready():
  out.success("Status: Ready")

# --- Loading modules. --- #
for filename in os.listdir(f"./modules"):
	if filename.endswith(".py"):
		try:
			boilerplate.load_extension(f"modules.{filename[:-3]}")
			console.log(f"[green]Module[/green]: {filename} was successfully loaded.")
		except Exception as e:
			console.log(f"[red]Module[/red]: {filename} could not be loaded.\nException: {e}\n---")
			continue
	else:
		continue
    
boilerplate.run(token)
