import socket
import telebot

# Dirección IP y puerto del Arduino
HOST = '192.168.100.20'  # IP del Arduino
PORT = 80  # El puerto donde el Arduino está escuchando

#Conexion con nuestro bot

TOKEN = '7973323183:AAFAW-ZcriAk3hvjX_-M_eodurhr6hbKs5Y'
bot = telebot.TeleBot(TOKEN)

#Creacion de Comandos

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Saludos! , Soy el Bot de Telegram Mr.GreenApples , si estas leyendo este mensaje estoy funcionando correctamente :D . \nPara ver mis funciones haz uso del comando \n/help')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Para interactuar conmigo haz uso de los comandos /encender o /apagar , ante cualquier otro mensaje no sere capaz de proporcionarte alguna respuesta')

@bot.message_handler(commands=['encender'])
def send_encender(message):
    
    # Crear el socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))   

        # Enviar datos al Arduino
        mensaje = "1"
        s.sendall(mensaje.encode('utf-8'))  # Enviar el mensaje codificado
    bot.reply_to(message,'El Led esta encendido !')


@bot.message_handler(commands=['apagar'])
def send_apagar(message):
    
    # Crear el socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))   

        # Enviar datos al Arduino
        mensaje = "A"
        s.sendall(mensaje.encode('utf-8'))  # Enviar el mensaje codificado
    bot.reply_to(message,'El Led esta apagado !')


    

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.reply_to(message,'Lo siento no soy capaz de responder ante cualquier mensaje , para mas ayuda utiliza el comando /help')

if __name__ == "__main__":
    bot.polling(none_stop=True)

    