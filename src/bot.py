
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from sopt import buscar_questoes
import json
import os

# Habilitar o logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

mytags = ["python"]


def start(bot, update):
    """Mensagem inicial do comando /start"""
    update.message.reply_text('Iniciar configuração - mostrar lista de comandos')

def tagsToString():
    return "\n".join(str(x) for x in mytags)

def myTag(bot, update):
    update.message.reply_text("Minhas tags:\n\n" + tagsToString())

def addTag(bot, update, args):
    mytags.extend(args)
    update.message.reply_text("Minhas tags:\n\n" + tagsToString())

def deleteTag(bot, update, args):
    return

def ver_perguntas(bot, update, args):
    max_default = 10

    if args:
        max_default = int(args[0])
    #reply_keyboard = [['python', 'php', 'javascript']]

    #buscar questao da lista de mais recentes da tag 'python'(intervalo de 1 dia)
    questoes = buscar_questoes(mytags)
    total = len(questoes)
    for i in range(0, max_default if total > max_default else total):
        update.message.reply_text(questoes[i])

def help(bot, update):
    update.message.reply_text("""
    Bot para perguntas do SOpt - em construção!
    """)

def echo(bot, update):
    """Responder comandos invalidos"""
    update.message.reply_text("Comando inválido - ver lista de comandos")


def error(bot, update, error):
    """Log de Erros"""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Iniciar o bot"""
    # Criar o EventHandler
    config = json.loads(open(os.getcwd()[0:int(len(os.getcwd())-4)]+"/config/token.json").read())
    updater = Updater(config["token"])

    # Obter o dispatcher para registrar os handlers
    dp = updater.dispatcher

    # comandos habilitados
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("buscar", ver_perguntas, pass_args=True))
    dp.add_handler(CommandHandler("mytag", myTag))
    dp.add_handler(CommandHandler("addtag", addTag, pass_args=True))
    dp.add_handler(CommandHandler("deletetag", deleteTag, pass_args=True))

    # p/ comandos não reconhecidos
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log de erros
    dp.add_error_handler(error)

    # Iniciar o Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
