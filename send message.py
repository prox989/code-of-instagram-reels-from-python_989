import pyautogui as pg

import time

time.sleep(10)

for i in range (100):

    for i in range (1):

        with pg.hold('ctrl'):

            pg.press('tab')

        pg.write('follow @python_989')

        pg.press('enter')