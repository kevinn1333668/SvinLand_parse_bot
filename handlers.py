from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from services.parse import parse_loop, parse, ParseStates
import asyncio

router = Router()


@router.message(Command('start_parse'))
async def start_parse(message: Message, state: FSMContext):
    if await state.get_state() == ParseStates.parsing:
        await message.answer("Парсинг уже идёт...")
        return
    await state.set_state(ParseStates.parsing)
    asyncio.create_task(parse_loop(message, state))
    await message.answer('Парсим цену!')

@router.message(Command("stop_parse"))
async def stop_parse(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Перестали парсить!")


@router.message(Command(commands='price'))
async def process_ask_price(message: Message):
    price: str = await parse()
    await message.answer(text=f'{price}\nhttps://svinland.ru')
