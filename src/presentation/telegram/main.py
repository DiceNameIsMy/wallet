from telegram.ext import ApplicationBuilder

from presentation.telegram.configure import configure_application
from presentation.telegram.settings import Settings


def main() -> None:
    settings = Settings()

    application = ApplicationBuilder().token(settings.api_token).build()
    configure_application(application)

    application.run_polling()


if __name__ == "__main__":
    main()
