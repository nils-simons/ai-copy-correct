import pyperclip
import keyboard
from openai import OpenAI
from win10toast import ToastNotifier

toaster = ToastNotifier()

client = OpenAI(api_key='API_KEY')

def correct_text():
    clipboard_text = pyperclip.paste()
    # print("Clipboard Text:", clipboard_text)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": 'correct this text and return just the corrected text: '+clipboard_text}
        ]
    )

    # print(completion.choices[0].message.content)

    pyperclip.copy(completion.choices[0].message.content)


    toaster.show_toast(
        "AIAC",
        "Corrected Text coppied to clipboard.",
        duration=2,
    )


keyboard.add_hotkey('ctrl+shift+k', correct_text)

input('')