from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup ,  ReplyKeyboardMarkup

import logging
from aiogram import Bot, Dispatcher, InlineKeyboardButton, InlineKeyboardMarkup


import logging
from aiogram import Bot, Dispatcher, InlineKeyboardButton, InlineKeyboardMarkup

async def music_bot_btn():
    btn = InlineKeyboardMarkup

async def choose_lang_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("pastlives", callback_data="pastlives")   
    )
    return btn


