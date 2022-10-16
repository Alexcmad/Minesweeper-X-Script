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
for i in range (rows):
    game.append([])
    for j in range (columns):
        game[i].append([''])


for i in range(len(game)):
    for j in range(len(game[i])):
        game[i][j]=('*')

for i in game:
    print(i)








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

leftBorder = pg.locateOnScreen("Buttons/leftBorder.png",region)
topBorder = pg.locateOnScreen("Buttons/topBorder.png",region)

gridLeft = leftBorder[0]+leftBorder[2]
gridTop = topBorder[1]+topBorder[3]

class cell:
    def __init__(self, box):
        self.box = box
        self.w = box[2]
        self.h = box[3]
        self.left = box[0] - gridLeft
        self.top = box[1] -gridTop
        self.center = pg.center(box)
        self.row = self.top//16
        self.column = self.left//16


def main():
    c1 = cell(pg.locateOnScreen(hitMine, region))
    print(f"{rows} {columns}")
    print(f"Top: {c1.top} Left: {c1.left} Row: {c1.row} Column: {c1.column}")


if __name__ == '__main__':
    main()
