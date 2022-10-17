import pyautogui as pg
import pygetwindow as pw

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

print(f"Game Size:\nRows={rows}\nColumns={columns}")

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

numbers = [one, two, three, four, five, six, seven, eight]
btnList = [unchecked, emptySpace, flag, mine, hitMine, wrongFlag] + numbers


def cell(box, ty):
    left = box[0] - gridLeft
    top = box[1] - gridTop
    center = pg.center(box)
    row = top // 16
    column = left // 16

    typ = {
        unchecked: '-', emptySpace: ' ', one: '1', two: '2', three: '3', four: '4', five: '5',
        six: '6', seven: '7', eight: '8', flag: 'F', mine: '*', hitMine: '!', wrongFlag: 'x'
    }

    d = {
        "row": row,
        "column": column,
        "type": typ[ty],
        'raw': ty,
        "point": (row, column),
        "center": center
    }

    return d


def click(r, c, g,b):
    if b == 'l':
        for i in g:
            if i["point"] == (r, c):
                pg.click(i["center"])
    else:
        for i in g:
            if i["point"] == (r, c):
                pg.click(i["center"],button='right')

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
        for i in pg.locateAllOnScreen(x, confidence=0.99):
            grid.append(cell(i, x))
    return grid


def square(r, c):
    threeXthree = [(r + 1, c - 1), (r + 1, c), (r + 1, c + 1),
                   (r, c - 1), (r, c), (r, c + 1),
                   (r - 1, c - 1), (r - 1, c), (r - 1, c + 1)]
    return threeXthree


def showGame(g):
    for x in g:
        if x['column'] == columns - 1:
            print(f" {x['type']} ")
        else:
            print(f" {x['type']} ", end='')


def play(g):
    for i in g:
        r = i['row']
        c = i['column']
        if i['raw'] in numbers:
            v = int(i['type'])
            sq = square(r, c)
            uCount = []
            fCount = []

            for j in g:
                if j['raw'] == flag and j['point'] in sq:
                    fCount.append(j)
                if j['raw'] == unchecked and j['point'] in sq:
                    uCount.append(j)

            print(f'Value: {v}')
            print(f'uCount: {len(uCount)}')
            print(f'fCount: {len(fCount)}')

            if len(fCount) == v and uCount:
                print("YESF")
                for x in uCount:
                    click(x["row"], x["column"], g,'l')
                play(scan())
            elif len(uCount)-len(fCount) == v:
                print("YESU")
                for x in uCount:
                    click(x["row"], x["column"], g,'r')
                play(scan())

            else:
                print("NO")



def main():
    grid = scan()
    game = sorted(grid, key=lambda d: d['point'])
    #showGame(game)
    play(game)


if __name__ == '__main__':
    main()
