import progress.bar as pb
import time
import os
from art import tprint
from colorama import init, Style, Fore
import tabulate
from faker import Faker
import wget
import pygame
import random
import json


pygame.mixer.init()
pygame.init()

fake = Faker("RU_ru")

Name = os.getlogin()

init()

pygame.mixer.music.load("system.mp3")
pygame.mixer.music.play(-1)

sound_order = pygame.mixer.Sound('order.mp3')


def startsearch():
    os.system('cls||clear')

    random_name = fake.name()
    random_prise = random.randint(950, 2850)

    barsearchone = pb.ChargingBar("Находим подходящий заказ...")
    for i in range(100):
        barsearchone.next()
        time.sleep(0.02)
    barsearchone.finish()
    os.system('cls||clear')
    barsearchtwo = pb.ChargingBar("Находим более точный заказ...")
    for i in range(100):
        barsearchtwo.next()
        time.sleep(0.01)
    barsearchtwo.finish()
    os.system('cls||clear')
    barsearchthree = pb.ChargingBar("Почти готово...")
    for i in range(100):
        barsearchthree.next()
        time.sleep(0.007)
    barsearchthree.finish()

    sound_order.play()

    os.system('cls||clear')

    print("      Заказ добавлен на LonelyKitty")



    data = {'name': random_name, 'prise': random_prise, 'relevance': True}

    with open('data.json', 'w') as file:
        json.dump(data, file)

    a = input("$ ")
    startnet()


def startinfo():
    os.system('cls||clear')

    with open('info.json', 'r') as json_file:
        info = json.load(json_file)
        comp_order = info['completed_orders']

    print(Fore.RED + "        Ваш профиль:" + Style.RESET_ALL)
    print(f"Ваш ник: {Name}")
    print(f"Выполнено заказов: {comp_order}")
    print(Fore.GREEN + "               ..." + Style.RESET_ALL)

    a = input("$ ")
    startnet()

def startfeedback():
    os.system('cls||clear')




def startnet():
    os.system('cls||clear')
    tprint("RuHNet")
    a = input("$ ")
    if a == "search":
        startsearch()
    elif a == "info":
        startinfo()
    elif a =="feedback":
        startmyaccount()
    else:
        print("Неккоректно")
        time.sleep(0.5)
        startnet()

startnet()
