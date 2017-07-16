# Fix your variable names

import random
import getch
global X
global Y
X= 0
Y= random.randint(0,9)
boss_horizontal_x= random.randint(15,24)
boss_horizontal_y= random.randint(0,9)
boss_vertical_x= random.randint(15,24)
boss_vertical_y= random.randint(0,9)
left = True
down = True
bomb_x=None
bomb_y=None	
global game_map
global count
count=0
boss_vertical=True
boss_horizontal=True


def gen_map():
    global game_map
    game_map=[['.']*25 for _ in range(10)]
    
def print_map():
    
    for a in range(10):
        for boss in range(25):
            print game_map[a][boss],
        print '\n'
    print '\n'
    

def assign_player():
    global game_map
    if game_map[Y][X]=='.': 
       game_map[Y][X]='$'

def set_traps(n):
    for boss in range(n):
    	x=random.randint(2,14)
    	y=random.randint(0,3)
        for assign in range(7):
            if game_map[y+assign][x]=='.':
                game_map[y+assign][x]='#'


def assign_boss_vertical():
    global boss_vertical_x
    global boss_vertical_y
    global boss_vertical
    if boss_vertical:
       if game_map[boss_vertical_y][boss_vertical_x]=='.' or game_map[boss_vertical_y][boss_vertical_x]=='@'  :
           game_map[boss_vertical_y][boss_vertical_x]='@'

def assign_boss_horizontal():
    global boss_horizontal_x
    global boss_horizontal_y
    global boss_horizontal
    if boss_horizontal:
       if game_map[boss_horizontal_y][boss_horizontal_x]=='.' or game_map[boss_horizontal_y][boss_horizontal_x]=='@':
           game_map[boss_horizontal_y][boss_horizontal_x]='@'

def move_boss_horizontal():
    global boss_horizontal_x
    global boss_horizontal_y
    global left
    if boss_horizontal_x >15 and boss_horizontal_x <24:
        if left:
           game_map[boss_horizontal_y][boss_horizontal_x]='.'
           boss_horizontal_x-=1
           assign_boss_horizontal()
        else:
           game_map[boss_horizontal_y][boss_horizontal_x]='.'
           boss_horizontal_x+=1
           assign_boss_horizontal()
            
    elif boss_horizontal_x==15:
        game_map[boss_horizontal_y][boss_horizontal_x]='.'
        boss_horizontal_x+=1
        assign_boss_horizontal()
        left = False
    elif boss_horizontal_x==24:
        game_map[boss_horizontal_y][boss_horizontal_x]='.'
        boss_horizontal_x-=1
        assign_boss_horizontal()
        left = True


def move_boss_vertical():
    global boss_vertical_x
    global boss_vertical_y
    global down
    if boss_vertical_y>0 and boss_vertical_y <9:
        if down:
           game_map[boss_vertical_y][boss_vertical_x]='.'
           boss_vertical_y-=1
           assign_boss_vertical()
        else:
           game_map[boss_vertical_y][boss_vertical_x]='.'
           boss_vertical_y+=1
           assign_boss_vertical()
            
    elif boss_vertical_y==0:
        game_map[boss_vertical_y][boss_vertical_x]='.'
        boss_vertical_y+=1
        assign_boss_vertical()
        down = False
    elif boss_vertical_y==9:
        game_map[boss_vertical_y][boss_vertical_x]='.'
        boss_vertical_y-=1
        assign_boss_vertical()
        down = True

#Movement functions

def u():
    global X
    global Y
    if Y>0:
        if not game_map[Y][X]=='*':
            game_map[Y][X]='.'
        Y-=1
        if check():
            assign_player()
            move_boss_horizontal()
            move_boss_vertical()
            print_map()

        else:
            end_game() 
    if Y==0:
	pass
        move_boss_horizontal()
        move_boss_vertical()
        print_map()

def d():
    global X
    global Y
    if Y<9:
        if not game_map[Y][X]=='*':
            game_map[Y][X]='.'
        Y+=1
        if check():
            assign_player()
            move_boss_horizontal()
            move_boss_vertical()
            print_map()
        else:
            end_game()   
    if Y==9:
	pass
        move_boss_horizontal()
        move_boss_vertical()
        print_map()

def l():
    global X
    global Y
    if X>0:
        if not game_map[Y][X]=='*':
            game_map[Y][X]='.'
        X-=1
        if check():
            assign_player()
            move_boss_horizontal()
            move_boss_vertical()
            print_map()

        else:
            end_game()
    elif X==0:
	pass
        move_boss_horizontal()
        move_boss_vertical()
        print_map()
      
def r():
    global X
    global Y
    if X<24:
        if not game_map[Y][X]=='*':
            game_map[Y][X]='.'
        X+=1
        if check():
            assign_player()
            move_boss_horizontal()
            move_boss_vertical()
            print_map()

        else:
            end_game()   
    if X==24:
	pass
        move_boss_horizontal()
        move_boss_vertical()
        print_map()


    
def check():
    global X
    global Y
    global game_map
    if game_map[Y][X]=='.':
        return True
    else:
        return False


def end_game():
    global done
    print " game over"
    done = True

def plant_bomb():
    global bomb_x
    global bomb_y
    bomb_x=X
    bomb_y=Y
    game_map[bomb_y][bomb_x]='*'

def detonate_bomb():
    global bomb_x
    global bomb_y
    global count
    global boss_vertical
    global boss_horizontal
    game_map[bomb_y][bomb_x]='.'
    if bomb_y<9:
        if game_map[bomb_y+1][bomb_x]=='@':
            if bomb_y+1==boss_vertical_y and bomb_x == boss_vertical_x:
               boss_vertical=False
            elif bomb_y+1==boss_horizontal_y and bomb_x == boss_horizontal_x:
               boss_horizontal=False
            game_map[bomb_y+1][bomb_x]='.'
            count+=1 
        if game_map[bomb_y+1][bomb_x]=='$':
            end_game()
        if not game_map[bomb_y+1][bomb_x]=='$':
            game_map[bomb_y+1][bomb_x]='.'
		
    if bomb_x <24:
    	if game_map[bomb_y][bomb_x+1]=='@':
            if bomb_y==boss_vertical_y and bomb_x+1 == boss_vertical_x:
               boss_vertical=False
            elif bomb_y==boss_horizontal_y and bomb_x+1 == boss_horizontal_x:
               boss_horizontal=False
            game_map[bomb_y][bomb_x+1]='.'
            count+=1 
        if game_map[bomb_y][bomb_x+1]=='$':
            end_game()
        if not game_map[bomb_y][bomb_x+1]=='$':
            game_map[bomb_y][bomb_x+1]='.'
		
    if bomb_y >0:
    	if game_map[bomb_y-1][bomb_x]=='@':
            if bomb_y-1==boss_vertical_y and bomb_x == boss_vertical_x:
               boss_vertical=False
            elif bomb_y-1==boss_horizontal_y and bomb_x == boss_horizontal_x:
               boss_horizontal=False
            game_map[bomb_y-1][bomb_x]='.'
            count+=1 
        if game_map[bomb_y-1][bomb_x]=='$':
            end_game()
        if not game_map[bomb_y-1][bomb_x]=='$':
            game_map[bomb_y-1][bomb_x]='.'
		
    if bomb_x > 0:	
    	if game_map[bomb_y][bomb_x-1]=='@':
            if bomb_y==boss_vertical_y and bomb_x-1 == boss_vertical_x:
               boss_vertical=False
            elif bomb_y==boss_horizontal_y and bomb_x-1== boss_horizontal_x:
               boss_horizontal=False
            game_map[bomb_y][bomb_x-1]='.'
            count+=1 
        if game_map[bomb_y][bomb_x-1]=='$':
            end_game()	
        if not game_map[bomb_y][bomb_x-1]=='$':
            game_map[bomb_y][bomb_x-1]='.'
		    
    print_map()
    if count==2:
         print " You win "
         end_game()

instructions="""Objective: Destroy the enemies to win
                Controls: u-> up
                          d-> down
                          r-> right
                          l-> left
                          p-> plant bomb
                        space-> detonate bomb
                          q -> quit"""

gen_map()
assign_player()
set_traps(3)
assign_boss_vertical()
assign_boss_horizontal()
print instructions
print_map()


global done
done=False

while not done:
    A=getch.getch()
    if A=='w':
        u()
    elif A=='s':
        d()
    elif A=='a':
        l()
    elif A=='d':
        r()
    elif A=='p':
        plant_bomb()
    elif A==' ':
        detonate_bomb()
    elif A=='q':
        done=True
