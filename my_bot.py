import random
import gtts
import khayyam
import telebot
from telebot import types

game_keyboard = types.ReplyKeyboardMarkup(row_width=1)
key1=types.KeyboardButton('new game')
key2=types.KeyboardButton('فال حافظ')
key3=types.KeyboardButton('ماشین حساب')
key4=types.KeyboardButton('چت بات')
key5=types.KeyboardButton('دانلود')
key6=types.KeyboardButton('راهنما')
game_keyboard.add(key1)


bot = telebot.TeleBot("6448003610:AAFUY91lIc1uC3hntVbiVnlBrC8OHK_Ls6g", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global user_name
    user_name = message.from_user.first_name #gets user's first name from telegram
    bot.reply_to(message,"سلام " + user_name + ". به بات پایتون مهدی خوش آمدی. 🙂")


computer_number = random.randint (10,40)

@bot.message_handler(commands=['game'])
@bot.message_handler(func=lambda m: True)
def guess_number(message):
  
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, "یک عدد حدس بزن " , reply_markup=game_keyboard)

    bot.send_message(message.chat.id, computer_number)

    user_number = int(message.text)

    if computer_number == user_number:
        bot.send_message(message.chat.id, "💡")
        bot.send_message(message.chat.id, "آفرین " + user_name + " برنده شدی." , reply_markup=game_keyboard)

    elif computer_number > user_number:
        bot.send_message(message.chat.id, "برو بالا ⬆" , reply_markup=game_keyboard)
        
    elif computer_number < user_number:
        bot.send_message(message.chat.id, "بیا پایین سرم درد گرفت ⬇" , reply_markup=game_keyboard)



@bot.message_handler(commands=['age'])
@bot.message_handler(func=lambda m: True)
def age(message):
    
    bot.send_message(message.chat.id, "تاریخ تولدت رو به شکل 1/1/1401 وارد کن")
    date_of_birth = message.text.split("/")
    dif=khayyam.JalaliDate.today()-khayyam.JalaliDate(date_of_birth[0], date_of_birth[1], date_of_birth[2])
    year = dif // 365
    month = (dif - (year * 365)) // 30
    day = dif - (year * 365 + month * 30)
    
    bot.send_message(message.chat.id, "سن تو: " + year + " سال و " + month + " ماه و " + day + " روز")

    
@bot.message_handler(commands=['voice'])
@bot.message_handler(func=lambda m: True)
def voice(message):
    
    input=bot.send_message(message.chat.id, "جمله‌ی خود را به انگلیسی وارد کنید.")
    v = gtts.gTTS (input, lang= 'en', slow = False)
    v.save ("PyLearn7-Assignment9/voice.mp3")
    audio = open('D:\PyLearn7\Assignments\PyLearn7-Assignment9\voice.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)



@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "برای کمک به شما آماده‌ام")

@bot.message_handler(commands= ["fal"])
def send_fal(message):
    fal_list = ["شخص بزرگی را خواهی دید","به دیدار یار خواهی رفت","به سفر خواهی رفت"]
    selected_fal = random.choice(fal_list)
    bot.send_message(message.chat.id, selected_fal)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "سلام":
        bot.send_message(message.chat.id, "علیک سلام")
    elif message.text == "خوبی؟":
        bot.send_message(message.chat.id, "خوبم. سپاس")
    elif message.text == "دوستت دارم":
        bot.send_message(message.chat.id, "❤")
    elif message.text == "یک عکس بده":
        photo = open("session 9/marguerite.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "متوجه منظورت نمی‌شم 😕")
        

bot.infinity_polling()