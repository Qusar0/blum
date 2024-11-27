from mss import mss
import numpy
import pyautogui as pg
import keyboard
import time

mss = mss()
monitor = {
    "left": 0,
    "top": 150,
    "width": 380,
    "height": 500    
}

def find_color_in_image(img_arr, color):
    o_map = (color[0], color[1], color[2], 255)
    indexes = numpy.where(numpy.all(img_arr == o_map, axis=-1))
    if indexes[0].size > 0:
        return (indexes[0][0], indexes[1][0]) 
    return None

# b g r
colors = [
    [233, 221, 130],
    [0, 220, 205],
    [255, 255, 255]
]

# Время последнего клика
last_click_time = time.time()

while True:
    if keyboard.is_pressed('q'):
        print("Выход из программы.")
        break

    img = mss.grab(monitor)
    img_arr = numpy.array(img)

    for color in colors:
        result = find_color_in_image(img_arr, color)
        if result:
            x = result[1] + monitor['left']
            y = result[0] + monitor['top']
            pg.click(x, y + 5)
            break

    current_time = time.time()
    if current_time - last_click_time >= 40:
        pg.click(180, 615)
        last_click_time = current_time

