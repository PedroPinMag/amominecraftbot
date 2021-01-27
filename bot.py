# -*- coding: utf-8 -*-
import tweepy
import time

def executeSomething():
    text_file = open("palavras.txt", "r")  # Abrimos a lista de palavras
    palavras = text_file.readlines()  # E convertemos numa lista

    text_file = open("palavras.txt", "r")  # Abrimos a lista de palavras
    palavras = text_file.readlines()  # E convertemos numa lista

    consumer_secret = ""
    consumer_key = ""  # Credencias do twitter dev
    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)  # Logando

    numero = int(palavras[0])  # A palavra atual esta salvo no indice 0 da lista

    texto = ""

    if str(palavras[numero])[0] == '0':
        texto = palavras[numero][1].lower() + "... " + "Ama Minecraft "
        # Algumas palavras não podem ser chingadas, marcamos elas com um 0
        # O bot so vai postar a primeira letra delas

    else:
        texto = palavras[numero].lower() + "Ama Minecraft "
        print(texto)
        # Caso não seja uma palavra marcada o bot manda ela se foder msm

    api.update_status(status=texto)  # Então postamos no twitter o texto gerado

    palavras[0] = str(numero + 1) + '\n'  # Incrementos o contador

    with open('palavras.txt', 'w') as file:
        file.writelines(palavras)  # E salvamos devolta no arquivo

    time.sleep(1800)

while True:
    executeSomething()
