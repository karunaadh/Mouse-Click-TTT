import turtle as t
#-------------------------------------
t.ht()
def basics():
  #turtle speed
  t.speed(0)
  #-----------------
  #turtle pensize
  t.pensize(4)
  #-----------------
  #background
  background = t.getscreen()
  background.bgcolor("white")
basics()

#--------------------------------------
#go somewhere
def travel (x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()

#--------Board---------
#board background
boardx = -150
boardy = 150
def boardback():
  t.color("light coral")
  travel(boardx,boardy)
  t.begin_fill()
  for i in range (4):
    t.forward(300)
    t.right(90)
  t.end_fill()
boardback()

#board lines
def boardlines():
  t.color("white")
  #horizontal
  for i in range (1,3):
    travel ((boardx), (boardy) - (i*100))
    t.forward(300)
  #turn right
  t.right(90)
  #vertical
  for j in range (1,3):
    travel(boardx + (j*100), boardy)
    t.forward(300)
boardlines()

#board numbers
def boardnum (num):
  t.color("white")
  for i in range (3):
    for j in range (3):
      travel ((boardx+85) + (j*100), (boardy-12) - (i*100))
      t.write(num)
      num +=1  
boardnum(1)

#-------X AND O and QUIT-------
#o
def drawo (x, y):
  t.color("white")
  travel(x, y)
  t.circle(30)

#x
def drawx(x, y):
  t.color("white")
  t.left(45)
  travel (x+10, y+25)
  t.forward(65)
  travel(x+55, y+25)
  t.right(90)
  t.forward(65)
  t.left(90)
  t.right(45)


#quit button 
def drawquit():
  t.color("light cyan")
  travel(boardx+400, boardy -260)
  t.begin_fill()
  for i in range (2):
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.right (90)
  t.end_fill()
  t.color("midnight blue")
  travel(boardx+357, boardy-284)
  t.write("QUIT", font=("Calibri", 10, "bold"))
drawquit()

#----------Winner display ---------
def winnerdisplay (winner):
  travel(boardx+25, boardy-100)
  t.color(224, 255, 255, 0.75) #light cyan, less opacity
  t.begin_fill()
  for i in range (2):
    t.forward(100)
    t.left(90)
    t.forward(250)
    t.left(90)
  t.end_fill()
  travel (boardx+60, boardy-155)
  t.color("midnight blue") 
  t.write (winner, font=("Calibri", 17, "bold"))


#--------------------------------LOGIC------------------------
#places
places = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#draw x and o where there is x and o
def drawxo(places):
  x = boardx + 20
  y = boardy - 50
  for place in places:
    if place == "x":
      drawx(x, y)
    elif place == "o":
      drawo(x, y)
    x += 100
    if x > boardx + 220:
      x = boardx + 20
      y -= 100

#-----------MOUSE CLICK EVENTS--------------
#screen
screen = t.Screen()
quit = False

#X AND O CLICK FUNCTIONALITY
xcord = None
ycord = None

#QUIT FUNCTIONALITY
def gameend(x, y):
  if (x >= (boardx + 338) and x <= (boardx+400) and y <= (boardy-258) and y >= (boardy-300)):
    global quit
    quit = True
  global xcord, ycord
  xcord = x
  ycord = y

#send click info
screen.onscreenclick(gameend)

#turn
turn = 0

#player1 = x. player2 = o.
def player1():
  if turn % 2 == 1:
      return False
  else:
      return True

#FUNCTION to put x and o on the list according to (x, y), and change turn
def drawvisuals(minx, maxx, miny, maxy, square):
  if (places[square] != "x" and places[square] != "o") and (xcord >= minx and xcord <= maxx and ycord >= miny and ycord <= maxy):
    global turn
    if player1():
      places[square] = "x"
    else:
      places[square] = "o"
    turn += 1


#MAIN LOOP 
while True:
  #quit button
  if quit:
    winnerdisplay("Thanks for playing!")
    break

  #put x and o on list according to coordinates, change turn
  drawvisuals(boardx, boardx+100, boardy-100, boardy, 0)
  drawvisuals(boardx+100, boardx+200, boardy-100, boardy, 1)
  drawvisuals(boardx+200, boardx+300, boardy-100, boardy, 2)
  drawvisuals(boardx, boardx+ 100, boardy-200, boardy-100, 3)
  drawvisuals(boardx + 100, boardx+200, boardy-200, boardy-100, 4)
  drawvisuals(boardx + 200, boardx+300, boardy-200, boardy-100, 5)
  drawvisuals(boardx, boardx+100, boardy-300, boardy-200, 6)
  drawvisuals(boardx+100, boardx+200, boardy-300, boardy-200, 7)
  drawvisuals(boardx+200, boardx+300, boardy-300, boardy-200, 8)
  #draw x and o according to list
  drawxo(places)  

  #check for win
  if (places[0] == places[1] == places[2]) or (places[3] == places[4] == places[5]) or (places[6] == places[7] == places[8]) or (places[0] == places[3] == places[6]) or (places[1] == places[4] == places[7]) or (places[2] == places[5] == places[8]) or (places[0] == places[4] == places[8]) or (places[2] == places[4] == places[6]):
    if player1():
      print ("Player 2 won!")
      winnerdisplay("     Player 2 won!")
    else:
      print ("Player 1 won!")
      winnerdisplay("     Player 1 won!")
    break
  
  if turn >= 9:
    winnerdisplay("          It's a tie.")
    print ("It's a tie.")
    break

  screen.update()  


print ("Thanks for playing!")
