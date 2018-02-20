import asyncio
import discord
from discord.ext import commands

description = 'a basic say sound bot'
token = ('Mzk5Mjg4NzQ3MDA0MjY0NDYx.DTK6YA.Z6-pNZTTqTDil3PyzTI9hILGLv4')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description=description)
soundlist = ['그만', '병신', '앙대', '개소리', '지랄', '거짓말', '좋아', '세계']
soundfilename = ['stop', 'idiot', 'no', 'dog', 'retard', 'lie', 'good', 'world']
path = 'E:\\saysoundbot\\sounds\\'
playing = False
debug = False

if not discord.opus.is_loaded():
	# the 'opus' library here is opus.dll on windows
	# or libopus.so on linux in the current directory
	# you should replace this with the location the
	# opus library is located in and with the proper filename.
	# note that on windows this DLL is automatically provided for you
	discord.opus.load_opus('opus')

@bot.event
async def on_ready():
	print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
	channel = bot.get_channel('398896214629941252')
	global voice
	voice = await bot.join_voice_channel(channel)
	await bot.change_presence(game=discord.Game(name='ran🅱om dank 🅱eme soun🅱s'))

@bot.event
async def on_message(message):
	global voice
	global playing
	global soundlist
	global soundfilename
	global debug
	if not message.author == bot.user:
		if message.content.startswith('!debug'):
			if debug:
				debug = False
			else:
				debug = True
			await bot.send_message(message.channel, 'debug mode toggled')
		elif message.content.startswith('!list'):
			await bot.send_message(message.channel, 'all sound list')
			list_out = ''
			temp2 = 0
			for temp in soundlist:
				list_out = list_out + ', ' + temp
				temp2 = temp2 + 1
				if temp2 >=5:
					temp2 = 0
					list_out = list_out + '\n'
			await bot.send_message(message.channel, "```{0}```".format(list_out))
			await asyncio.sleep(10)
			bot.delete_message(message)
		else:
			searchcnt = 0
			for temp3 in soundlist:
				if message.content.startswith(temp3):
					if debug : await bot.send_message(message.channel, 'current temp3 var:' + temp3)
					if not soundfilename[searchcnt] == 'null': temp3 = soundfilename[searchcnt]
					if debug : await bot.send_message(message.channel, 'current temp3 var:' + temp3)
					if not playing:
						if debug : await bot.send_message(message.channel, 'play sound attemp:' + path + temp3 + '.m4a')
						if not voice :
							voice = await bot.join_voice_channel(channel)
							if debug : await bot.send_message(message.channel, 'wasnt connected to voice channel. reconnected.')
						player = voice.create_ffmpeg_player(path + temp3 + '.m4a')
						player.start()
						playing = True
						while player.is_playing():
							await asyncio.sleep(1)
						playing = False
					else:
						await bot.send_message(message.channel, 'sound blocked to prevent earrape. please wait current playing sound to stop.')
					await asyncio.sleep(10)
					bot.delete_message(message)
				searchcnt = searchcnt + 1
bot.run(token)
