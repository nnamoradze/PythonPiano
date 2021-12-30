
import pyautogui as pg
import time

print('გადადით "https://virtualpiano.net/"')
time.sleep(5)
delay = 0.03
with open('sheet.txt') as f:
    notes = f.read()
    index = 0
    while index in range(len(notes)):
        if notes[index].isalpha() or notes[index].isdigit():
            pg.press(notes[index])
        else:
            if notes[index] == '|':
                time.sleep(delay * 8)
            if notes[index] == '[':
                chord = []
                while notes[index] != ']':
                    if notes[index].isalpha() or notes[index].isdigit():
                        chord.append(notes[index])
                    index += 1
                exec('pg.hotkey(' + str(chord)[1: -1] + ')')
        time.sleep(delay)
        index += 1

