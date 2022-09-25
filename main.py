import time
import pyautogui as pt


class Clicker:

    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        items = ['images/img1.png',
                 'images/img2.png',
                 'images/img3.png',
                 'images/img4.png',
                 'images/img5.png']

        try:
            for item in items:
                position = pt.locateOnScreen(item, confidence=.7)

                if position is None:
                    global counter
                    counter = counter + 1
                    if counter == 30:
                        pt.click(939, 957, 3, button="left")
                        counter = 0

                pt.moveTo(position[0] + 25, position[1] + 25, duration=self.speed)
                pt.doubleClick()
                time.sleep(2.5)
        except:
            print('No image found...')
            time.sleep(0.1)
            return 0


if __name__ == '__main__':
    time.sleep(3)
    # Initialises the clicker
    clicker = Clicker('images/img1.png', speed=.001)

    counter = 0
    while True:
        clicker.nav_to_image()