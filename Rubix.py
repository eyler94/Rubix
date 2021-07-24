#!/usr/bin/env python3
import numpy as np
from PIL import Image, ImageDraw
def NewBrick():
    brick = np.zeros([5,5,5],dtype=int)
    brick[0,1:4,1:4] = 1 #init red on top
    brick[-1,1:4,1:4] = 2 #init orange on bottom
    brick[1:4,1:4,0] = 5 #init blue on left
    brick[1:4,1:4,-1] = 4 #init green on right
    brick[1:4,0,1:4] = 3 #init yellow on back
    brick[1:4,-1,1:4] = 6 #init white on front
    return brick
def Rotate(face,rot,cw):
    if(cw=="y"):
        cw = 1
    elif(cw=="n"):
        cw = -1
    if face == "top":
        for spot in range(2):
            brick[spot,:,:] = np.rot90(brick[spot,:,:],cw*rot)
    elif face == "bottom":
        for spot in range(-1,-3,-1):
            brick[spot,:,:] = np.rot90(brick[spot,:,:],cw*rot)
    elif face == "front":
        for spot in range(-1,-3,-1):
            brick[:,spot,:] = np.rot90(brick[:,spot,:],cw*rot)
    elif face == "back":
        for spot in range(2):
            brick[:,spot,:] = np.rot90(brick[:,spot,:],cw*rot)
    elif face == "left":
        for spot in range(2):
            brick[:,:,spot] = np.rot90(brick[:,:,spot],cw*rot)
    elif face == "right":
        for spot in range(-1,-3,-1):
            brick[:,:,spot] = np.rot90(brick[:,:,spot],cw*rot)
    print(brick)
def plotBlock(target_img, x_spot, y_spot, color):
    x, y = 50*x_spot, 50*y_spot
    shape = [(x, y), (x+50, y+50)]
    img1 = ImageDraw.Draw(target_img)
    img1.rectangle(shape, fill = color, outline ="black")
w, h = 450, 600
colors = ["black", "red", "orange", "yellow", "green", "blue", "white"]
img = Image.new("RGB", (w, h))
def PlotCube():
    for y in range(3):#Plot back
        for x in range(3,6):
            plotBlock(img,x,y,colors[brick[1:4,0,1:4][2-y][x-3]])
    for y in range(3,6):#Plot left
        for x in range(3):
            plotBlock(img,x,y,colors[brick[1:4,1:4,0][2-x][y-3]])
    for y in range(3,6):#Plot top
        for x in range(3,6):
            plotBlock(img,x,y,colors[brick[0,1:4,1:4][y-3][x-3]])
    for y in range(3,6):#Plot right
        for x in range(6,9):
            plotBlock(img,x,y,colors[brick[1:4,1:4,-1][x-6][y-3]])
    for y in range(6,9):#Plot front
        for x in range(3,6):
            plotBlock(img,x,y,colors[brick[1:4,-1,1:4][y-6][x-3]])
    for y in range(9,12):#Plot bottom
        for x in range(3,6):
            plotBlock(img,x,y,colors[brick[-1,1:4,1:4][11-y][x-3]])
    img.show()
brick = NewBrick()
userArg = ""
while userArg != "exit" or userArg != "3":
    userArg = input("What action would you like? (1. new 2. rotate 3. exit)")
    if(userArg == "1" or userArg == "new"):
        brick = NewBrick()
    elif(userArg == "2" or userArg == "rotate"):
        try:
            face = input("Which face? (top, bottom, front, back, left, right)")
            turns = int(input("how many turns?"))
            cw = input("Clockwise? (y or n)")
            Rotate(face,turns,cw)
        except:
            print("Please try again")
    elif(userArg == "exit" or userArg == "3"):
        break
    PlotCube()
