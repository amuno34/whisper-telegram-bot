from telegram.ext import Updater, MessageHandler, Filters
import os
from telegram.utils.request import Request
import telegram
import subprocess
import whisper
import requests

# Creating a bot object with token
TOKEN = 'PUT_YOUR_TOKEN_HERE'
request = Request(con_pool_size=8)
bot = telegram.Bot(token=TOKEN, request=request)

def handle_audio(update, context):
    #Getting the ID message of the bot
    file_id = update.message.audio.file_id
    file = bot.get_file(file_id)

    #Getting the audio extension
    file_extension = os.path.splitext(file.file_path)[1]
    file_extension_global = file_extension

    #Downloading the audio file
    file_name = f"{file_id}{file_extension}"
    file.download(file_name)

    # Changing format file and calling a subprocess for converting the downloaded message in WAV 
    file_output = f"{file_id}.wav"
    subprocess.call(['ffmpeg', '-i', file_name, file_output, '-y'])

    # Deleting the original file
    os.remove(file_name)
    
    # Calling the TTS function of the code
    tts_audio(update, context, file_id = file_output)


def tts_audio(update, context, file_id):
    # This section of the code is interacting directly with the Whisper AI segment
    # Choosing the model that the AI should use ("tiny","base","small","medium","large")
    model = whisper.load_model("small")

    # Getting the converted file as the input for the model
    result = model.transcribe(f"{file_id}")
    
    # Cleans the output of the model in a more understandable way
    output_text = result["text"]
    language_text = result["language"]
    final_text = "Language detected: {}\n\n{}".format(language_text,output_text)

    update.message.reply_text(final_text)

    # Deleting the converted audio file
    os.remove(file_id)

   
    


# Bot updater
updater = Updater(bot=bot, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.audio, handle_audio))


# Bot startup
updater.start_polling()
updater.idle()
