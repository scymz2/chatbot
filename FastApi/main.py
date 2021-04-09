from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# server
from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn
from pydantic import BaseModel
app = FastAPI()

# Create a new instance of a ChatBot
bot = ChatBot(
    'Norman',
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        {'import_path': 'weather_adapter.WeatherLogicAdapter'}
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    'chatterbot.corpus.english',
    'chatterbot.corpus.chinese'
)



# 这个接口现在是用来从外部导入对话列表来训练的，但是我准备用它来返回用户报告的情况
@app.post("/training")
async def training(uselessKey: str = None, dialogue: list=[]):
    if uselessKey != 'nnnnnnnnnn':
        return JSONResponse(status_code=403, content='403 Forbidden')
    conversation = dialogue
    trainer = ListTrainer(bot)
    trainer.train(conversation)
    return {"code": "200"}


@app.get("/talking")
async def talking(key: str = None, ask: str = 'hi!'):
    if key != 'admin':
        return JSONResponse(status_code=403, content='403 Forbidden')
    response = bot.get_response(ask)
    print(response)
    return {'response': str(response)}


# print('Type something to begin...')
# def r(s):return bot.get_response(s).text
# # The following loop will execute each time the user enters input
# while True:
#     try:
#       i = input('>>> ').strip()
#       if i != 'exit':
#         print(r(i))
#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break
