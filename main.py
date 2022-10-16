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
l = window.left
t = window.top

gridLeft = l + 15
gridTop = t + 101

columns = int((width - 30) / 16)
rows = int((height - 116) / 16)

print(f"Game Size:\nRows={rows}\nColums={columns}")

# all the different things that will appear
# non-numbers:
flag = "Buttons/flag.png"
emptySpace = "Buttons/emptySpace.png"
unchecked = "Buttons/unchecked.png"
mine = "Buttons/mine.png"
hitMine = "Buttons/hitMine.png"
wrongFlag = "Buttons/wrongFlag.png"
# numbers:
one = "Buttons/one.png"
two = "Buttons/two.png"
three = "Buttons/three.png"
four = "Buttons/four.png"
five = "Buttons/five.png"
six = "Buttons/six.png"
seven = "Buttons/seven.png"
eight = "Buttons/eight.png"
# misc
win = "Buttons/win.png"
lose = "Buttons/lose.png"
reset = "Buttons/reset.png"

btnList = [unchecked, emptySpace, one, two, three, four, five, six, seven, eight, flag, mine, hitMine, wrongFlag]

"""
try:
    leftBorder = pg.locateOnScreen("Buttons/leftBorder.png", region)
    topBorder = pg.locateOnScreen("Buttons/topBorder.png", region)
except TypeError:
    print("Window not open. Try again with the window visible on the screen")
    window.activate()
    window.restore()
    quit()
"""



def cell(box, t):
    left = box[0] - gridLeft
    top = box[1] - gridTop
    center = pg.center(box)
    row = top // 16
    column = left // 16


    type = {
        unchecked: 'U', emptySpace: 'E', one: '1', two: '2', three: '3', four: '4', five: '5',
        six: '6', seven: '7', eight: '8', flag: 'F', mine: 'M', hitMine: 'H', wrongFlag: 'W'
    }

    d = {
        "row": row,
        "column": column,
        "type": type[t],
        "point": (row, column),
        "center": center
    }

    return d


flagList = []


def click(r, c, g):
    for i in g:
        if i["point"] == (r, c):
            pg.click(i["center"])


def newGame():
    try:
        pg.click(reset)
    except:
        try:
            pg.click(win)
        except:
            pg.click(lose)


def scan():
    grid = []
    for x in btnList:
        for i in pg.locateAllOnScreen(x):
            grid.append(cell(i, x))
    return grid


def square(r, c):
    threeXthree = [(r + 1, c - 1), (r + 1, c), (r + 1, c + 1),
                   (r, c - 1), (r, c), (r, c + 1),
                   (r - 1, c - 1),(r - 1, c), (r - 1, c + 1)]
    return threeXthree


def showGame(g):
    for x in g:
        if x['column'] == columns-1:
            print(f" {x['type']} ")
        else:
            print(f" {x['type']} ", end='')


def main():
    global flagList

    toprow = [i for i in flagList if i['row'] == 0]
    # print(toprow)
    grid = scan()
    game = []
    for x in grid:
        game.append({'type': x['type'], 'row': x['row'], 'column': x['column'], 'point': x["point"]})
    game = sorted(game, key=lambda d: d['point'])
    showGame(game)

"""
    test = [i['type'] for i in game if i['point'] in square(6, 3)]
    for i, x in enumerate(test):
        if i in (5, 2):
            print(f" {x} ")
        else:
            print(f" {x} ", end='')
"""


if __name__ == '__main__':
    main()
