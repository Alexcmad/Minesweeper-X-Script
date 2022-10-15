import pyautogui as pg
import pygetwindow as pw
import PIL

window = pw.getWindowsWithTitle('Minesweeper X')[0]
width = window.width
height = window.height
region = window.box

columns = int((width - 30) / 16)
rows = int((height - 116) / 16)

game = []

# all the different things that will appear
# non-numbers:
flag = "Buttons/flag.png"
emptySpace = "Buttons/emptySpace.png"
unchecked = "Buttons/unchecked.png"
mine = "Buttons/mine.png"
hitMine = "Buttons/hitMine.png"
wrongFlag = "Buttons/wrongFlag.png"
reset = "Buttons/reset.png"
win = "Buttons/win.png"
lose = "Buttons/lose.png"
# numbers:
one = "Buttons/one.png"
two = "Buttons/two.png"
three = "Buttons/three.png"
four = "Buttons/four.png"
five = "Buttons/five.png"
six = "Buttons/six.png"
seven = "Buttons/seven.png"
eight = "Buttons/eight.png"


def printGame():
    for i in range (rows):
        game.append([])
        for j in range(columns):
            game[i].append('')
        print(game[i])
    print(game)


def main():
    for i in pg.locateAllOnScreen(unchecked, region=region):
        print(pg.center(i))
    printGame()


if __name__ == '__main__':
    main()
