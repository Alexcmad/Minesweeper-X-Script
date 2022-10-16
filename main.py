import pyautogui as pg
import pygetwindow as pw
import PIL

try:
    window = pw.getWindowsWithTitle('Minesweeper X')[0]
except IndexError:
    print("Game Not Running")
    exit()

width = window.width
height = window.height
region = window.box

columns = int((width - 30) / 16)
rows = int((height - 116) / 16)

print(f"Game Size:\nRows={rows}\nColums={columns}")

game = []
for i in range(rows):
    game.append([])
    for j in range(columns):
        game[i].append([''])

for i in range(len(game)):
    for j in range(len(game[i])):
        game[i][j] = ('*')

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

try:
    leftBorder = pg.locateOnScreen("Buttons/leftBorder.png", region)
    topBorder = pg.locateOnScreen("Buttons/topBorder.png", region)
except TypeError:
    print("Window not open. Try again with the window visible on the screen")
    window.activate()
    window.restore()
    quit()

gridLeft = leftBorder[0] + leftBorder[2]
gridTop = topBorder[1] + topBorder[3]


def cell(box,type):
        left = box[0] - gridLeft
        top = box[1] - gridTop
        center = pg.center(box)
        row = top // 16
        column = left // 16

        d = {
            "row":row,
            "column":column,
            "type":type
        }

        return d


def main():

    flagList = [cell(i,'Flag') for i in pg.locateAllOnScreen(unchecked)]
    print(flagList)
    toprow = [i for i in flagList if i['row']==0]
    print(toprow)


if __name__ == '__main__':
    main()
