import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# Set your API keys
TELEGRAM_BOT_TOKEN = "Enter your Telegram API Key here"
REMOVE_BG_API_KEY = "Enter your Gackground API KEY here"


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Send me an image, Nick will remove the background!")


def remove_bg(image_path):
    url = "https://api.remove.bg/v1.0/removebg"
    with open(image_path, "rb") as image_file:
        response = requests.post(
            url,
            files={"image_file": image_file},
            data={"size": "auto"},
            headers={"X-Api-Key": REMOVE_BG_API_KEY},
        )

    if response.status_code == 200:
        output_path = image_path.replace(".jpg", "_no_bg.png")
        with open(output_path, "wb") as out_file:
            out_file.write(response.content)
        return output_path
    else:
        return None


# async def handle_photo(update: Update, context: CallbackContext):
#     photo = await update.message.photo[-1].get_file()
#     image_path = "input.jpg"
#     await photo.download(image_path)
#
#     await update.message.reply_text("Removing background, please wait...")
#     output_path = remove_bg(image_path)
#
#     if output_path:
#         await update.message.reply_photo(photo=open(output_path, "rb"))
#         os.remove(output_path)
#     else:
#         await update.message.reply_text("Failed to remove background. Try again later.")
#
#     os.remove(image_path)

async def handle_photo(update: Update, context: CallbackContext):
    photo = await update.message.photo[-1].get_file()
    image_path = "input.jpg"
    await photo.download_to_drive(image_path)  # FIXED HERE ✅

    await update.message.reply_text("Removing background, please wait...")
    output_path = remove_bg(image_path)

    if output_path:
        await update.message.reply_photo(photo=open(output_path, "rb"))
        os.remove(output_path)
    else:
        await update.message.reply_text("Failed to remove background. Try again later.")

    os.remove(image_path)



def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    app.run_polling()


if __name__ == "__main__":
    main()
