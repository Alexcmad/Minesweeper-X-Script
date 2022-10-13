import pyautogui as pg

def main():
    flag = pg.locateOnScreen('Buttons/flag.png')
    unchecked = pg.locateCenterOnScreen('Buttons/lose.png')
    print(unchecked)

if __name__ == '__main__':
    main()