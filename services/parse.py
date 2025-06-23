from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters.state import State, StatesGroup
import asyncio


class ParseStates(StatesGroup):
    parsing = State()

async def parse() -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Без UI
        page = await browser.new_page()
        await page.goto('https://svinland.ru', timeout=15000)
        
        await page.wait_for_selector("text=₽", timeout=5000)

        html_content = await page.content()
        soup = BeautifulSoup(html_content, 'html.parser')


        price_element = soup.select_one('div.mt-3.relative.z-30.text-base.font-medium')


        if price_element:
            price_text: str = price_element.text.strip()
            await browser.close()
            return price_text.split()[0]
        else:
            await browser.close()
            return "Цена не найдена"

async def parse_loop(message: Message, state: FSMContext):
    while (await state.get_state()) == ParseStates.parsing:
        price = await parse()
        if price != '2500':
            await message.answer(f'ЦЕНА ИЗМЕНИЛАСЬ!!!\n<u>{price}</u> Р\nhttps://svinland.ru')
            break
        await asyncio.sleep(60)
