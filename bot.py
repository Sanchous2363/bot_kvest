import telebot
from telebot import types
from datetime import datetime
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from for_json import load_user_data, save_user_data
smiles = "🔊📣☣☢⚠"
TOKEN = "6901106032:AAGU3pum50ckHlNCU5dj8uR_apAeV_pdzhU"
bot = telebot.TeleBot(TOKEN)
data_path = "users.json"
user_data = load_user_data(data_path)
data = "info.json"
user_data2 = load_user_data(data)

@bot.message_handler(commands=['start', 'regame'])
def start(message):
    knopka = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Играть🔥☣☢⚠", callback_data='text_answer1')
    btn2 = types.InlineKeyboardButton("Информация(перед прохождением)", callback_data='text_answer2')
    btn3 = types.InlineKeyboardButton("Помощь🔊📣", callback_data='text_answer3')
    knopka.row(btn1, btn3)
    knopka.row(btn2)
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}! Я бот, который поможет тебе погрузиться в атмосферу путешествий во времени. Бот-квест по мотивам трилогии 'Книга времени' с увлекательными развязками, разнообразными выборами! Удачной игры!", reply_markup=knopka)
    if message.from_user.id in user_data:
        bot.send_message(message.chat.id, "Ухты! Вы уже зарегестрированны в нашей системе!")
    else:
        time = datetime.now().strftime('%d.%m.%y')
        #todo: Считываем данные из файла, если
        # Инициализируем данные пользователя
        user_data[message.chat.id]= {"name": message.from_user.first_name,
                                  "time": time, "status_of_location": 0, "inventory": ["Ключи от дома и сейфа"], "status": ""}
        #todo: Сохраняем данные пользователя
        save_user_data(user_data, data_path)
    user_data[message.chat.id]["status"] = ""
    save_user_data(user_data, data_path)

@bot.message_handler(commands=['help'])
def hendler_help(message):
    bot.send_message(message.chat.id, "/regame - начать игру сначала, \n/start - запуск бота\n Правила сохранения:\n 1. Сохраняютя не все этапы\n 2. Эти этапы нельзя настроить!")

@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    if callback.data == "text_answer2":
        bot.send_message(callback.message.chat.id, "пока ничего нет")
        bot.send_photo(callback.message.chat.id, open("media/2363.PNG", "rb"))
    elif callback.data == "text_answer3":
        bot.send_message(callback.message.chat.id, "описание команд и тп")

    elif callback.data == "text_answer1":
        if user_data[callback.message.chat.id]["status_of_location"] == 0:
            knopka = types.InlineKeyboardMarkup()
            btn4 = types.InlineKeyboardButton(user_data2["start"]["options"]["a"], callback_data='text_answer4')
            btn5 = types.InlineKeyboardButton(user_data2["start"]["options"]["b"], callback_data='text_answer5')
            knopka.row(btn4, btn5)
            bot.send_message(callback.message.chat.id, user_data2["start"]["description"])
            bot.send_photo(callback.message.chat.id, open("media/final2.PNG", "rb"))
            bot.send_photo(callback.message.chat.id, open("media/final3.PNG", "rb"))
            bot.send_message(callback.message.chat.id, user_data2["start"]["description2"], reply_markup=knopka)
        elif user_data[callback.message.chat.id]["status_of_location"] == 1:
            bot.send_message(callback.message.chat.id, user_data2["loc4"]["description"])
            bot.send_photo(callback.message.chat.id, open("media/final7.PNG", "rb"))
            knopka = types.InlineKeyboardMarkup()
            btn10 = types.InlineKeyboardButton(user_data2["loc4"]["options"]["a"], callback_data='text_answer10')
            knopka.row(btn10)
            bot.send_message(callback.message.chat.id, user_data2["loc4"]["description2"], reply_markup=knopka)
        elif user_data[callback.message.chat.id]["status_of_location"] == 2:
            bot.send_photo(callback.message.chat.id, open("media/final1.PNG", "rb"))
            knopka = types.InlineKeyboardMarkup()
            btn16 = types.InlineKeyboardButton(user_data2["loc7"]["options"]["a"], callback_data='text_answer16')
            btn17 = types.InlineKeyboardButton(user_data2["loc7"]["options"]["b"], callback_data='text_answer17')
            knopka.row(btn16, btn17)
            bot.send_message(callback.message.chat.id, user_data2["loc7"]["description"], reply_markup=knopka)
        elif user_data[callback.message.chat.id]["status_of_location"] == 3:
            knopka = types.InlineKeyboardMarkup()
            btn25 = types.InlineKeyboardButton(user_data2["loc10"]["options"]["c"], callback_data='text_answer25')
            btn26 = types.InlineKeyboardButton(user_data2["loc10"]["options"]["d"], callback_data='text_answer26')
            knopka.row(btn25, btn26)
            bot.send_message(callback.message.chat.id, user_data2["loc10"]["description2"], reply_markup=knopka)
        elif user_data[callback.message.chat.id]["status_of_location"] == 4:
            knopka = types.InlineKeyboardMarkup()
            bot.send_message(callback.message.chat.id, user_data2["loc13"]["options"]["b"])
            btn30 = types.InlineKeyboardButton(user_data2["loc13"]["options"]["options_for_c"]["a"],
                                               callback_data='text_answer30')
            btn31 = types.InlineKeyboardButton(user_data2["loc13"]["options"]["options_for_c"]["b"],
                                               callback_data='text_answer31')
            knopka.row(btn30, btn31)
            bot.send_message(callback.message.chat.id, user_data2["loc13"]["options"]["c"], reply_markup=knopka)
    if user_data[callback.message.chat.id]["status"] != "LOSE":
        if callback.data == "text_answer4":
            knopka = types.InlineKeyboardMarkup()
            btn7 = types.InlineKeyboardButton(user_data2["loc2"]["options"]["a"], callback_data='text_answer6')
            btn8 = types.InlineKeyboardButton(user_data2["loc2"]["options"]["b"], callback_data='text_answer7')
            knopka.row(btn8, btn7)
            bot.send_message(callback.message.chat.id,user_data2["loc2"]["description"], reply_markup=knopka)
        elif callback.data == "text_answer5":
            bot.send_message(callback.message.chat.id, 'Вы проиграли! ВЫ недостаточно инициативны')
            bot.send_message(callback.message.chat.id,
                         "К сожалению вы не можете продолжать прозодить квест, для прохождения придется начать заново, все данные влияющие на прохождение будут стерты! Пройдите его заного, через команду /start или /regame",
                         )
            user_data[callback.message.chat.id]["status_of_location"] = 0
            user_data[callback.message.chat.id]["level_in_level"] = ""
            user_data[callback.message.chat.id]["status"] = "LOSE"
            user_data[callback.message.chat.id]["inventory"] = ["Ключи от дома и сейфа"]
            save_user_data(user_data, data_path)

        elif callback.data == "text_answer6":
            knopka = types.InlineKeyboardMarkup()
            btn8 = types.InlineKeyboardButton(user_data2["loc3"]["options"]["a"], callback_data='text_answer8')
            btn9 = types.InlineKeyboardButton(user_data2["loc3"]["options"]["b"], callback_data='text_answer9')
            knopka.row(btn8, btn9)
            bot.send_photo(callback.message.chat.id, open("media/final5.PNG", "rb"))
            bot.send_message(callback.message.chat.id, user_data2["loc3"]["description"], reply_markup=knopka)
        elif callback.data == "text_answer7":
            bot.send_message(callback.message.chat.id, user_data2["loc2"]["police_setuation"])
            bot.send_photo(callback.message.chat.id, open("media/final4.PNG", "rb"))
            bot.send_message(callback.message.chat.id,
                         "К сожалению вы не можете продолжать прозодить квест, для прохождения придется начать заново, все данные влияющие на прохождение будут стерты! Пройдите его заного, через команду /start или /regame",
                         )
            user_data[callback.message.chat.id]["status_of_location"] = 0
            user_data[callback.message.chat.id]["level_in_level"] = ""
            user_data[callback.message.chat.id]["status"] = "LOSE"
            save_user_data(user_data, data_path)
        elif callback.data == "text_answer8":
            knopka = types.InlineKeyboardMarkup()
            btn11 = types.InlineKeyboardButton("Погнали дальше?", callback_data='text_answer9')
            knopka.row(btn11)
            bot.send_message(callback.message.chat.id, user_data2["loc3"]["reading"], reply_markup=knopka)
        elif callback.data == "text_answer9":
            bot.send_message(callback.message.chat.id, user_data2["loc4"]["description"])
            bot.send_photo(callback.message.chat.id, open("media/final7.PNG", "rb"))
            knopka = types.InlineKeyboardMarkup()
            btn10 = types.InlineKeyboardButton(user_data2["loc4"]["options"]["a"], callback_data='text_answer10')
            knopka.row(btn10)
            bot.send_message(callback.message.chat.id, user_data2["loc4"]["description2"], reply_markup=knopka)
            user_data[callback.message.chat.id]["status_of_location"] = 1
            save_user_data(user_data, data_path)
        #todo: фигачим сохранения левла China
        elif callback.data == "text_answer10":
            bot.send_message(callback.message.chat.id, user_data2["loc5"]["description"])
            bot.send_message(callback.message.chat.id, user_data2["loc6"]["description"])
            bot.send_photo(callback.message.chat.id, open("media/final8.PNG", "rb"))
            knopka = types.InlineKeyboardMarkup()
            btn13 = types.InlineKeyboardButton(user_data2["loc6"]["options"]["b"], callback_data='text_answer13')
            btn14 = types.InlineKeyboardButton(user_data2["loc6"]["options"]["d"], callback_data='text_answer14')
            btn15 = types.InlineKeyboardButton(user_data2["loc6"]["options"]["e"], callback_data='text_answer15')
            knopka.row(btn15)
            knopka.row(btn13, btn14)
            bot.send_message(callback.message.chat.id, user_data2["loc6"]["description2"], reply_markup=knopka)
        elif callback.data == "text_answer13":
            user_data[callback.message.chat.id]["inventory"].append("нож")
            bot.send_message(callback.message.chat.id, "В ваш инвентарь добавлен нож")
            bot.send_photo(callback.message.chat.id, open("media/final11.PNG", "rb"))
        elif callback.data == "text_answer14":
            user_data[callback.message.chat.id]["inventory"] += ["отмычка и фонарик"]
            bot.send_message(callback.message.chat.id, "В ваш инвентарь добавлены отмычка и фонарик")
            bot.send_photo(callback.message.chat.id, open("media/final12.PNG", "rb"))
        elif callback.data == "text_answer15":
            bot.send_photo(callback.message.chat.id, open("media/final1.PNG", "rb"))
            knopka = types.InlineKeyboardMarkup()
            btn16 = types.InlineKeyboardButton(user_data2["loc7"]["options"]["a"], callback_data='text_answer16')
            btn17 = types.InlineKeyboardButton(user_data2["loc7"]["options"]["b"], callback_data='text_answer17')
            knopka.row(btn16, btn17)
            bot.send_message(callback.message.chat.id, user_data2["loc7"]["description"], reply_markup=knopka)
            user_data[callback.message.chat.id]["status_of_location"] = 2
            save_user_data(user_data, data_path)
        elif callback.data == "text_answer16":
            knopka = types.InlineKeyboardMarkup()
            btn18 = types.InlineKeyboardButton(user_data2["loc7"]["options"]["c"], callback_data='text_answer18')
            btn19 = types.InlineKeyboardButton(user_data2["loc7"]["options"]["d"], callback_data='text_answer19')
            knopka.row(btn18, btn19)
            bot.send_message(callback.message.chat.id, user_data2["loc7"]["description2"], reply_markup=knopka)
            bot.send_photo(callback.message.chat.id, open("media/final10.PNG", "rb"))
        elif callback.data == "text_answer17":
            bot.send_message(callback.message.chat.id, "А ты был так близок... Пока ты брел домой ты замерз, это фиаско!")
            bot.send_message(callback.message.chat.id,
                             "К сожалению вы не можете продолжать прозодить квест, для прохождения придется начать заново, все данные влияющие на прохождение будут стерты! Пройдите его заного, через команду /start или /regame",
                             )
            user_data[callback.message.chat.id]["status_of_location"] = 0
            user_data[callback.message.chat.id]["inventory"] = ["Ключи от дома и сейфа"]
            user_data[callback.message.chat.id]["level_in_level"] = ""
            user_data[callback.message.chat.id]["status"] = "LOSE"
            save_user_data(user_data, data_path)
        elif callback.data == "text_answer18":
            bot.send_message(callback.message.chat.id, user_data2["loc8"]["description2"])
        elif callback.data == "text_answer19":
            knopka = types.InlineKeyboardMarkup()
            btn20 = types.InlineKeyboardButton(user_data2["loc8"]["options"]["a"], callback_data='text_answer20')
            knopka.row(btn20)
            bot.send_message(callback.message.chat.id, user_data2["loc8"]["description"], reply_markup=knopka)
        elif callback.data == "text_answer20":
            bot.send_message(callback.message.chat.id, user_data2["loc9"]["description"])
            knopka = types.InlineKeyboardMarkup()
            btn21 = types.InlineKeyboardButton(user_data[callback.message.chat.id]["inventory"][0], callback_data='text_answer21')
            btn22 = types.InlineKeyboardButton(user_data[callback.message.chat.id]["inventory"][1], callback_data='text_answer22')
            knopka.row(btn21, btn22)
            bot.send_message(callback.message.chat.id, user_data2["loc9"]["description2"], reply_markup=knopka)
        elif callback.data == 'text_answer22':
            if user_data[callback.message.chat.id]["inventory"][1] == "нож":
                knopka = types.InlineKeyboardMarkup()
                btn23 = types.InlineKeyboardButton(user_data2["loc10"]["options"]["a"], callback_data='text_answer23')
                btn24 = types.InlineKeyboardButton(user_data2["loc10"]["options"]["b"], callback_data='text_answer24')
                knopka.row(btn23, btn24)
                bot.send_message(callback.message.chat.id, user_data2["loc10"]["description3"], reply_markup=knopka)
            elif user_data[callback.message.chat.id]["inventory"][1] == "отмычка и фонарик":
                knopka = types.InlineKeyboardMarkup()
                btn25 = types.InlineKeyboardButton(user_data2["loc10"]["options"]["c"], callback_data='text_answer25')
                btn26 = types.InlineKeyboardButton(user_data2["loc10"]["options"]["d"], callback_data='text_answer26')
                knopka.row(btn25, btn26)
                bot.send_message(callback.message.chat.id, user_data2["loc10"]["description2"], reply_markup=knopka)
                user_data[callback.message.chat.id]["status_of_location"] = 3
                save_user_data(user_data, data_path)
                #todo: сохранение2
        elif callback.data == 'text_answer21':
            bot.send_message(callback.message.chat.id, user_data2["loc10"]["description"])
        elif callback.data == 'text_answer23':
            bot.send_message(callback.message.chat.id, user_data2["loc13"]["description"])
            bot.send_message(callback.message.chat.id,
                         "К сожалениювы не можете продолжать прозодить квест, для прохождения придется начать заново, все данные влияющие на прохождение будут стерты! Пройдите его заного, через команду /start или /regame",
                         )
            user_data[callback.message.chat.id]["status_of_location"] = 0
            user_data[callback.message.chat.id]["inventory"] = ["Ключи от дома и сейфа"]
            user_data[callback.message.chat.id]["level_in_level"] = ""
            user_data[callback.message.chat.id]["status"] = "LOSE"
            save_user_data(user_data, data_path)

        elif callback.data == "text_answer24":
            knopka = types.InlineKeyboardMarkup()
            btn27 = types.InlineKeyboardButton("Далее", callback_data='text_answer27')
            knopka.row(btn27)
            bot.send_message(callback.message.chat.id, user_data2["loc13"]["description2"], reply_markup=knopka)
        elif callback.data == "text_answer25":
            bot.send_message(callback.message.chat.id, user_data2["loc12"]["description"])
            bot.send_photo(callback.message.chat.id, open("media/final15.PNG", "rb"))
            bot.send_message(callback.message.chat.id,
                         "К сожалению вы не можете продолжать прозодить квест, для прохождения придется начать заново, все данные влияющие на прохождение будут стерты! Пройдите его заного, через команду /start или /regame",
                         )
            user_data[callback.message.chat.id]["status_of_location"] = 0
            user_data[callback.message.chat.id]["level_in_level"] = ""
            user_data[callback.message.chat.id]["status"] = "LOSE"
            user_data[callback.message.chat.id]["inventory"] = ["Ключи от дома и сейфа"]
            save_user_data(user_data, data_path)
        elif callback.data == "text_answer26":
            bot.send_message(callback.message.chat.id, user_data2["loc12"]["description2"])
            bot.send_photo(callback.message.chat.id, open("media/final13.PNG", "rb"))
            user_data[callback.message.chat.id]["status_of_location"] = 0
            user_data[callback.message.chat.id]["level_in_level"] = ""
            user_data[callback.message.chat.id]["inventory"] = ["Ключи от дома и сейфа"]
            save_user_data(user_data, data_path)
        elif callback.data == 'text_answer27':
            knopka = types.InlineKeyboardMarkup()
            btn29 = types.InlineKeyboardButton("И че теперь делать?!", callback_data='text_answer29')
            knopka.row(btn29)
            bot.send_message(callback.message.chat.id, user_data2["loc13"]["options"]["a"], reply_markup=knopka)
        elif callback.data == "text_answer29":
            knopka = types.InlineKeyboardMarkup()
            bot.send_message(callback.message.chat.id, user_data2["loc13"]["options"]["b"])
            btn30 = types.InlineKeyboardButton(user_data2["loc13"]["options"]["options_for_c"]["a"], callback_data='text_answer30')
            btn31 = types.InlineKeyboardButton(user_data2["loc13"]["options"]["options_for_c"]["b"], callback_data='text_answer31')
            knopka.row(btn30, btn31)
            bot.send_message(callback.message.chat.id, user_data2["loc13"]["options"]["c"], reply_markup=knopka)
            bot.send_photo(callback.message.chat.id, open("media/final14.PNG", "rb"))
            user_data[callback.message.chat.id]["status_of_location"] = 4
            #todo: сохранение предфинальное
            save_user_data(user_data, data_path)
        elif callback.data == "text_answer30":
            bot.send_message(callback.message.chat.id, user_data2["loc14"]["description"])
            bot.send_message(callback.message.chat.id,
                         "К сожалению вы не можете продолжать проходить квест, для прохождения придется начать заново, все данные влияющие на прохождение будут стерты! Пройдите его заного, через команду /start или /regame",)
            user_data[callback.message.chat.id]["status_of_location"] = 0
            user_data[callback.message.chat.id]["level_in_level"] = ""
            user_data[callback.message.chat.id]["status"] = "LOSE"
            user_data[callback.message.chat.id]["inventory"] = ["Ключи от дома и сейфа"]
            save_user_data(user_data, data_path)
        elif callback.data == "text_answer31":
            bot.send_message(callback.message.chat.id, user_data2["loc14"]["description2"])
            user_data[callback.message.chat.id]["status_of_location"] = 0
            user_data[callback.message.chat.id]["level_in_level"] = ""
            user_data[callback.message.chat.id]["inventory"] = ["Ключи от дома и сейфа"]
            save_user_data(user_data, data_path)

@bot.message_handler(content_types=["text"])
def text(message):
    bot.send_message(message.chat.id, "Бот не расчитан на обработку сообщений")
@bot.message_handler(content_types=["audio"])
def audio(message):
    bot.send_message(message.chat.id, "Бот не расчитан на обработку аудио сообщений")
@bot.message_handler(content_types=["photo"])
def photo(message):
    bot.send_message(message.chat.id, "Бот не расчитан на обработку фото")
bot.polling()


