import telebot
import feedparser
import time

CHAVE_API = "5673118044:AAGUkRNwBIUp_lkTe2EJfnMhxfF1usZzUEw"
bot = telebot.TeleBot(CHAVE_API)

# URL do RSS
URL_RSS = "https://rss.app/feeds/UHtXRmOdmZq2Ys5J.xml"

# Limite de notícias a serem enviadas
LIMITE_NOTICIAS = 1

# ID do chat onde as notícias serão enviadas
CHAT_ID = -1001808334431

# Data da última notícia enviada
ultima_noticia = None

while True:
    try:
        print("Executando...")
        # Lê as notícias do feed
        feed = feedparser.parse(URL_RSS)

        # Contador de notícias
        contador = 0

        # Envia cada notícia para o usuário
        for noticia in feed["entries"]:
            # Verifica se a data da notícia é posterior à da última notícia enviada
            if ultima_noticia is not None and noticia["published_parsed"] <= ultima_noticia:
                continue
            # Verifica se o limite foi atingido
            if contador >= LIMITE_NOTICIAS:
                break
            # Concatena as informações da notícia
            texto = f"{noticia['title']}\n\n{noticia['link']}"
            bot.send_message(CHAT_ID, texto)
            # Atualiza a data da última notícia enviada
            ultima_noticia = noticia["published_parsed"]
            contador += 1
    except Exception as e:
        # Imprime qualquer exceção que ocorra
        print(e)

        # Delay de 60 segundos
    time.sleep(300)