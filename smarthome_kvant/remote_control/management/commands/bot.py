from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater
from telegram.utils.request import Request
from remote_control.models import Termometr, Led, PosTerm, Rgb, Profile, Message


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_msg = f'Произошла Ошибка: {e}'
            print(error_msg)
            raise e
    return inner

@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    p, _= Profile.objects.get_or_create(
        external_id = chat_id,
        defaults={
            'name': update.message.from_user.username
        }
    )
    m = Message(
        profile=p,
        text=text,
    )
    m.save()
    reply_text = f"Привет {update.message.from_user.first_name}! Как дела?"
    update.message.reply_text(
        text=reply_text,
    )
    off = Led.pos(

    )
class Command(BaseCommand):
    help = 'Телеграм-бот для управления умным домом'
    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token='1407504233:AAHcvnfzhfPS-Hqs4ZN_dJoJqfO1erzyeJU',
        )
        updater = Updater(
            bot=bot,
            use_context=True,
        )
        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)
        updater.start_polling()
        updater.idle()
        print(bot.get_me())
