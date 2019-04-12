
# l=[["- - - -"],"- - K -","- - P E","- - - -"]
# # random.shuffle(l)
# print(*l,sep="\n")
# while True:
#     q=input('your move:')
#     if q=="W":
#         l.remove("- - P E")
#         l.insert(2,"- - - E")
#         print(*l,sep='\n')
# board=[0,1,2,3,4,5,6,7,8,9,10,11,12]
# def printl_n(x1,x2,x3,x4):
#     print(board[x1],"|",board[x2],'|',board[x3],"|",board[x4])
# def show():
#     printl_n(0,1,2,4)
#     printl_n(5,6,7,8)
#     printl_n(9,10,11,12)
# show()
from random import randint
Welcome = input('Welcome To Dynamic Dungeon Escape!\nPress \'ENTER\' to begin.\n')

#global variables
randnum = randint(0, 6)
_randnum = randint(0, 6)
flag = True
_flag = [True, True, True, True, True, True]
score = 1000
highscore = 0
y =  3
x = 3
inpu = ''
gem_x = []
gem_y = []
  
#7 by 7 two-dimensional list
l = [['-' for y in range(4)] for x in range(4)]
print(l)

l[y][x] = 'P'
l[2][3]="E"
l[1][2]="K"


#functions
def array(m):
  '''
    function that prints the list in grid form
    
    l: two dimensional list
  '''
  for row in m:
    for col in row:
      print(col, end=' ')
    print('')
def check():
  global randnum
  global _randnum
  while randnum == 3 and _randnum == 3:
    randnum = randint(0, 6)
    _randnum = randint(0, 6)
def highest():
  global highscore
  global score
  if score >= highscore:
    highscore = score
  else: 
    highscore = highscore
def set_gem():
  global gem_x
  global gem_y
  gem_x = [randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6)]
  gem_y = [randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6)]

def reset():
  global randnum
  global _randnum
  randnum = randint(0, 6)
  _randnum = randint(0, 6)
  set_gem()
def restart():
  global flag
  global score
  global randnum
  global _randnum
  global y
  global x
  global health
  global _flag
  start = input('Would you like to restart? (y/n)')
  if start.lower() == 'n': 
    flag = False
  elif start.lower() == 'y':
    reset()
    health = 10
    score = 1000
    _flag = [True, True, True, True, True, True]
    l[y][x] = '-'
    y = 3
    x = 3
    l[y][x] = 'o'
    print('\n')
  else:
    print('invalid answer')
    restart()
def encounter():
  global x
  global y
  global gem_x
  global gem_y
  global _flag
  global score
  for i in range(0, len(gem_y)):
    if x == gem_x[i] and y == gem_y[i] and _flag[i] == True:
      print('You found a gem! (+25 points)')
      score += 25
      _flag[i] = False
def win():
  global randnum
  global _randnum
  global highscore
  global score
  if x == randnum and y == _randnum:
    l[y][x] = 'o'
    print('\n\n\n\nYou Have Escaped!!!')
    print('Score: ', score)
    highest()
    print('Highscore: ', highscore, '\n\n\n\n')
    restart()
print('-INSTRUCTIONS-\n-You are the \'O\' in the map of \'X\' below\n-To move, press \'ENTER\' after typing \'W\', \'A\', \'S\', or \'D\'\n-\'W\' = up, \'A\' = left, \'S\' = down, \'D\' = right\n-You cannot move off the map\n-Your objective is to find the exit to this dungeon, which could be anywhere\n')
array(l)
def move():
  global flag
  global x
  global y
  global o 
  global score
  global highscore
  global l
  global health
  while flag == True:
    check()
    inpu = input('')
    win()
    encounter()
    if inpu.lower() == 'w':
      if y == 0:
        pass
      else:
        l[y][x] = '-'
        y -= 1
        score -= 2
    elif inpu.lower() == 'a':
      if x == 0:
        pass
      else:
        l[y][x] = 'x'
        x -= 1
        score -= 2
    elif inpu.lower() == 's':
      if y == 6:
        pass
      else:
        l[y][x] = 'x'
        y += 1
        score -= 2
    elif inpu.lower() == 'd':
      if x == 6:
        pass
      else:
        l[y][x] = 'x'
        x += 1
        score -= 2
    else: 
      pass
    l[y][x] = 'o'
    array(l)
set_gem()
move()