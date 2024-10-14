from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update._effective_chat:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="Добро пожаловать!"
        )

