import telebot

import requests
from bs4 import BeautifulSoup
from Secrets import TOKEN
from Metodos import Start_txt, email_text, Menu_text, FAQ_text, base_Text, Curso_text, help_Text, devs_text

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def Inicio(mensagem):
    bot.set_chat_menu_button()
    bot.send_message(mensagem.chat.id, Start_txt)

@bot.message_handler(commands=["menu"])
def Inicio(mensagem):
    bot.send_message(mensagem.chat.id, Menu_text)

@bot.message_handler(commands=["horario"])
def Curso(mensagem):
    bot.send_message(mensagem.chat.id, Curso_text)

@bot.message_handler(commands=["computacao", "automacao", "quimica", "hidrica"])
def resposta(mensagem):
    bot.send_message(mensagem.chat.id, "https://drive.google.com/file/d/1NxgAicFzdM_369I5u6ExakDXoe_Luyit/view?usp=sharing")
    bot.send_message(mensagem.chat.id, "É só baixar, se quiser pode voltar ao /menu")

@bot.message_handler(commands=["UABJ"])
def site(mensagem):
    bot.send_photo(mensagem.chat.id, "https://www.bj1.com.br/wp-content/uploads/2022/03/UABJ.jpeg")
    bot.send_message(mensagem.chat.id, "http://www.uabj.ufrpe.br")
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /menu")

@bot.message_handler(commands=["emails"])
def atalho(mensagem):
    bot.send_message(mensagem.chat.id, email_text)
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /start")

@bot.message_handler(commands=["help"])
def ajuda(mensagem):
    bot.send_message(mensagem.chat.id, help_Text)


@bot.message_handler(commands=["FAQ"])
def perguntas(mensagem):
    bot.send_message(mensagem.chat.id, FAQ_text)

@bot.message_handler(commands=["devs"])
def dev(mensagem):
    bot.send_message(mensagem.chat.id, devs_text)

@bot.message_handler(commands=['bolsas'])
def webtal(msg):

    url = 'https://www.prg.unicamp.br/graduacao/pad/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='elementor-text-editor elementor-clearfix')
    headlines = []

    for article in articles:
        headline_element = article.find('p')   # Selecionando cada elemento <p> naquela div
        if headline_element is not None:
            headline = headline_element.text.strip() + "\n"
            headlines.append({'headline': headline, })

    message = 'Essas são as ultimas informações que se tem sobre bolsas no nosso site:\n\n'
    message_chunks = []
    for headline in headlines:

        message_chunk = f'- {headline["headline"]}\n'
        if len(message + message_chunk) > 4000:    #tratamento para textos que excedam o limite de characteres do telegram
            message_chunks.append(message)
            message = 'informações sobre bolsas (continuação):\n\n'
        message += message_chunk
        
    message_chunks.append(message)
    for message_chunk in message_chunks:
        text = f'{message_chunk }'
        bot.send_message(msg.chat.id, text)


#________________ INTEGRAÇÃO COM O SITE PARA ALUNOS _________________________
@bot.message_handler(commands=["Sugestao"])
def enviar_sugestao(mensagem):
    faq_link = "http://127.0.0.1:5000/index_aluno"  # Substitua pelo endereço correto do FAQ
    bot.send_message(mensagem.chat.id, f"Para enviar uma sugestão, acesse o FAQ através deste link: {faq_link}")
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser voltar, é só clicar no /menu")

bot.polling()

bot.polling()

# @bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
# def conferir(mensagem):
#     bot.send_message(mensagem.chat.id, base_Text)