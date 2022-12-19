# import ספריות
import pygame
import random
import time
import sys, os
# משתנים שהוספנו
textToWin = ""
showTextWiner = True
ballMove = True
ball_direction = "left"
ball_x = random.randint(100,700)
if ball_x > 300:
    ball_direction == "left"
else:
    ball_direction == "right"
print(ball_x)
print(ball_direction)
#הגדרת מהירות רנדומלית לכדור
right_left_y = random.randint(4,10)
right_left_x = random.randint(2,6)
# init pygame
pygame.init()
# create the window and set the size
# יצירת חלון והגדרת הגודל שלו
win  = pygame.display.set_mode((800,500))
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
background = pygame.image.load(background_os)

player_os = resource_path("images/player.png")
player = pygame.image.load(player_os)

ball_os = resource_path("images/ball.png")
ball = pygame.image.load(ball_os)

gate_os = resource_path("images/gate.png")
gate = pygame.image.load(gate_os)

# player location
# מיקום השחקן
player_x = 400
player_y = 310
# ball random location 
# מיקום אקראי של החייזר

my_ball_y = 50
ball_y = my_ball_y
#המיקום של השער
gate_x = -312
gate_y = 270
# create the text font
# יצירת הפונט לטקסט
font = pygame.font.SysFont('bahnschrift', 32)
font2 = pygame.font.SysFont('bahnschrift', 80)

score = 0 
game_time = 60
time.sleep(1)

if ball_x > 300:
    ball_direction == "left"
else:
    ball_direction == "right"

# while run
# האם להפעיל
run = True 
while run:
    #פעולה המחשבת את צעדי הכדור
    if ballMove == True:
        if ball_direction == "left":
            ball_y = ball_y + right_left_y
            ball_x = ball_x - right_left_x
        elif ball_direction == "right":
            ball_y = ball_y + right_left_y
            ball_x = ball_x + right_left_x

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
        player_x = player_x + 8 
   # ask if the key is K_LEFT
   # בודק האם המקש הוא לחצן שמאל
    if keys[pygame.K_LEFT]: 
        player_x=player_x-8



    # if ballMove == True and (ball_x >= 750 or ball_x <= 0):
    #     if ball_direction == "left":
    #         ball_direction = "right"
    #     else:
    #         ball_direction = "left"
    # בודק אם הכדור נמצא בתחתית המסך
    if ballMove == True and ball_y >= 480:
        textToWin = "Game Over!!"
        showTextWiner = True
        pressedSpace = False
        ballMove = False
    #בודק אם השחקן נגע בכדור
    if player_y > ball_y - 80 and player_y < ball_y +80 and player_x > ball_x and player_x < ball_x +60:
        player_x += gate*ball_x
        player_y += gate * ball_y
        if ball_x > 300:
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

        ball_y = my_ball_y
        ballMove = True
        # if ball_x > 300:
        #     ball_direction == "left"
        # else:
        #     ball_direction == "right"



    # ask if the player at the end of the window 
    # בודק אם השחקן בקצה החלון
    if player_x > 550 : 
        player_x = 550
    # ask if the player at the begining of the window 
    # בודק אם השחקן בתחילת החלון
    if player_x < 150 :
        player_x = 150

    # fill the window with the background image
    # # ממלא את החלון בתמונת הרקע    
    win.blit(background,(0,0)) 
    # מלא את החלון בתמונות
    win.blit(player,(player_x,player_y))
    win.blit(gate,(gate_x, gate_y))
    win.blit(ball,(ball_x, ball_y))
    win.blit(winner, (100,100))
    # update the changes
    # מעדכן את השינויים
    pygame.display.update()
pygame.quit()