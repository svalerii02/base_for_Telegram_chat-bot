import telebot

bot = telebot.TeleBot('789381710:AAFDGOFoE-ySju8S1-xwvcdAcrbgzArV_AI')


class User:
    def __init__(self, number, ident):
        self.number = number
        self.id = ident


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '/reg - регистрация\n/help - список команд\n/arch - пакет на архивацию')
    bot.register_next_step_handler(message, reg)


@bot.message_handler(commands=['reg'])
def reg(message):
    bot.send_message(message.chat.id, 'Ваш номер?\nНомер состоит из символа \'#\' и четырёх цифр. Пример: #5555')
    bot.register_next_step_handler(message, reg_number)


@bot.message_handler(content_types=['text'])
def reg_number(message):
    if len(message.text) == 5 and message.text.startswith('#') == True and message.text[1:4].isdigit() == True:
        bot.send_message(message.chat.id, 'Принято.')
    else:
        bot.send_message(message.chat.id, 'Номер введен некорректно.')


bot.polling()
