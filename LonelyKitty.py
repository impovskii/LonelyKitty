import progress.bar as pb
import time
import os
from art import tprint
from colorama import init, Style, Fore
from simple_term_menu import TerminalMenu
import tabulate
from faker import Faker
import wget
import pygame
import random
import json

pygame.mixer.init()
pygame.init()

init()

pygame.mixer.music.load("system.mp3")
pygame.mixer.music.play(-1)

fake = Faker("RU")

url_img = "https://i.pinimg.com/564x/18/88/2d/18882de68a593383dfdc20b3eef1adc0.jpg"

sound_error = pygame.mixer.Sound('error2.mp3')
sound_sell = pygame.mixer.Sound('sell.mp3')


coin = 0
data = 0


cat1 = " |\_/|"
cat2 = "( o.o )"
cat3 = " > ^ <"

deadcat1 = " |\_/|"
deadcat2 = "( x.x )"
deadcat3 = " > ^ <"

deadtext = "почему, за что, почему?"

os.system('cls||clear')

Name = os.getlogin()

def starthack():
    os.system('cls||clear')
    random_time = random.uniform(0, 1)
    bar8 = pb.ChargingBar("Собираем персональные данные")
    for i in range(100):
        bar8.next()
        time.sleep(random_time)
    bar8.finish()
    print("Персональные данные сохраннены")
    global data
    data = data + 1
    with open('PersonalData/data.txt', 'a+') as file:
        file.write(fake.name() + "\n")
        file.write(fake.address() + "\n")
    file.close()
    a = input("$ ")
    console()


def starthackeasy():
    os.system('cls||clear')
    bar999 = pb.ChargingBar("Собираем персональные данные")
    for i in range(100):
        bar999.next()
        time.sleep(0.001)
    bar999.finish()
    print("Персональные данные сохранены")
    global coin
    coin = coin + 1
    global data
    data = data + 1
    with open('PersonalData/data.txt', 'a+') as file:
        file.write(fake.name() + "\n")
        file.write(fake.address() + "\n")
    file.close()
    a = input("$ ")
    console()

    
def startrping():
    os.system('cls||clear')

    bar6 = pb.ChargingBar("Загрузка...", max=100)
    for i in range(100):
        bar6.next()
        time.sleep(0.09)
    bar6.finish()
    print("libary ~$euphoria", Fore.GREEN + "[True]" + Style.RESET_ALL)

    bar7 = pb.ChargingBar("Загрузка...", max=100)
    for i in range(100):
        bar7.next()
        time.sleep(0.06)
    bar7.finish()
    print("libary ~$grid", Fore.GREEN + "[True]" + Style.RESET_ALL)
    furst_file = open("ОткройМеня.txt", "w+")
    furst_file.write(cat1 + "\n")
    furst_file.write(cat2 + "\n")
    furst_file.write(cat3 + "\n")
    furst_file.close()

    print("")
    a = input("Чтобы продолжить нажмите Enter ")
    os.system('cls||clear')
    print("Ты справился!")
    time.sleep(1)
    print("Это было легко, правда?")
    time.sleep(1)
    console()

def money():
     os.system("cls||clear")
     print(f"У тебя {coin} рублей!")
     a = input("$ ")
     console()


def startdata():
    os.system("cls||clear")
    print(f"Количество персональных данных: {data} ")
    a = input("$ ")
    console()


def startsell():
    os.system("cls||clear")

    barsell = pb.ChargingBar("Продаем...", max=100)
    for i in range(100):
        barsell.next()
        time.sleep(0.05)
    barsell.finish()

    print("~$sell", Fore.GREEN + "[True]" + Style.RESET_ALL)
    sound_sell.play()

    os.remove('PersonalData/data.txt')
    random_coin = random.randint(150, 423)
    global coin
    coin = coin + random_coin
    global data
    data = 0

    a = input("$ ")
    console()


def startorder():
    os.system("cls||clear")
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        order_name = data['name']
        order_prise = data['prise']
        order_relevance = data['relevance']

    if order_relevance == True:
        print(Fore.RED + "        Информация о заказе:" + Style.RESET_ALL)
        print(f"ФИО жертвы: {order_name}")
        print(f"Цена заказа: {order_prise}₽")
        print(Fore.GREEN + "               Активно" + Style.RESET_ALL)
    else:
        print("У вас нету активных заказов!")

    a = input("$ ")
    console()


def startorderhack():
    os.system('cls||clear')

    random_num_one = random.randint(1, 9)
    random_num_two = random.randint(1, 9)
    random_num_three = random.randint(1, 9)
    random_num_four = random.randint(1, 9)
    random_num_five = random.randint(1, 9)
    random_num_six = random.randint(1, 9)
    random_num_seven = random.randint(1, 9)
    random_num_eight = random.randint(1, 9)
    random_num_nine = random.randint(1, 9)

    print("autohack")
    print("")
    print(f"+7 (9{random_num_one}{random_num_two}) {random_num_three}{random_num_four}{random_num_five} {random_num_six}{random_num_seven} {random_num_eight}{random_num_nine}")

    a = input("$ ")
    console()


def console():
    os.system("cls||clear")

    tprint("Lonely kitty")
    print("")
    a = input("$ ")
    if a == "ping":
        startping()
    elif a == "r_ping":
        startrping()
    elif a == "hack":
        starthack()
    elif a == "hackeasy":
        starthackeasy()
    elif a == "money":
        money()
    elif a == "data":
        startdata()
    elif a == "sell":
        startsell()
    elif a == "order":
        startorder()
    elif a == "orderhack":
        startorderhack()
    else: 
        print("Неккоректно")
        time.sleep(0.5)
        console()
        


def startping():
    os.system('cls||clear')

    bar1 = pb.ChargingBar("Загрузка...", max=100)
    for i in range(100):
        bar1.next()
        time.sleep(0.05)
    bar1.finish()
    print("libary ~$commands", Fore.GREEN + "[True]" + Style.RESET_ALL)

    bar2 = pb.ChargingBar("Загрузка...", max=100)
    for i in range(100):
        bar2.next()
        time.sleep(0.03)
    bar2.finish()
    print("libary ~$particles", Fore.GREEN + "[True]" + Style.RESET_ALL)

    bar3 = pb.ChargingBar("Загрузка...", max=100)
    for i in range(100):
        bar3.next()
        time.sleep(0.06)
    bar3.finish()
    sound_error.play()
    print("libary ~$euphoria", Fore.RED + "[False]" + Style.RESET_ALL)

    bar4 = pb.ChargingBar("Загрузка...", max=100)
    for i in range(100):
        bar4.next()
        time.sleep(0.02)
    bar4.finish()
    print("libary ~$flexbox", Fore.GREEN + "[True]" + Style.RESET_ALL)

    bar5 = pb.ChargingBar("Загрузка...", max=100)
    for i in range(100):
        bar5.next()
        time.sleep(0.01)
    bar5.finish()
    sound_error.play()
    print("libary ~$grid", Fore.RED + "[False]" + Style.RESET_ALL)
    furst_file = open("ОткройМеня.txt", "w+")
    furst_file.write(deadcat1 + "\n")
    furst_file.write(deadcat2 + "\n")
    furst_file.write(deadcat3 + "\n")
    furst_file.close()
    time.sleep(0.3)
    print("")
    print("...Чтобы устранить ошибки, пропиши команду r_ping")
    a = input("$ ")
    time.sleep(1)
    if a == "r_ping":
        startrping()
    else: 
        print("ты долбеабина")
 
def start():
    init()
    
    pygame.mixer.init()
    pygame.mixer.music.load("system.mp3")
    pygame.mixer.music.play(-1)

    os.system('cls||clear')

    time.sleep(1.5)
    tprint("Lonely kitty")
    print("")
    print(Name, "привет! Давно я тебя не видел! >.<")
    print("")
    a = input("Нажмите Enter")
    time.sleep(1.5)
    os.system('cls||clear')
    time.sleep(1)
    print("Как себя чувствуешь?")
    menu = TerminalMenu(['Неплохо', 'Отлично', 'Плохо', '...'])
    menu.show()
    os.system('cls||clear')
    time.sleep(1)
    print("Знаешь, это неважно... Лучше открой папку со мной и посмотри что я сделал для тебя!")

    furst_file = open("ОткройМеня.txt", "w+")
    wget.download(url_img)
    furst_file.write(cat1 + "\n")
    furst_file.write(cat2 + "\n")
    furst_file.write(cat3 + "\n")
    furst_file.write("" + "\n")
    for i in range(10):
        furst_file.write(fake.name() + "\n")
        furst_file.write(fake.address() + "\n")
    furst_file.close()
    time.sleep(3)
    print("Прикольно?")
    a = input("$ ")
    furst_mission()

def furst_mission():
    os.system('cls||clear')

    print("А теперь введи команду ping")
    print("")
    a = input("$ ")
    if a == "ping":
        startping()
    if a == "alien":
        alien()
    



def main_menu():
    tprint("Lonely kitty")
    print("")

    options = ["Начать", "Настройки", "Авторы", "Выход"]

    mainMenu = TerminalMenu(options, title="main menu")

    quitting = False 

    while quitting == False:
        optionsIndex = mainMenu.show()
        optionsChoice = options[optionsIndex]

        if(optionsChoice == "Начать"):
            start()
        if(optionsChoice == "Выход"):
            quitting = True


console()
#main_menu()
