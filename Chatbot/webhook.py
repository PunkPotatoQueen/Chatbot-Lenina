from flask import Flask, request
from telegram import Bot, Update 
from telegram.ext import CommandHandler, MessageHandler, filters, Updater
from Secrets import TOKEN
from pyngrok import ngrok

app = Flask(__name__)


# Configurar o bot do Telegram
bot = Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text('Olá! Bem-vindo ao seu bot local.')

def process_message(update, context):
    # Handle regular messages here if needed
    pass

@app.route('/webhook', methods=['POST'])
def webhook():
    
    update = Update.de_json(request.get_json(force=True), bot)
    dp = bot.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.text & ~filters.command, process_message))
    dp.process_update(update)
    return 'ok'

if __name__ == '__main__':
    # Iniciar o ngrok
    ngrok_tunnel = ngrok.connect(5000)
    print('NGROK URL:', ngrok_tunnel.public_url)

    # Executar a aplicação Flask
    app.run(debug=True)