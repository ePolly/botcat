import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import datetime
import time
from PIL import Image, ImageDraw, ImageFont
# настроим модуль ведения журнала логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
table={}
# определяем асинхронную функцию
async def start(update, context):
    # ожидание отправки сообщения по сети - нужен `await`
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    img = Image.open('img.png')
    d1 = ImageDraw.Draw(img)
    # Decide the text location, color and font

    font = ImageFont.truetype("arial.ttf", 40)
    d1.text((65, 10), time_string, fill=(255, 0, 0), font=font)
    # show and save the image
    # img.show()
    img.save("result.png")
    photo = open('result.png', 'rb')
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                   photo=photo)

    chat_id = update.message.chat_id
    username = update.message.chat.username


    table[username]=time_string
    print(table)
if __name__ == '__main__':
    TOKEN = ''
    # создание экземпляра бота через `ApplicationBuilder`
    application = ApplicationBuilder().token(TOKEN).build()

    # создаем обработчик для команды '/start'
    start_handler = CommandHandler('start', start)
    # регистрируем обработчик в приложение
    application.add_handler(start_handler)
    # запускаем приложение
    application.run_polling()