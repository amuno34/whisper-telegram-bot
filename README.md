# Whisper AI powered Telegram Bot
Speech to Text Telegram bot using the Whisper AI model made by OpenAI.

## TO DO:
- Port the code to a newer version of python-telegram-bot
- Get around the 50MB download limit that the Telegram API imposes
- Optimize the code in general
- Getting the LOGMMSE algorithm working for audios with a lot of noise
- Making a better documentation

## Setting up
You need to install the [python-telegram-bot v13.7](https://github.com/python-telegram-bot/python-telegram-bot), [WhisperAI](https://github.com/openai/whisper) and the [ffmpeg](https://github.com/kkroening/ffmpeg-python) packages with pip.

If you want to experiment with [LOGMMSE](https://pypi.org/project/logmmse/) install that package too.

## Running the bot
Just change the `PUT_YOUR_TOKEN_HERE` in the `TOKEN` variable with the bot token you created with Botfather.

Then with Python just run the `main.py` file.

## Contributions
I will read and test almost all the contributions you make.

## Special thanks
Special thanks to [x7429](https://github.com/x7429) for inviting me to continue this little project of mine.

