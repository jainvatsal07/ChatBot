from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')

trainer = ListTrainer(bot)

trainer.train([
	'Hi',
	'Hello',
	'I have a query.',
	'Please elaborate, your concern',
	'How long it will take to become expert in Coding ?',
	'It usually depends on the amount of practice.',
	'Ok Thanks',
	'No Problem! Have a Good Day!'
])

while True:
	request=input('you :')
	if request == 'OK' or request == 'ok':
		print('Bot: bye')
		break
	else:
		response=bot.get_response(request)
		print('Bot:', response)

