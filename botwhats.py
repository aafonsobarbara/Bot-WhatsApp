from selenium import webdriver
import time
from time import sleep
from datetime import datetime, timedelta, date

# PROGRAMAR O HORÁRIO QUE VAI ENVIAR A MENSAGEM
horaAtual = datetime.now() 
# HORARIO ATUAL + QNT TEMPO VC QUER QUE ESPERE
horario = horaAtual + timedelta(seconds=30)
horario = horario.strftime('%d/%m/%Y %H:%M')


class WhatsappBot:
    def __init__(self):
        self.message = "mensagem"
        self.chats = ["CHATS"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    #abrir o WhatsApp
    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        #verificando se está na hora de mandar a mensagem
        while True:
            hrs = datetime.now()
            hrs = hrs.strftime('%d/%m/%Y %H:%M')
            if (hrs == horario):
                break

        #mandando a mensagem    
        for person in self.chats:
            person = self.driver.find_element_by_xpath(
                f"//span[@title='{person}']")
            time.sleep(3)
            person.click()
            chatBox = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chatBox.click()
            chatBox.send_keys(self.message)
            sendButton = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(2)
            sendButton.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
