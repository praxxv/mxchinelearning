from pynput import keyboard
import csv
import time
import os
import sys

file_path = 'keystroke_datax.csv'
rows = []
key_data = {}
last_release_time = None
last_press_time = None
shift_pressed = False
digraph_latencies = {}

# Keys we do NOT want to store in dataset
excluded_keys_from_data = {
    keyboard.Key.esc,
    keyboard.Key.space,
    keyboard.Key.backspace,
    keyboard.Key.enter,
    keyboard.Key.caps_lock,
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.shift_l
}

def on_press(key):
    global last_press_time, shift_pressed

    if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
        shift_pressed = True

    now = time.time()

    # Display typed keys
    if hasattr(key, 'char') and key.char is not None:
        if shift_pressed and key.char in shift_symbol_map:
            print(shift_symbol_map[key.char], end='', flush=True)
        elif shift_pressed and key.char.isalpha():
            print(key.char.upper(), end='', flush=True)
        else:
            print(key.char, end='', flush=True)
    elif key == keyboard.Key.space:
        print(' ', end='', flush=True)
    elif key == keyboard.Key.backspace:
        sys.stdout.write('\b \b')
        sys.stdout.flush()
    elif key == keyboard.Key.enter:
        print()

    # Don't log excluded keys (but allow printing above)
    if key in excluded_keys_from_data:
        return

    try:
        k = key.char
        if k is not None and shift_pressed:
            if k.isalpha():
                k = k.upper()
            elif k in shift_symbol_map:
                k = shift_symbol_map[k]
    except AttributeError:
        k = str(key)

    key_data[k] = now

    # Digraph latency
    if last_press_time is not None:
        digraph_latencies[k] = now - last_press_time
    else:
        digraph_latencies[k] = 0.0

    last_press_time = now

def on_release(key):
    global last_release_time, shift_pressed

    if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
        shift_pressed = False

    if key == keyboard.Key.esc:
        file_exists = os.path.isfile(file_path)
        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Key', 'HoldTime', 'FlightTime', 'DigraphLatency'])
            writer.writerows(rows)
        print("\n\nData saved to", file_path)
        return False  # Exit listener

    if key in excluded_keys_from_data:
        return

    try:
        k = key.char
        if k is not None and shift_pressed:
            if k.isalpha():
                k = k.upper()
            elif k in shift_symbol_map:
                k = shift_symbol_map[k]
    except AttributeError:
        k = str(key)

    release_time = time.time()

    if k in key_data:
        hold_time = release_time - key_data[k]
        flight_time = release_time - last_release_time if last_release_time else 0.0
        digraph_latency = digraph_latencies.get(k, 0.0)
        last_release_time = release_time

        rows.append([k, round(hold_time, 4), round(flight_time, 4), round(digraph_latency, 4)])

# Shift symbol map
shift_symbol_map = {
    '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
    '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
    '`': '~', '-': '_', '=': '+', '[': '{', ']': '}',
    '\\': '|', ';': ':', "'": '"', ',': '<', '.': '>',
    '/': '?'
}

print("Typing... (Press ESC to stop and save)")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
