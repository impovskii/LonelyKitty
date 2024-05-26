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
from matplotlib import pyplot as plt


pygame.mixer.init()
pygame.init()

init()

pygame.mixer.music.load("game_files/sound/system.mp3")
pygame.mixer.music.play(-1)

fake = Faker("RU")

url_img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT73GlitgyBwbdb2m-s3m8snu2Y9cm0T0OyDtEXJo2fwENstzIH656TdXaooMWE_RjTEH4&usqp=CAU"
sound_error = pygame.mixer.Sound('game_files/sound/error2.mp3')
sound_sell = pygame.mixer.Sound('game_files/sound/sell.mp3')
sound_horror = pygame.mixer.Sound('game_files/sound/horror.mp3')
sound_minecraft = pygame.mixer.Sound('game_files/sound/minecraft.mp3')


cat1 = " |\_/|"
cat2 = "( o.o )"
cat3 = " > ^ <"

deadcat1 = " |\_/|"
deadcat2 = "( x.x )"
deadcat3 = " > ^ <"

deadtext = "почему, за что, почему?"

os.system('cls||clear')

Name = os.getlogin()
    
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


def startorder():
    os.system("cls||clear")
    with open('game_files/json/data.json', 'r') as json_file:
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

def dataplus():
        #изменяем активность заказа
    with open('game_files/json/data.json', 'r') as file:
        data = json.load(file)

        data['relevance'] = False
        data_prise = data['prise']

    with open('game_files/json/data.json', 'w') as file:
        json.dump(data, file)
        #изменяем количество выполненых заказов и изменяем баланс
    with open('game_files/json/info.json', 'r') as file:
        data = json.load(file)

        data['completed_orders'] += 1
        data['money'] += data_prise

    with open('game_files/json/info.json', 'w') as file:
        json.dump(data, file, indent=4)


def starthack():
    os.system('cls||clear')

    with open('game_files/json/data.json', 'r') as json_file:
        data = json.load(json_file)
        order_relevance = data['relevance']

    with open('game_files/json/info.json', 'r') as json_file:
        info = json.load(json_file)
        completed_orders = info['completed_orders']
        money = info['money']

    if completed_orders == 13:
        sound_horror.play()
        img13 = plt.imread('game_files/img/images.jpeg')
        plt.imshow(img13)
        plt.show()
        time.sleep(22)
        furst_file = open("Тестордеры.txt", "w+")
        furst_file.write(deadcat1 + "\n")
        furst_file.write(deadcat2 + "\n")
        furst_file.write(deadcat3 + "\n")
        furst_file.close()

    if money >= 4000:
        furst_file = open("Тестденьги.txt", "w+")
        furst_file.write(deadcat1 + "\n")
        furst_file.write(deadcat2 + "\n")
        furst_file.write(deadcat3 + "\n")
        furst_file.close()

    if order_relevance == True:

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
        print(f"+7 (9**) *** ** **")

        i = 0
        while i == 0:
            print(random_num_one)
            a = input("$ ")
            c = int(a)
            if c == random_num_one:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}*) *** ** **")
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()

            print(random_num_two)
            a = input("$ ")
            c = int(a)

            if c == random_num_two:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}{random_num_two}) *** ** **")
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()

            print(random_num_three)
            a = input("$ ")
            c = int(a)

            if c == random_num_three:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}{random_num_two}) {random_num_three}** ** **")
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()

            print(random_num_four)
            a = input("$ ")
            c = int(a)

            if c == random_num_four:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}{random_num_two}) {random_num_three}{random_num_four}* ** **")
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()

            print(random_num_five)
            a = input("$ ")
            c = int(a)

            if c == random_num_five:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}{random_num_two}) {random_num_three}{random_num_four}{random_num_five} ** **")
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()

            print(random_num_six)
            a = input("$ ")
            c = int(a)

            if c == random_num_six:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}{random_num_two}) {random_num_three}{random_num_four}{random_num_five} {random_num_six}* **")
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()

            print(random_num_seven)
            a = input("$ ")
            c = int(a)

            if c == random_num_seven:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}{random_num_two}) {random_num_three}{random_num_four}{random_num_five} {random_num_six}{random_num_seven} **")
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()

            print(random_num_eight)
            a = input("$ ")
            c = int(a)

            if c == random_num_eight:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}{random_num_two}) {random_num_three}{random_num_four}{random_num_five} {random_num_six}{random_num_seven} {random_num_eight}*")
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()


            print(random_num_nine)
            a = input("$ ")
            c = int(a)

            if c == random_num_nine:
                os.system('cls||clear')
                print("autohack")
                print("")
                print(f"+7 (9{random_num_one}{random_num_two}) {random_num_three}{random_num_four}{random_num_five} {random_num_six}{random_num_seven} {random_num_eight}{random_num_eight}")
                i += 1
            else:
                os.system('cls||clear')
                print("~$Hack ", Fore.RED + "[Error]" + Style.RESET_ALL)
                sound_error.play()
                time.sleep(1)
                starthack()

        sound_sell.play()
        print("Вы успешно выполнили заказ!")
        dataplus()
        a = input("$ ")
        console()

    else:
        print("У вас нету заказов!")
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
    elif a == "hackeasy": #можно удалить
        starthackeasy()
    elif a == "order":
        startorder()
    elif a == "minecraft":
        sound_minecraft.play()
        minecraft = open("minecraft.txt", "w+")
        minecraft.write("⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⠀⠈⣷⣄⠀⠀⠀⠀⣾⣷⠀⠀⠀⠀⣠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⠀⠀⢿⠿⠃⠀⠀⠀⠉⠉⠁⠀⠀⠐⠿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⣠⣶⣿⣿⡿⣿⣿⣿⡿⠋⠉⠀⠀⠉⠙⢿⣿⣿⡿⣿⣿⣷⣦⡀⠀⠀⠀" + "\n")
        minecraft.write("⠀⢀⣼⣿⣿⠟⠁⢠⣿⣿⠏⠀⠀⢠⣤⣤⡀⠀⠀⢻⣿⣿⡀⠙⢿⣿⣿⣦⠀⠀" + "\n")
        minecraft.write("⣰⣿⣿⡟⠁⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣿⡟⠀⠀⠈⣿⣿⡇⠀⠀⠙⣿⣿⣷⡄" + "\n")
        minecraft.write("⠈⠻⣿⣿⣦⣄⠀⠸⣿⣿⣆⠀⠀⠀⠉⠉⠀⠀⠀⣸⣿⣿⠃⢀⣤⣾⣿⣿⠟⠁" + "\n")
        minecraft.write("⠀⠀⠈⠻⣿⣿⣿⣶⣿⣿⣿⣦⣄⠀⠀⠀⢀⣠⣾⣿⣿⣿⣾⣿⣿⡿⠋⠁⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⠀⠀⢰⣷⡦⠀⠀⠀⢀⣀⣀⠀⠀⠀⢴⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠙⢷⠀⠀⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.write("⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠻⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀" + "\n")
        minecraft.close()
        console()
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
