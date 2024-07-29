import pyperclip
import keyboard
import os
import json
from openai import OpenAI
# from plyer import notification



if os.path.exists('./config.json'):
    with open('./config.json') as configFile:
        config = json.load(configFile)
else:
    with open('./config.json', 'w') as configFile:
        configFile.write(json.dumps({
            "shortcut": "ctrl+shift+k",
            "openai-model": "gpt-4o-mini",
            "openai-api-key": "ENTER YOUR OPENAI API KEY HERE",
            "instructions": "correct this text and return just the corrected text: "
        }))

        # notification.notify(
        #     title='AI Copy Correct',
        #     message='Please enter your api key in the config file.',
        #     app_name='AI Copy Correct',
        #     timeout=8
        # )

client = OpenAI(api_key=config['openai-api-key'])


def correct_text():
    clipboard_text = pyperclip.paste()

    completion = client.chat.completions.create(
        model=config['openai-model'],
        messages=[
            {"role": "user", "content": config["instructions"]+clipboard_text}
        ]
    )

    pyperclip.copy(completion.choices[0].message.content)


    # notification.notify(
    #     title='AI Copy Correct',
    #     message='Corrected Text coppied to clipboard.',
    #     app_name='AI Copy Correct',
    #     timeout=8
    # )


keyboard.add_hotkey(config['shortcut'], correct_text)


# notification.notify(
#     title='AI Copy Correct',
#     message='The Program is running in the background.',
#     app_name='AI Copy Correct',
#     timeout=6
# )

keyboard.wait('ctrl+shift+esc')