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

init()

pygame.mixer.music.load("AltBankRofl.mp3")
pygame.mixer.music.play(-1)

fake = Faker("RU")

Name = os.getlogin()


def startmoneybox():
    os.system('cls||clear')
    tprint("Alt   Bank")


    with open('info.json', 'r') as json_file:
        info = json.load(json_file)
        money = info['money']

    with open('arrears.json', 'r') as json_file:
        arrears = json.load(json_file)
        studies = arrears['studies']
        paul = arrears['paul']
        food = arrears['food']
        rent = arrears['rent']
        payment_studies = arrears['payment_studies']
        payment_paul = arrears['payment_paul']
        payment_food = arrears['payment_food']
        payment_rent = arrears['payment_rent']


    print(Fore.RED + "        Ваши накопительные счета:" + Style.RESET_ALL)
    print(f"      Обучение: {studies}₽/{payment_studies}₽")
    print(f"      Павел: {paul}₽/{payment_paul}₽")
    print(f"      Еда: {food}₽/{payment_food}₽")
    print(f"      Квартплата: {rent}₽/{payment_rent}₽")
    print(Fore.GREEN + "               ..." + Style.RESET_ALL)

    a = input("$ ")
    startbank()



def startbalance():
    os.system('cls||clear')
    tprint("Alt   Bank")
    print("")
    with open('info.json', 'r') as json_file:
        info = json.load(json_file)
        money = info['money']
    print(f"Кошелек: {money}₽")
    print("")
    a = input("$ ")
    startbank()


def startbank():
    os.system('cls||clear')
    tprint("Alt   Bank")
    random_num = random.randint(0, 16)
    if random_num == 0:
        print(Fore.YELLOW +"        Выгодные микрозаймы по всей России!" + Style.RESET_ALL)
    elif random_num == 1:
        print(Fore.YELLOW +"        Банк, которому доверяют" + Style.RESET_ALL)
    elif random_num == 2:
        print(Fore.YELLOW +"        Мы приумножим ваши деньги" + Style.RESET_ALL)
    elif random_num == 3:
        print(Fore.RED +"       Основан за 2 года до н.э." + Style.RESET_ALL)
    elif random_num == 4:
        print(Fore.YELLOW +"        Лето без процентов" + Style.RESET_ALL)
    elif random_num == 5:
        print(Fore.YELLOW +"        С ALT-картой не за что краснеть!" + Style.RESET_ALL)
    elif random_num == 6:
        print(Fore.RED +"       Самые невыгодные кредиты, только у нас" + Style.RESET_ALL)
    elif random_num == 7:
        print(Fore.RED +"       Карта возможностей" + Style.RESET_ALL)
    elif random_num == 8:
        print(Fore.YELLOW +"        Всё получится!" + Style.RESET_ALL)
    elif random_num == 9:
        print(Fore.YELLOW +"        Большое преимущество" + Style.RESET_ALL)
    elif random_num == 10:
        print(Fore.YELLOW +"        Одна подписка — много возможностей" + Style.RESET_ALL)
    elif random_num == 11:
        print(Fore.YELLOW +"        ALT.Всегда рядом!" + Style.RESET_ALL)
    elif random_num == 12:
        print(Fore.YELLOW +"        Он такой один" + Style.RESET_ALL)
    elif random_num == 13:
        print(Fore.RED +"       Честным быть выгодно" + Style.RESET_ALL)
    elif random_num == 14:
        print(Fore.RED +"       Возьмите кредит, дальше будем действовать мы" + Style.RESET_ALL)
    elif random_num == 15:
        print(Fore.RED +"       Самые быстрые коллекторы" + Style.RESET_ALL)
    elif random_num == 16:
        print(Fore.YELLOW + f"      Доброй ночи{Name}" + Style.RESET_ALL)


    print("")
    print("")
    a = input("$ ")
    if a == "balance":
        startbalance()
    elif a == "moneybox":
        startmoneybox()
    elif a =="feedback":
        startmyaccount()
    else:
        print("Неккоректно")
        time.sleep(0.5)
        startbank()

startbank()
