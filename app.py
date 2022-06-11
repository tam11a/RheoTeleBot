import time
from bot import bot
from telepot.loop import MessageLoop

from handler import on_callback_query, on_chat_message


MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
