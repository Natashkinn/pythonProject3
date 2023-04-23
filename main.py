import logging
import telebot
from telebot import types
from telegram.ext import Application, MessageHandler, filters, CommandHandler


def is_prime(number):
    if number == '1':
        return ' не'
    f = True
    for i in range(2, int(number)):
        if int(number) % i == 0:
            f = False
    if f:
        return ''
    else:
        return ' не'


def number_of_deliteley(number):
    n = 0
    for i in range(1, int(int(number) ** 0.5) + 1):
        if int(number) % i == 0:
            n += 1
    return n


def summ_digits(number):
    return str(sum([int(i) for i in number]))


def mult_digits(number):
    mult = 1
    for j in number:
        mult *= int(j)
    return str(mult)


def deliteli(number):
    s = []
    for i in range(1, int(int(number) ** 0.5) + 1):
        if int(number) % i == 0:
            s.append(str(i))
    return ', '.join(s)


def prime_deliteli(number):
    s = []
    for i in range(2, int(number) + 1):
        if int(number) % i == 0 and not is_prime(i):
            s.append(str(i))
    return ', '.join(s)


def last_prime(number):
    number = int(number) - 1
    while is_prime(int(number)):
        number -= 1
    return number


def next_prime(number):
    number = int(number) + 1
    while is_prime(int(number)):
        number += 1
    return number


def bin_system(number):
    return bin(int(number))[2:]


def oct_system(number):
    return oct(int(number))[2:]


def twe_system(number):
    number = int(number)
    to_base = 12
    from_base = 10
    if isinstance(number, str):
        number = int(number, from_base)
    else:
        number = int(number)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number < to_base:
        return alphabet[number]
    else:
        return twe_system(number // 12) + alphabet[number % 12]


def hex_system(number):
    return hex(int(number))[2:]


def is_fibonacci(number):
    a, b = 0, 1
    number = int(number)
    for i in range(number):
        a, b = b, a + b
        if number == b:
            return ''
    return ' не'


def is_factorial(number):
    i = f = 1
    number = int(number)
    while f < number:
        i += 1
        f *= i
    if f == number:
        return ''
    else:
        return ' не'


def squart(number):
    return int(number) ** 0.5


def square(number):
    return int(number) ** 2


def answer(number):
    output_text = []
    output_text.append(f'Квадрат числа: {square(number)}')
    output_text.append(f'Корень из числа: {squart(number)}')
    output_text.append(f'Сумма цифр числа {number}: ' + summ_digits(number))
    output_text.append(f'Произведение цифр числа {number}: ' + mult_digits(number))
    output_text.append(f'Делители числа {number}: ' + deliteli(number))
    output_text.append(
        f'Количество делителей у числа {number}: {number_of_deliteley(number)}')
    output_text.append(f'Простые делители числа {number}: ' + prime_deliteli(number))
    output_text.append(f'Предыдущее простое число: {last_prime(number)}')
    output_text.append(f'Следующее простое число: {next_prime(number)}')
    output_text.append(f'Двоичная запись числа: {bin_system(number)}')
    output_text.append(f'Восьмеричная запись числа: {oct_system(number)}')
    output_text.append(f'Двенадцатeричная запись числа: {twe_system(number)}')
    output_text.append(f'Шестнадцатеричная запись числа: {hex_system(number)}')
    output_text.append(f'Число {number}{is_prime(number)} является простым')
    output_text.append(f'Число {number}{is_fibonacci(number)} является членом'
                       f' последовательности Фибоначчи')
    output_text.append(f'Число {number}{is_factorial(number)} является факториалом')
    return output_text


def buttons(number):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    item_next = types.KeyboardButton(f'{int(number) + 1}')
    item_last = types.KeyboardButton(f'{int(number) - 1}')
    keyboard.add(item_last, item_next)
    return keyboard


bot = telebot.TeleBot('6299211797:AAHsmgaSjJYWuKmuMmqycptwaXXdqzHdSB8')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text(open('приветствие', 'r', encoding='utf-8').readlines()[0])


async def picture(update, context):
    await update.message.reply_text('Очень красиво! Но я работаю только с числами :( попробуй еще раз', )


async def text(update, context):
    if not update.message.text.isdigit():
        await update.message.reply_text('Это конечно хорошо, но я работаю только с натуральными числами '
                                        ':( попробуй еще раз')
    else:
        if update.message.text == '1906' or update.message.text == '1709' or \
                update.message.text == '1211' or update.message.text == '1406':
            url = 'https://sun9-36.userapi.com/impg/sqOrQ4kBa_PtctbUcy_OV3B4xy0unG5pN' \
                  'p7oMw/Wfb76Rl2Nkc.jpg?size=750x751&quality=96&sign=333eb641ded924aed615' \
                  '1ba240174b41&c_uniq_tag=t67hzk7WMeHHY7FZcgt_VgwKtkf4P7AdVSWwG_yW20w&type=album'
            await update.message.reply_text('Поздравляю! Ты набрел на счастливое число - день рождения самого лучшего '
                                            'человека! Этот котик для тебя <3')
            bot.send_photo(update.message.chat.id, url)
        elif update.message.text == '1307':
            url = 'https://i.pinimg.com/originals/1e/55/6d/1e556d156c42ae73c80b20b172740798.jpg'
            await update.message.reply_text('Поздравляю! Ты набрел на счастливое число - день рождения человека, '
                                            'который может поставить мне максимум за премию ваууу! <3')
            bot.send_photo(update.message.chat.id, url)
        elif update.message.text == '2905':
            url = 'https://www.meme-arsenal.com/memes/bb6a1695fc537ceb9aeb6b7220812e20.jpg'
            await update.message.reply_text('Соболезную. Ты ввел дату ЕГЭ по русскому')
            bot.send_photo(update.message.chat.id, url)
        if int(update.message.text) > 1000000:
            await update.message.reply_text('Слишком большое число, сегодня я с таким не справлюсь :<')
        else:
            bot.send_message(update.message.chat.id, '\n\n'.join(answer(update.message.text)),
                             reply_markup=buttons(update.message.text))


async def voice(update, context):
    await update.message.reply_text('У тебя прекрасный голос, но я работаю только с числами :( попробуй еще раз')


def main():
    application = Application.builder().token('6299211797:AAHsmgaSjJYWuKmuMmqycptwaXXdqzHdSB8').build()
    application.add_handler(CommandHandler("start", start))
    text_handler = MessageHandler(filters.PHOTO, picture)
    application.add_handler(text_handler)
    text_handler = MessageHandler(filters.TEXT, text)
    application.add_handler(text_handler)
    text_handler = MessageHandler(filters.VOICE, voice)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
