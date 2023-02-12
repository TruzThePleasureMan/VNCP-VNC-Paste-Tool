# VNCP

> One day the creator of this found out, I want to paste stuff into VNC sessions. So he created this.

VNCP is a simple tool to paste stuff into VNC sessions.

## Required software and libraries

- Python 3.6+
- Pyperclip
- PyAutoGUI
- Keyboard

Install the libraries with `pip install pyperclip pyautogui keyboard`.

## Usage

Run `py vncp.py` and press `CTRL + ALT + V` to paste the clipboard into the active VNC session.

If this hotkey does not suit you, you can change it in the `vncp.py` file.

## If you face any problems

I would recommend to change your keyboard layout to US. This is the only layout that I know for sure that works well with this tool.
Keyboard layouts like German or French might cause problems. Until I find a solution for it adapt to your keyboard layout.
Keep in mind that this tool is still in development.-

## Will this ever be a standalone application?

This tool might become an application in the future. But for now it has to become more robust.
