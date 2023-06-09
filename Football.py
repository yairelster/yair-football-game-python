import pygame
from random import randint
import time
import sys, os
import tkinter as tk
from tkinter import messagebox

# משתנים- הגדרות של המשחק בהתחלה
textToWin = ""
showTextWiner = True
ballMove = True
ball_direction1, ball_direction2, ball_direction3, ball_direction4, ball_direction5, ball_direction6 = "","","","","",""
balls_amount = 0
difficulty_amount= 0
score = 0
running = False
speed = 0 #מהירות תזוזת הכדור
fast = 0 #מהירות השחקן


# פונקציה להצגת חלון הגדרות
def show_settings():
    root = tk.Tk()
    root.title("game settings")
    root.geometry("535x620")  # גודל החלון
    
    # פונקציה לעדכון רמת הקושי
    def update_difficulty(value):
        difficulty_label.config(text="Difficulty:  " + str(value))
    
    # פונקציה לעדכון מספר הכדורים
    def update_balls(value):
        balls_label.config(text="Maximum number of balls:  " + str(value))
    
    # כמות כדורים
    balls_label = tk.Label(root, text="Maximum number of balls:  6", font=("Arial", 14))
    balls_label.pack()
    
    balls_scale = tk.Scale(root, from_=1, to=6, orient="horizontal", length=400, command=update_balls)
    balls_scale.set(6)  # ברירת מחדל 3
    balls_scale.pack()
    
    # רמת קושי
    difficulty_label = tk.Label(root, text="Difficulty:  5", font=("Arial", 14))
    difficulty_label.pack()
    
    difficulty_scale = tk.Scale(root, from_=1, to=10, orient="horizontal", length=400, command=update_difficulty)
    difficulty_scale.set(5)  # ברירת מחדל 5
    difficulty_scale.pack()
    
    # חוקי המשחק
    rules_label = tk.Label(root, text="\nGame rules: ", font=("Arial", 14))
    rules_label.pack()
    
    rules_text = tk.Label(root, text="In the game: you are the player\nand you must keep the ball from hitting the goal.\nYou play as the goalkeeper!\n\nButtons: To move right or left you need to\nuse the arrows on your keyboard\n\nThe goal of the game: to get as many points as possible\n\nThe course of the game: the balls move towards the goal and\n you have to touch them by moving. The more balls you hit,\nthe more points you get! The more points you get,\nthe more balls will be added to the game according to\nthe settings above. And the level of difficulty will\nalso change according to the settings above, good luck!", font=("Arial", 14))
    rules_text.pack()
    
    # כפתור התחלה
    def start_game_button():
        global running
        balls = balls_scale.get()
        difficulty = difficulty_scale.get()
        
        root.destroy()
        running = True
        # קריאה לפונקציה שמתחילה את המשחק עם הפרמטרים הנבחרים
        start_game(balls, difficulty)
    
    start_button = tk.Button(root, text="Start!", command=start_game_button, font=("Arial", 16))
    start_button.pack(side=tk.BOTTOM, pady=20)  # הזזת הכפתור למטה
    start_button.config(width=10)  # שינוי רוחב הכפתור
    
    root.mainloop()

# פונקציה להתחיל את המשחק
def start_game(balls, difficulty):
    global balls_amount
    global difficulty_amount
    print("the game is starting!")
    print("Maximum number of balls:", balls)
    print("difficulty:", difficulty)
    balls_amount = balls
    difficulty_amount = difficulty


# פתיחת חלון הגדרות
show_settings()

# This is a simple class that represents a Football
# It has a position (x and y) and a strength (strength)
class Football:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Initialize Pygame
pygame.init()

font = pygame.font.SysFont('bahnschrift', 32)
font2 = pygame.font.SysFont('bahnschrift', 80)


#משתני הגדרות
balls = balls_amount
difficulty = difficulty_amount
fast = 22 - difficulty
speed = 0.55 + difficulty/10
fast_first = fast + 1
fast_second = fast_first +2
fast_third = fast_second + 0.5
fast_four = fast_third + 2
speed_first = speed - 0.25
speed_second = speed_first - 0.15
speed_third = speed_second - 0.15



# Set the width and height of the screen
screen_width = 800
screen_height = 500
win = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Football Game')

# Create Footballs
goal,ball,ball2,ball3 = Football(-312, 270),Football(randint(0, 800), 50),Football(randint(0, 800), 0),Football(randint(0, 800), 0)
ball4,ball5,ball6,player = Football(randint(0, 800), 0),Football(randint(0, 800), 0),Football(randint(0, 800), 0),Football(400,300)


while ball.x > 290 and ball.x < 435:
    ball.x = randint(0,800)
while ball2.x > 290 and ball2.x < 435:
    ball2.x = randint(0,800)
while ball3.x > 290 and ball3.x < 435:
    ball3.x = randint(0,800)
while ball4.x > 290 and ball4.x < 435:
    ball4.x = randint(0,800)
while ball5.x > 290 and ball5.x < 435:
    ball5.x = randint(0,800)
while ball6.x > 290 and ball6.x < 435:
    ball6.x = randint(0,800)

if ball.x > 350:
    ball_direction1 = "left"
else:
    ball_direction1 = "right"
if ball2.x > 350:
    ball_direction2 = "left"
else:
    ball_direction2 = "right"
if ball3.x > 350:
    ball_direction3 = "left"
else:
    ball_direction3 = "right"
if ball4.x > 350:
    ball_direction4 = "left"
else:
    ball_direction4 = "right"
if ball5.x > 350:
    ball_direction5 = "left"
else:
    ball_direction5 = "right"
if ball6.x > 350:
    ball_direction6 = "left"
else:
    ball_direction6 = "right"

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

def touch(ballX, ballY, direction):
    global score
    if player.y > ballY - 51 and player.y < ballY + 51 and player.x > ballX - 50.5 and player.x < ballX + 50.5:
        ballX = randint(0, 800)
        while ballX > 290 and ballX < 435:
            ballX = randint(0, 800)
        ballY = 35
        score += 1

        if ballX > 350:
            direction = "left"
        else:
            direction = "right"
    if ballMove:
        if direction == "left":
            ballX += 10 * -speed
        else:
            ballX += 10 * speed
        ballY += 10 * speed
    # החזרה של הערכים ששונו
    return ballX, ballY, direction


# load the images
# טעינת תמונות
background_os = resource_path("images/background.png")
background_ = pygame.image.load(background_os)

player_os = resource_path("images/player.png")
player_ = pygame.image.load(player_os)

ball_os = resource_path("images/ball.png")
ball_ = pygame.image.load(ball_os)
ball_2 = pygame.image.load(ball_os)
ball_3 = pygame.image.load(ball_os)
ball_4 = pygame.image.load(ball_os)
ball_5 = pygame.image.load(ball_os)
ball_6 = pygame.image.load(ball_os)

goal_os = resource_path("images/goal.png")
goal = pygame.image.load(goal_os)


# This is the game loop
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

        # set the time delay of the elements on the screen
    # הגדר את השהיית הזמן של האלמנטים על המסך
    pygame.time.delay(30)
    winner = font2.render(textToWin, False, "yellow")
    # display the score in the top of the window
    # הצג את הניקוד בחלק העליון של החלון
    pygame.display.set_caption("Your Score: "+ str(score))
    # get the keyboard keys list to variable     
    # קבלת את רשימת מקשי המקלדת למשתנה   
    keys= pygame.key.get_pressed()
    # ask if the key is K_RIGHT 
    # בודק האם המקש הוא לחצן ימין
    if keys[pygame.K_RIGHT]: 
        player.x = player.x + fast 
   # ask if the key is K_LEFT
   # בודק האם המקש הוא לחצן שמאל
    if keys[pygame.K_LEFT]: 
        player.x=player.x-fast


    if ballMove == True and (ball.y >= 480 or ball2.y >= 480 or ball3.y >= 480 or ball4.y >= 480):
        textToWin = "Game Over!!"
        showTextWiner = True
        pressedSpace = False
        ballMove = False
    
    if score == 10 and balls >= 2:
        fast == fast_first
    elif score == 30 and balls >= 3:
        speed == speed_first
        fast == fast_second
    elif score == 100 and balls >= 4:
        speed == speed_second
        fast == fast_third
    elif score == 160 and balls >= 5:
        speed == speed_third
        fast == fast_four
    ball.x, ball.y, ball_direction1 = touch(ball.x, ball.y, ball_direction1)
    if score >= 10 and balls >= 2:
        ball2.x, ball2.y, ball_direction2 = touch(ball2.x, ball2.y, ball_direction2)
    if score >= 30 and balls >= 3:
        ball3.x, ball3.y, ball_direction3 = touch(ball3.x, ball3.y, ball_direction3)
    if score >= 60 and balls >= 4:
        ball4.x, ball4.y, ball_direction4 = touch(ball4.x, ball4.y, ball_direction4)
    if score >= 100 and balls >= 5:
        ball5.x, ball5.y, ball_direction5 = touch(ball5.x, ball5.y, ball_direction5)
    if score >= 150 and balls == 6:
        ball6.x, ball6.y, ball_direction6 = touch(ball6.x, ball6.y, ball_direction6)
    # ask if the player at the end of the window 
    # בודק אם השחקן בקצה החלון
    if player.x > 570 : 
        player.x = 570
    # ask if the player at the begining of the window 
    # בודק אם השחקן בתחילת החלון
    if player.x < 140 :
        player.x = 140

    # fill the window with the background image
    # # ממלא את החלון בתמונת הרקע    
    win.blit(background_,(0,-50)) 
    # מלא את החלון בתמונות
    win.blit(player_,(player.x,player.y))
    if ballMove:
        win.blit(ball_,(ball.x, ball.y))
    if score >= 10 and ballMove and balls >=2:
        win.blit(ball_2,(ball2.x, ball2.y))
    if score >= 30 and ballMove and balls >=3:
        win.blit(ball_3,(ball3.x, ball3.y))
    if score >= 60 and ballMove and balls >=4:
        win.blit(ball_4,(ball4.x, ball4.y))
    if score >= 100 and ballMove and balls >=5:
        win.blit(ball_5,(ball5.x, ball5.y))
    if score >= 150 and ballMove and balls ==6:
        win.blit(ball_6,(ball6.x, ball6.y))


    win.blit(goal,(110, 363))
    win.blit(winner, (100,270))
    # update the changes
    # מעדכן את השינויים
    pygame.display.update()
# Quit Pygame
pygame.quit()