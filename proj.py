import random
global X
global Y
X=0
Y=random.randint(0,9)
b_h_x=random.randint(15,24)
b_h_y=random.randint(0,9)
b_v_x=random.randint(15,24)
b_v_y=random.randint(0,9)
left = True
down = True
bomb_x=None
bomb_y=None	
global game_map
global count
count=0
b_v=True
b_h=True
def gen_map():
    global game_map
    game_map=[['.']*25 for _ in range(10)]
    
def print_map():
    for a in range(10):
        for b in range(25):
            print game_map[a][b],
        print '\n'

def assign_player():
    global game_map
    if game_map[Y][X]=='.': 
       game_map[Y][X]='$'

def set_traps(n):
    for b in range(n):
    	x=random.randint(2,14)
    	y=random.randint(0,3)
        for a in range(7):
            if game_map[y+a][x]=='.':
                game_map[y+a][x]='#'

def a_b_v():
    global b_v_x
    global b_v_y
    global b_v
    if b_v:
       if game_map[b_v_y][b_v_x]=='.' or game_map[b_v_y][b_v_x]=='@'  :
           game_map[b_v_y][b_v_x]='@'

def a_b_h():
    global b_h_x
    global b_h_y
    global b_h
    if b_h:
       if game_map[b_h_y][b_h_x]=='.' or game_map[b_h_y][b_h_x]=='@':
           game_map[b_h_y][b_h_x]='@'

def m_b_h():
    global b_h_x
    global b_h_y
    global left
    if b_h_x >15 and b_h_x <24:
        if left:
           game_map[b_h_y][b_h_x]='.'
           b_h_x-=1
           a_b_h()
        else:
           game_map[b_h_y][b_h_x]='.'
           b_h_x+=1
           a_b_h()
            
    elif b_h_x==15:
        game_map[b_h_y][b_h_x]='.'
        b_h_x+=1
        a_b_h()
        left = False
    elif b_h_x==24:
        game_map[b_h_y][b_h_x]='.'
        b_h_x-=1
        a_b_h()
        left = True


def m_b_v():
    global b_v_x
    global b_v_y
    global down
    if b_v_y>0 and b_v_y <9:
        if down:
           game_map[b_v_y][b_v_x]='.'
           b_v_y-=1
           a_b_v()
        else:
           game_map[b_v_y][b_v_x]='.'
           b_v_y+=1
           a_b_v()
            
    elif b_v_y==0:
        game_map[b_v_y][b_v_x]='.'
        b_v_y+=1
        a_b_v()
        down = False
    elif b_v_y==9:
        game_map[b_v_y][b_v_x]='.'
        b_v_y-=1
        a_b_v()
        down = True
def u():
    global X
    global Y
    if Y>0:
        if not game_map[Y][X]=='*':
            game_map[Y][X]='.'
        Y-=1
        if check():
            assign_player()
            m_b_h()
            m_b_v()
            print_map()

        else:
            end_game() 
    if Y==0:
	pass
        m_b_h()
        m_b_v()
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
            m_b_h()
            m_b_v()
            print_map()
        else:
            end_game()   
    if Y==9:
	pass
        m_b_h()
        m_b_v()
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
            m_b_h()
            m_b_v()
            print_map()

        else:
            end_game()
    elif X==0:
	pass
        m_b_h()
        m_b_v()
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
            m_b_h()
            m_b_v()
            print_map()

        else:
            end_game()   
    if X==24:
	pass
        m_b_h()
        m_b_v()
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

def p_bomb():
    global bomb_x
    global bomb_y
    bomb_x=X
    bomb_y=Y
    game_map[bomb_y][bomb_x]='*'

def det_bomb():
    global bomb_x
    global bomb_y
    global count
    global b_v
    global b_h
    game_map[bomb_y][bomb_x]='.'
    if bomb_y<9:
        if not game_map[bomb_y+1][bomb_x]=='$':
            game_map[bomb_y+1][bomb_x]='.'
        elif game_map[bomb_y+1][bomb_x]=='@':
            if bomb_y+1==b_v_y and bomb_x == b_v_x:
               b_v=False
            elif bomb_y+1==b_h_y and bomb_x == b_h_x:
               b_h=False
            game_map[bomb_y+1][bomb_x]='.'
            count+=1 
        else:
            end_game()
    if bomb_x <24:
    	if not game_map[bomb_y][bomb_x+1]=='$':
            game_map[bomb_y][bomb_x+1]='.'
        elif game_map[bomb_y][bomb_x+1]=='@':
            if bomb_y==b_v_y and bomb_x+1 == b_v_x:
               b_v=False
            elif bomb_y==b_h_y and bomb_x+1 == b_h_x:
               b_h=False
            game_map[bomb_y][bomb_x+1]='.'
            count+=1 
        else:
            end_game()
    if bomb_y >0:
    	if not game_map[bomb_y-1][bomb_x]=='$':
            game_map[bomb_y-1][bomb_x]='.'
        elif game_map[bomb_y-1][bomb_x]=='@':
            if bomb_y-1==b_v_y and bomb_x == b_v_x:
               b_v=False
            elif bomb_y-1==b_h_y and bomb_x == b_h_x:
               b_h=False
            game_map[bomb_y-1][bomb_x]='.'
            count+=1 
        else:
            end_game()
    if bomb_x > 0:	
    	if not game_map[bomb_y][bomb_x-1]=='$':
            game_map[bomb_y][bomb_x-1]='.'
        elif game_map[bomb_y][bomb_x-1]=='@':
            if bomb_y==b_v_y and bomb_x-1 == b_v_x:
               b_v=False
            elif bomb_y==b_h_y and bomb_x-1 == b_h_x:
               b_h=False
            game_map[bomb_y][bomb_x-1]='.'
            count+=1 
        else:
            end_game()	    
    print_map()
    if count==2:
         print " You win"

instructions="""Objective: Destroy the enemies to win
                Controls: u-> up
                          d-> down
                          r-> right
                          l-> left
                          p-> plant bomb
                        det-> detonate bomb"""

gen_map()
assign_player()
set_traps(3)
a_b_v()
a_b_h()
print instructions
print_map()


global done
done=False

while not done:
    A=raw_input(" ")
    if A=='u':
        u()
    elif A=='d':
        d()
    elif A=='l':
        l()
    elif A=='r':
        r()
    elif A=='p':
        p_bomb()
        print 'Now move in any direction'
    elif A=='det':
        det_bomb()
    elif A=='quit':
        done=True
