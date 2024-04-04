import config
import asyncio

from os import getenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.magic_filter import MagicFilter

import menu

TOKEN='6708382846:AAFA3ASL3Vlhtjrnf7yZv-yqSqneAC9nDnI'
dp = Dispatcher()
bot = Bot(TOKEN)


def linkable_menu(menu_data : dict):
    kb = [
        [KeyboardButton(text=val['NAME'])] 
        for val in menu_data.values()
    ]

    return ReplyKeyboardMarkup(keyboard=kb)

def main_menu() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text=menu.main['FACULTIES'])],
        [KeyboardButton(text=menu.main['OPEN_DAYS']['NAME'])],
        [KeyboardButton(text=menu.main['ABOUT']['NAME'])], 
    ]

    return ReplyKeyboardMarkup(keyboard=kb)


def has_entry(menu_data : dict, entry : str):
    for val in menu_data.values():
        if val['NAME'] == entry:
            return True
    
    return False


def get_key(menu_data : dict, entry : str):
    for key in menu_data.keys():
        if entry == menu_data[key]['NAME']:
            return key

    return None


def get_faculty(menu_data : dict, entry : str):
    key = get_key(menu_data, entry)
    
    if key == 'CS':
        return menu.cs
    
    if key == 'CEC':
        return menu.cec
    
    if key == 'ACT':
        return menu.act
    
    if key == 'ITM':
        return menu.itm
    
    if key == 'IC':
        return menu.ic
    
    if key == 'ELBE':
        return menu.elbe
    
    if key == 'IRTIS':
        return menu.irtis
    
    return None
    

@dp.message(F.text.func(
    lambda text: has_entry(menu.cs, text)
))
async def command_cs(message: Message):
    key = get_key(menu.cs, message.text)

    await bot.send_message(message.chat.id, menu.cs[key]['LINK'])
    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )



@dp.message(F.text.func(
    lambda text: has_entry(menu.cec, text)
))
async def command_cec(message: Message):
    key = get_key(menu.cec, message.text)

    await bot.send_message(message.chat.id, menu.cec[key]['LINK'])
    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )




@dp.message(F.text.func(
    lambda text: has_entry(menu.act, text)
))
async def command_act(message: Message):
    key = get_key(menu.act, message.text)

    await bot.send_message(message.chat.id, menu.act[key]['LINK'])
    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )




@dp.message(F.text.func(
    lambda text: has_entry(menu.itm, text)
))
async def command_itm(message: Message):
    key = get_key(menu.itm, message.text)

    await bot.send_message(message.chat.id, menu.itm[key]['LINK'])
    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )




@dp.message(F.text.func(
    lambda text: has_entry(menu.ic, text)
))
async def command_ic(message: Message):
    key = get_key(menu.act, message.text)

    await bot.send_message(message.chat.id, menu.ic[key]['LINK'])
    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )




@dp.message(F.text.func(
    lambda text: has_entry(menu.elbe, text)
))
async def command_elbe(message: Message):
    key = get_key(menu.elbe, message.text)

    await bot.send_message(message.chat.id, menu.elbe[key]['LINK'])
    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )



@dp.message(F.text.func(
    lambda text: has_entry(menu.irtis, text)
))
async def command_irtis(message: Message):
    key = get_key(menu.irtis, message.text)

    await bot.send_message(
        message.chat.id, 
        menu.irtis[key]['LINK']
    )
    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )




@dp.message(F.text.func(
    lambda text: has_entry(menu.faculties, text)
))
async def command_department(message: Message):
    menu_data = get_faculty(menu.faculties, message.text)
    
    if menu_data != None:
        await message.reply(
            text='Оберіть кафедру', 
            reply_markup=linkable_menu(menu_data)
        )


@dp.message(F.text == menu.main['FACULTIES'])
async def command_faculties(message: Message):

    await message.reply(
        text='Оберіть факультет', 
        reply_markup=linkable_menu(menu.faculties)
    )

@dp.message(F.text == menu.main['ABOUT']['NAME'])
async def command_faculties(message: Message):

    await bot.send_message(
        message.chat.id, 
        menu.main['ABOUT']['LINK']
    )

    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )


@dp.message(F.text == menu.main['OPEN_DAYS']['NAME'])
async def command_faculties(message: Message):

    await bot.send_message(
        message.chat.id, 
        menu.main['OPEN_DAYS']['LINK']
    )

    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )


@dp.message(Command('start'))
async def command_start(message: Message) -> None:
    await message.reply(
        'Оберіть дію', 
        reply_markup=main_menu()
    )



@dp.startup()
async def on_startup():
    print(config.MSG_RUNNING)

@dp.shutdown()
async def on_shutdown():
    print(config.MSG_SERVICE)


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())