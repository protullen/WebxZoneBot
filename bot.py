from pyrogram import Client, filters, enums
from os import environ

api_id = environ.get('API_ID')
api_hash = environ.get('API_HASH')
bot_token = environ.get('BOT_TOKEN')
chat_id = int(environ.get('TO_CHAT'))
from_chat_id = int(environ.get('FROM_CHAT'))

webxzonebot = Client(    
    name='webxzonebot',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@webxzonebot.on_message(filters.channel & filters.group)
async def forward(bot, message):
    try:
        await bot.copy_message(
            chat_id = chat_id,
            from_chat_id = from_chat_id,
            caption = f'**{message.caption}**',
            message_id = message.id,
            parde_mode = enums.ParseMode.MARKDOWN            
        )
    except Exception as e:
        print(f'{e}')

print('Bot Started!')
webxzonebot.run()
