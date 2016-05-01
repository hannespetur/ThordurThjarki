#!/usr/bin/env python3
import asyncio
import csv
import random

class Trivia:
	def __init__(self):
		self.questions = []
		self.discord = []
		self.channel = []

		# Game states
		self.gamequestions = []
		self.state = 'gameover'
		self.players = {}
		self.questionNr = 0

	async def send(self, text):
		await self.discord.send_message(self.channel, text)

	def reset(self):
		self.gamequestions = []
		self.state = 'gameover'
		self.players = {}
		self.questionNr = 0

	async def answer(self, client, message, answer):
		await client.delete_message(message)
		if self.state == 'answering':
			score = 0
			if self.gamequestions[self.questionNr][answer] == self.gamequestions[self.questionNr]['Answer']:
				score = 1
			else:
				score = 0

			if len(self.players[message.author.id]['answers']) > self.questionNr:
				self.players[message.author.id]['answers'][self.questionNr] = score
			else:
				self.players[message.author.id]['answers'].append(score)
			print(self.players[message.author.id]['answers'])

	async def load_questions(self):
		if len(self.questions) == 0:
			with open('triviaquestions.csv') as csvfile:
				reader = csv.DictReader(csvfile, delimiter=';')
				for row in reader:
					self.questions.append(row)
		self.gamequestions = random.sample(self.questions, 7)

	async def end_game(self):
		print('end game')
		await self.send('Game Over. Score Lists:')
		for player in sorted(self.players.values(), key=lambda p: sum(p['answers']), reverse=True):
			print(player)
			await self.send('{0}: {1} points'.format(player['displayname'], sum(player['answers'])))
		await self.send("Thank you for playing.")
		self.reset()

	async def next_question(self):
		print('next question')
		if self.questionNr >= len(self.gamequestions):
			await self.end_game()
		else:
			self.state = 'answering'
			q = self.gamequestions[self.questionNr]
			await self.send("Question number {}:".format(self.questionNr +1))
			await asyncio.sleep(1)
			await self.send(q['Question'])
			await self.send("a) {}".format(q['a'].strip()))
			await self.send("b) {}".format(q['b'].strip()))
			await self.send("c) {}".format(q['c'].strip()))
			await self.send("d) {}".format(q['d'].strip()))
			await asyncio.sleep(10)

			self.state = 'starting'
			await self.send("Correct answer is: {}".format(q['Explanation']))
			# set unanswered
			for player in self.players.values():
				if len(player['answers']) <= self.questionNr:
					player['answers'].append(0)

			self.questionNr = self.questionNr + 1
			await self.next_question()

	async def join(self, client, message):
		if self.state != 'waiting':
			await client.send_message(message.channel, "Game in progress or not started")
		else:
			self.players[message.author.id] = {'id': message.author.id, 'name':message.author.name, 'displayname':message.author.display_name, 'user':message.author, 'answers':[]}
			await self.send("{0} joined the game".format(str(message.author.display_name)))

	async def start_game(self, client, message, command):
		if self.state != 'gameover':
			await client.send_message(message.channel, "Can't start a game that is in progress")
			return
		else:
			self.state = 'waiting'

		self.discord = client
		self.channel = message.channel

		await self.send("Starting the trivia ... You have 15 seconds to join the game using \"!trivia join\"")
		await asyncio.sleep(10)
		await self.send("5 seconds until game starts. {} players have joined.".format(len(self.players)))
		await asyncio.sleep(5)

		if(len(self.players) == 0):
			self.reset()
			await self.send("No players joined. Game Over. Enter !trivia start to start a new game")
		else:
			self.state = 'starting'
			await self.send("Starting game with {} players. 7 questions. 10 seconds per question. Answer by typing \"!t a\", \"!t b\", \"!t c\" or \"!t d\"".format(len(self.players)))
			await asyncio.sleep(2)
			await self.load_questions()
			await self.next_question()

	async def show_help(self, client, message):
		await client.send_message(message.channel, """
			trivia [?/help] -- displays available commands
			trivia start -- start a new trivia game
			trivia join -- join a trivia game
			trivia [a/b/c/d] -- answer a question
			""") 

	async def do_some_trivia(self, client, message):
		try:
			print(str(message.content))
			if message.channel.is_private == True or 'trivia' not in message.channel.name:
				await client.send_message(message.channel, "You can only play in the trivia channel")
				return
			if message.content.startswith('!trivia'):
				commands = message.content[7:].strip().split(' ', 1)
			else:				
				commands = message.content[2:].strip().split(' ', 1)
			if len(commands) == 0:
				command = '?'
			else:
				command = commands[0].strip().lower()

			if len(command) == 0 or command.startswith('?') or command.lower().startswith("help"):
				await self.show_help(client, message)
			elif command.startswith('start'):
				await self.start_game(client, message, command)
			elif command.startswith('join'):
				await self.join(client, message)
			elif command.startswith('test'):
				await self.load_questions()
			elif command == 'a' or command == 'b' or command == 'c' or command == 'd':
				await self.answer(client, message, command)
			else:
				await client.send_message(message.channel, "Option {0} is not a supported command. Use help for list of options".format(command))
		except BaseException as e:
			print(str(e))
			await client.send_message(message.channel, "I failed, something went wrong")