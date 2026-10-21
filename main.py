import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "سلام رفیق 💜 خوش اومدی به گروه Lithium!")

bot.infinity_polling()
