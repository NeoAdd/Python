from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import *


app = ApplicationBuilder().token("5775246226:AAF6ojGvY6AUyJCmXvj056u7pANWmS4ybkk").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))



print('server start')
app.run_polling()