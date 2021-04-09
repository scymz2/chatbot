from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    'Terminal',
    preprocessors=[
        'chatterbot.preprocessors.clean_symbols'
    ],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'Adapter.weather_adapter.WeatherLogicAdapter'
        },
            'chatterbot.logic.TimeLogicAdapter',
            'chatterbot.logic.MathematicalEvaluation'
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    'chatterbot.corpus.english'
)

# trainer = ListTrainer(bot)
#
# # Train the chat bot with a few responses
# trainer.train([
#     'How can I help you?',
#     'I want to create a chat bot',
#     'Have you read the documentation?',
#     'No, I have not',
#     'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
# ])

print('Type something to begin...')

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
