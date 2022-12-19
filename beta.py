import pygame
import math
import random
import time
import sys, os
# משתנים שהוספנו
textToWin = ""
showTextWiner = True
ballMove = True
ball_direction = "left"

# This is a simple class that represents a magnet
# It has a position (x and y) and a strength (strength)
class Magnet:
    def __init__(self, x, y, strength):
        self.x = x
        self.y = y
        self.strength = strength

# Initialize Pygame
pygame.init()

font = pygame.font.SysFont('bahnschrift', 32)
font2 = pygame.font.SysFont('bahnschrift', 80)

#משתנה שמראה לכדור לאן להגיע מהאמצע של השער
point = random.randint(-150,150)
score = 0 
game_time = 60
time.sleep(1)

# Set the width and height of the screen
screen_width = 800
screen_height = 500
win = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Magnet Game')

# Create two magnets with different strengths
gate = Magnet(-312, 270, 100)
ball = Magnet(random.randint(100, 700), 50, random.randint(-50000,-30000))
player = Magnet(400,300,100)
# load an image for window background 
# טעינת תמונות לרקע החלון
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    # PyInstaller יוצר תיקיית זמנית ומאחסן נתיב ב-_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# load the images
# טעינת תמונות
background_os = resource_path("images/background.png")
background_ = pygame.image.load(background_os)

player_os = resource_path("images/player.png")
player_ = pygame.image.load(player_os)

ball_os = resource_path("images/ball.png")
ball_ = pygame.image.load(ball_os)

gate_os = resource_path("images/gate.png")
gate_ = pygame.image.load(gate_os)
# Set the magnet that is being magnetized to ball
magnetized_magnet = ball
running = True
# This is the game loop
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Draw the magnets
#    pygame.draw.circle(screen, WHITE, (gate.x, gate.y), 50)
#    pygame.draw.circle(screen, RED, (ball.x, ball.y), 50)

    # Calculate the distance between the two magnets
    distance = ((gate.x - ball.x)**2 + (gate.y - ball.y)**2)**0.5

    # Calculate the force of attraction between the two magnets
    force = gate.strength * ball.strength / distance**2

    # Calculate the angle between the two magnets
    angle = math.atan2(ball.y - gate.y, gate.x + (ball.x+point))

    # Calculate the change in position for the magnetized magnet
    dx = force * math.cos(angle)
    dy = force * math.sin(angle)
    # Update the position of the magnetized magnet based on the force of attraction
    magnetized_magnet.x += dx
    magnetized_magnet.y += dy

    # Update the screen
    pygame.display.flip()

        # set the time delay of the elements on the screen
    # הגדר את השהיית הזמן של האלמנטים על המסך
    pygame.time.delay(30)
    winner = font2.render(textToWin, False, "yellow")
    # display the score in the top of the window
    # הצג את הניקוד בחלק העליון של החלון
    pygame.display.set_caption("Your Score: "+ str(score))
    # run the window till the user press on Quit
    # הפעל את החלון עד שהמשתמש ילחץ על צא
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    # get the keyboard keys list to variable     
    # קבלת את רשימת מקשי המקלדת למשתנה   
    keys= pygame.key.get_pressed()
    # ask if the key is K_RIGHT 
    # בודק האם המקש הוא לחצן ימין
    if keys[pygame.K_RIGHT]: 
        player.x = player.x + 8 
   # ask if the key is K_LEFT
   # בודק האם המקש הוא לחצן שמאל
    if keys[pygame.K_LEFT]: 
        player.x=player.x-8



    # if ballMove == True and (ball_x >= 750 or ball_x <= 0):
    #     if ball_direction == "left":
    #         ball_direction = "right"
    #     else:
    #         ball_direction = "left"
    # בודק אם הכדור נמצא בתחתית המסך
    if ballMove == True and ball.y >= 480:
        textToWin = "Game Over!!"
        showTextWiner = True
        pressedSpace = False
        ballMove = False
    #בודק אם השחקן נגע בכדור
    if player.y > ball.y - 51 and player.y < ball.y +51 and player.x > ball.x-50.5 and player.x < ball.x +50.5:
        ball.x = random.randint(000,800)
        #ball.strength = random.randint(4,10)
        point = random.randint(-150,150)
        ball.y = 50
        if ball.x > 300:
            ball_direction == "left"
        else:
            ball_direction == "right"
        #השחקן כאילו בועט בכדור למעלה בלולאה
        # ball_y= ball_y + 17
        # time.sleep(0.1)
        # ball_y= ball_y + 17
        # time.sleep(0.1)
        # ball_y= ball_y + 17
        # time.sleep(0.1)
        # ball_y= ball_y + 17
        # time.sleep(0.1)
        # set the status to false
        # מעדכן את הסטטוס לשקר
        ballMove = True
        # set the score
        # מעדכן את הניקוד
        score = score +1

        ballMove = True
        # if ball_x > 300:
        #     ball_direction == "left"
        # else:
        #     ball_direction == "right"



    # ask if the player at the end of the window 
    # בודק אם השחקן בקצה החלון
    if player.x > 550 : 
        player.x = 550
    # ask if the player at the begining of the window 
    # בודק אם השחקן בתחילת החלון
    if player.x < 150 :
        player.x = 150

    # fill the window with the background image
    # # ממלא את החלון בתמונת הרקע    
    win.blit(background_,(0,0)) 
    # מלא את החלון בתמונות
    win.blit(player_,(player.x,player.y))
    win.blit(gate_,(gate.x, gate.y))
    win.blit(ball_,(ball.x, ball.y))
    win.blit(winner, (100,100))
    # update the changes
    # מעדכן את השינויים
    pygame.display.update()
# Quit Pygame
pygame.quit()
