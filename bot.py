import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define a function for handling the /start command

def start(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a Telegram bot!")

# Define a function for handling incoming messages

def echo(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Define the main function for the bot

def main():

    # Create an Updater object and pass in your bot's API token

    updater = Updater(token='YOUR_TOKEN_HERE', use_context=True)

    # Get the dispatcher to register handlers

    dispatcher = updater.dispatcher

    # Register the /start command handler

    start_handler = CommandHandler('start', start)

    dispatcher.add_handler(start_handler)

    # Register the echo message handler

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(echo_handler)

    # Start the bot

    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT

    updater.idle()

# Call the main function to start the bot

if __name__ == '__main__':

    main()
