import telepot
from bot import bot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Press me', callback_data='press')],
    ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(
        msg, flavor='callback_query')
    articles = [InlineQueryResultArticle(
        id='abc',
        title='ABC',
        input_message_content=InputTextMessageContent(
            message_text='Hello'
        )
    )]

    bot.answerInlineQuery(query_id, articles)
