from pyrogram import Client, filters, enums
from os import environ

app_id = int(environ.get('API_ID'))
api_hash = environ.get('API_HASH')
bot_token = environ.get('BOT_TOKEN')
chat_id = int(environ.get('TO_CHAT'))
from_chat_id = int(environ.get('FROM_CHAT'))

webxzonebot = Client(    
    name='webxzonebot',
    api_id=app_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@webxzonebot.on_message(filters.channel)
async def forward(bot, message):
    try:
        await bot.copy_message(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            caption=f'**{message.caption}**',
            message_id=message.id,
            parse_mode=enums.ParseMode.MARKDOWN            
        )
    except Exception as e:
        print(f'{e}')

@webxzonebot.on_message(filters.command('start') & filters.user(5163706369))
async def start(bot, message):
    await message.reply('Alive')

print('Bot Started!')
webxzonebot.run()
