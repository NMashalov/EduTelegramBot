from aiogram import Bot
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommand


async def set_ui_commands(bot: Bot):
    """
    Sets bot commands in UI
    :param bot: Bot instance
    """
    commands = [
        BotCommand(command="UploadTask", description="Upload task or check results"),
        BotCommand(command="Test", description="Attempt test or check results")
    ]
    await bot.set_my_commands(
        commands=commands
    )