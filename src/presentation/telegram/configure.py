from telegram.ext import Application, CommandHandler

from presentation.telegram.handlers import start


def configure_application(application: Application) -> None:
    application.add_handler(CommandHandler("start", start.handler))
