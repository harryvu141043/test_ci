y=2
x=2
flag=True
l = [['-' for y in range(4)] for x in range(4)]
l[y][x]='P'
l[2][3]="E"
l[1][2]="K"
print(l)
def array(m):
  
  for row in m:
        for col in row:
            print(col, end=' ')
        print(' ')
array(l)
def move():
  global flag
  global x
  global y 
  global l
  while flag == True:
    
    inpu = input('YOUR MOVE:')
    
    if inpu.lower() == 'w':
        if y==0:
            pass
        elif l[1][2]=="K" and l[2][3]=="E" and l[2][2]=="P":
            
            l[y][x]="-"
            y-=1
        
            print("You've just picked up a key !!!")
        elif "P"==l[3][3] and "K"==l[1][2]:
            l[y][x]="P"
            l[y-1][x]="E"
            print("You can't exit,please acquire the key(s) first")

        else:
            l[y][x] = '-'
            y -= 1
            
            
    elif inpu.lower() == 'a':
        if x==0:
            pass
        elif l[1][2]=="K" and l[2][3]=="E" and l[1][3]=="P":
            
            l[y][x]="-"
            x-=1
        
            print("You've just picked up a key !!!")
        else:
            l[y][x] = '-'
            x -= 1
        
    elif inpu.lower() == 's':
        if y==3:
            pass
        elif l[1][2]=="K" and l[2][3]=="E" and l[0][2]=="P":
            
            l[y][x]="-"
            y+=1
            print("You've just picked up a key !!!")
        elif "P"==l[1][3] and "K"==l[1][2]:
            l[y][x]="P"
            l[y+1][x]="E"
            print("You can't exit,please acquire the key(s) first")
        

        
        else:
            l[y][x] = '-'
            y += 1
            
    elif inpu.lower() == 'd':
        if x == 3:
            pass
        elif l[1][2]=="K" and l[2][3]=="E" and l[1][1]=="P":
            
            l[y][x]="-"
            x+=1
            print("You've just picked up a key !!!")
        elif "P"==l[2][2] and "K"==l[1][2]:
            l[y][x]="P"
            l[y][x+1]="E"
            print("You can't exit,please acquire the key(s) first")
            
        else:
            l[y][x] = '-'
            x += 1
    l[y][x] = 'P'
    array(l)
    # if l[1][2]!="K" and l[2][3]=="E":
        
    #     print("You've just picked up a key !!!")
    
    if l[2][3]!="E" and l[1][2]!="K":
        print("Congrats, you've just escaped the dungeon")
        break
    # if (l[3][3]=="P"or l[2][2]=="P" or l[1][3]=="P") and l[1][2]=="K":
    #     print("You can't exit,please acquire the key(s) first")
move()
