# Version: 1.0.1
# Currently not working perfectly, but it's a start.
# I recommend using a US keyboard layout, as I have tested it with other layouts and it doesn't work as well.
# If you have any suggestions, on how to improve this, please let me know.

from pyperclip import paste
from pyperclip import pyperclip
from pyautogui import typewrite
from pyautogui import pyautogui
from keyboard import add_hotkey
from keyboard import keyboard
from time import sleep


def vncpaste():
    text_to_write = pyperclip.paste()
    # The print() function is used for debugging, uncomment it if you have any issues. (It will print the clipboard contents to the console)
    # print(text_to_write)
    sleep(0.5)  # Code was unstable without this little delay, so I added it.
    pyautogui.typewrite(text_to_write)


# If you want to use a different hotkey, change this line, remember to have a hotkey that doesn't conflict with the host OS, and remember to seperate the keys with a plus sign "+"
keyboard.add_hotkey("ctrl+alt+v", vncpaste)

print("VNCP by Truz#6978")
print("2023-02-12 - 1.0.1")

keyboard.wait()
