from telegram.ext import ConversationHandler


async def start(update, context):
    await update.message.reply_text(
        "Для более точных рекомендаций, пожалуйста, пройдите небольшой опрос.\n"
        "Вы можете прервать опрос, послав команду /stop\n"
        "(тогда результаты опроса не повлияют на рекомендации).\n")
    await update.message.reply_text(
        "Запишите интересные для Вас темы <b>через запятую</b>\n"
        "или оставьте поле пустым.",
                  parse_mode="HTML")

    return 1


async def first_response(update, context):

    tags = ", ".join(update.message.text.lower().split(",")).capitalize()
    await update.message.reply_text(
        "Интересные для Вас темы\n" + tags)
    await update.message.reply_text(
        "Дополнить список?")
    return 2


async def second_response(update, context):
    await update.message.reply_text("Спасибо за участие в опросе! Всего доброго!")
    return ConversationHandler.END


async def stop(update, context):
    await update.message.reply_text("Опрос пропущен.\n"
                                    "Если Вы хотите пройти опрос введите команду /start")
    return ConversationHandler.END