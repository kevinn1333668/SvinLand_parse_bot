from aiogram import Bot
from aiogram.types import BotCommand

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command='/price',
            description='Узнать цену'
        ),
        BotCommand(
            command='/start_parse',
            description='Бот пришлёт цену, если она изменилась'
        ),
        BotCommand(
            command='/stop_parse',
            description='Бот перестанет узнавать изменилась ли цена на сайте'
        )
    ]
    await bot.set_my_commands(main_menu_commands)