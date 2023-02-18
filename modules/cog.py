# --- Imports. --- #

import discord
from discord.ext import commands, tasks
from rich.console import Console

# --- Constants. --- #

console = Console()

# --- Module code itself. --- #

class Cog(commands.Cog):
	def __init__(self, boilerplate):
		self.boilerplate = boilerplate


	@commands.command(help="Pings the bot and returns latency.", usage='')
	async def ping(self, ctx):
		await ctx.reply(f"Pong, {round(self.boilerplate.latency, 1)}ms.", mention_author=False)

# --- Setup. --- #

def setup(boilerplate):
	boilerplate.add_cog(Cog(boilerplate))
	console.log(f"{__file__} loaded.")

def teardown(boilerplate):
	console.log(f"{__file__} unloaded.")
