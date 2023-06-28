from telegram import Update
from telegram.ext import ContextTypes

START_MESSAGE = "Application: Wallet"


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat = update.effective_chat
    assert chat is not None, "Chat should be present on `/start` command"

    await context.bot.send_message(chat_id=chat.id, text=START_MESSAGE)
