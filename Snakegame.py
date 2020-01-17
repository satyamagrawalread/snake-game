import pygame
import random
import time
pygame.init()

rows=30
width=600
size=width//rows
level=[7,15,24,34,45]

screen=pygame.display.set_mode((width,width))
screen.fill((0,0,0))
pygame.display.set_caption("SNAKE GAME designed by SATYAM(urf BABU)")

def drawgrid(screen,width,rows):
    
    x=0
    y=0
    pygame.draw.line(screen,(255,255,255),(x,0),(x,width))
    pygame.draw.line(screen,(255,255,255),(0,y),(width,y))
    for i in range(rows):
        x+=size
        y+=size
        pygame.draw.line(screen,(255,255,255),(x,0),(x,width))
        pygame.draw.line(screen,(255,255,255),(0,y),(width,y))


def apple(x,y,size):
    pygame.draw.rect(screen,(255,0,0),[x,y,size,size])

clock=pygame.time.Clock()



def snakelength(size,snakelist):
    for X in snakelist:
        pygame.draw.rect(screen,(0,155,0),[X[0],X[1],size,size])

font=pygame.font.Font('freesansbold.ttf',32)
def message(msg,color,x,y):
    
    text=font.render(msg,True,color)
    screen.blit(text,(x,y))


def gameloop():
    global screen
    screen=pygame.display.set_mode((width,width))
    message("LEVEL: 1",(0,0,155),100, 300)
    pygame.display.update()
    time.sleep(2)
    screen.fill((0,0,0))

    snake1_x=round((width/2)/size)*size-size
    snake1_y=round((width/2)/size)*size-size
    snake1_x_change=0
    snake1_y_change=0
    apple_x=round(random.randrange(0,(width-size))/size)*size+size
    apple_y=round(random.randrange(0,(width-size))/size)*size+size
    snakelen=1
    snakelist=[]
    dirn="boss"
    fps=10

    running=True
    gameover=False
    while running:
        while gameover:
            message("YOU LOSE",(255,0,0),100,200)
            message("Press C to play again",(0,255,255),100,300)
            message("Or Press Q to Quit",(0,255,0),100,350)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        gameloop()
                    elif event.key==pygame.K_q:
                        gameover=False
                        running=False
                elif event.type==pygame.QUIT:
                    gameover=False
                    running=False

        

        
        screen=pygame.display.set_mode((width,width))
        screen.fill((0,0,0))
        #drawgrid(screen, width,rows)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if dirn!="right":
                        snake1_x_change=-20
                        snake1_y_change=0
                        dirn="left"
    
                elif event.key==pygame.K_RIGHT:
                    if dirn!="left":
                        snake1_x_change=20
                        snake1_y_change=0
                        dirn="right"
                    
                elif event.key==pygame.K_UP:
                    if dirn!="down":
                        snake1_y_change=-20
                        snake1_x_change=0
                        dirn="up"
                        
                elif event.key==pygame.K_DOWN:
                    if dirn!="up":
                        snake1_y_change=20
                        snake1_x_change=0
                        dirn="down"
        
                    
        snake1_x+=snake1_x_change
        snake1_y+=snake1_y_change

        if(snake1_x>(width-size)):
            snake1_x=width
            gameover=True
        elif(snake1_x<0):
            snake1_x=-size
            gameover=True
        elif(snake1_y>(width-size)):
            snake1_y=width
            gameover=True
        elif(snake1_y<0):
            snake1_y=-size
            gameover=True

        if(snake1_x==apple_x and snake1_y==apple_y):
            apple_x=round(random.randrange(0,(width-size))/size)*size
            apple_y=round(random.randrange(0,(width-size))/size)*size
            snakelen+=1
            for i in range(5):
                if level[i]==snakelen:
                    message("LEVEL: "+str(i+2),(0,0,155),100,300)
                    pygame.display.update()
                    time.sleep(2)
                    fps+=3
        message("SNAKELENGTH: "+str(snakelen),(255,255,255),20,20)

        snakehead=[]
        snakehead.append(snake1_x)
        snakehead.append(snake1_y)
        snakelist.append(snakehead)
        l=len(snakelist)-snakelen
        for i in range(l):
            del snakelist[0]
        
        snakelength(size,snakelist)
         
        for i in range(snakelen-1):
            if(snakelist[i]==snakelist[snakelen-1]):
                gameover=True

        

        apple(apple_x,apple_y,size)
        #snake(snake1_x,snake1_y)
        pygame.display.update()

        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()
