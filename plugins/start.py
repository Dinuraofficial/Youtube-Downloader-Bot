from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/SL_bot_zone")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/DinuraNikalansuriya")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nN.M.Dinura Uthsara Nikalansuriya, [02.10.21 20:42]
Welcome to @Youtube_Video_Downloader_D_bot, The Most Advanced Youtube Video and Audio Downloader in Telegram!

Please send any Youtube video link or search using @vid inline mode."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
