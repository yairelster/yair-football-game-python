import pygame
from random import randint
import time
import sys, os
import tkinter as tk
from tkinter import messagebox

# משתנים- הגדרות של המשחק בהתחלה
textToWin = ""
textToEnd = ""
showTextWiner = True
ballMove = True
ball_direction1, ball_direction2, ball_direction3, ball_direction4, ball_direction5, ball_direction6, = "","","","","",""
ball_direction7, ball_direction8, ball_direction9, ball_direction10, ball_direction11, ball_direction12 = "","","","","",""
balls_amount = 0
difficulty_amount= 0
score = 0
running = False
speed = 0 #מהירות תזוזת הכדור
fast = 0 #מהירות השחקן
single_player = True
multi_player = False
winner_x =0
lose_x = 0
side1 = True


# פונקציה להצגת חלון הגדרות
def show_settings():
    root = tk.Tk()
    root.title("game settings")
    root.geometry("535x656") 
    
    def update_difficulty(value):
        difficulty_label.config(text="Difficulty:  " + str(value))
    
    # מספר הכדורים
    def update_balls(value):
        balls_label.config(text="Maximum number of balls:  " + str(value))
    
    # פונקציה להצגת הוראות המשחק הרלוונטיות
    def display_instructions(instructions_text):
        instructions_label.config(text=instructions_text)
    
    # כמות כדורים
    balls_label = tk.Label(root, text="Maximum number of balls:  6", font=("Arial", 16))
    balls_label.pack()
    
    balls_scale = tk.Scale(root, from_=1, to=6, orient="horizontal", length=400, command=update_balls)
    balls_scale.set(6)  # ברירת מחדל 6
    balls_scale.pack()
    
    # רמת קושי
    difficulty_label = tk.Label(root, text="Difficulty:  5", font=("Arial", 16))
    difficulty_label.pack()
    
    difficulty_scale = tk.Scale(root, from_=1, to=10, orient="horizontal", length=400, command=update_difficulty)
    difficulty_scale.set(5)  # ברירת מחדל 5
    difficulty_scale.pack()
    
    # הוראות משחק עבור מצב שחקן יחיד
    rules_text_single = "In the game: you are the player\nand you must keep the ball from hitting the goal.\nYou play as the goalkeeper!\n\nButtons: To move right or left you need to\nuse the arrows on your keyboard\n\nThe goal of the game: to get as many points as possible\n\nDuring the game: the balls move towards the goal and\nyou have to touch them by moving. The more balls you hit,\nthe more points you get! The more points you get,\nthe more balls will be added to the game according to\nthe settings above. And the level of difficulty will\nalso change according to the settings above, good luck!"
    
    # חוקי המשחק
    rules_label = tk.Label(root, text="\nGame rules: ", font=("Arial", 16))
    rules_label.pack()
    
    instructions_label = tk.Label(root, text=rules_text_single, font=("Arial", 14), wraplength=500, justify=tk.LEFT)
    instructions_label.pack(pady=10)
    
    # פונקציה להתחיל את המשחק במצב שחקן יחיד
    def start_game_single_player():
        single_player_pressed.set(True)
        single_player_button.config(relief=tk.SUNKEN)
        two_players_button.config(relief=tk.RAISED)
        display_instructions(rules_text_single)
    
    # פונקציה להתחיל את המשחק במצב 2 שחקנים
    def start_game_two_players():
        single_player_pressed.set(False)
        single_player_button.config(relief=tk.RAISED)
        two_players_button.config(relief=tk.SUNKEN)
        new_instructions_text = "In the game: you are 2 players and you must keep the ball\nfrom hitting the goal.  You play as the goalkeeper!\n\nButtons: To move right or left you need to use the arrows\non your keyboard\nThe goal of the game: to get as many points as possible!\nThe player who won is the player who stays in the game the longest without being lose.\n\nDuring the game: the balls move towards the goal and\nyou have to touch them by moving. The more balls you hit,\nthe more points you get! The more points you get,\nthe more balls will be added to the game according to\nthe settings above. And the level of difficulty will\nalso change according to the settings above, good luck!"
        display_instructions(new_instructions_text)
    
    # התחלת המשחק
    def start_game():
        global running
        global balls_amount
        global difficulty_amount
        global single_player
        global multi_player
        balls_amount = balls = balls_scale.get()
        difficulty_amount = difficulty = difficulty_scale.get()
        
        root.destroy()
        
        if single_player_pressed.get():
            print("Single Player Mode started!")
            single_player = True
            multi_player = False
        else:
            print("2 Players Mode started!")
            single_player = False
            multi_player = True
        
        print("Maximum number of balls:", balls)
        print("Difficulty:", difficulty)
        
        running = True
        time.sleep(0.7)
    single_player_pressed = tk.BooleanVar()
    single_player_pressed.set(True)
    
    # כפתור מצב שחקן יחיד
    single_player_button = tk.Button(root, text="Single Mode", command=start_game_single_player, font=("Arial", 16))
    single_player_button.pack(side=tk.LEFT, pady=20)  
    single_player_button.config(width=15, relief=tk.SUNKEN) 
    
    # כפתור מצב 2 שחקנים
    two_players_button = tk.Button(root, text="2 Players Mode", command=start_game_two_players, font=("Arial", 16))
    two_players_button.pack(side=tk.RIGHT, pady=20)  
    two_players_button.config(width=15)  
    
    # כפתור התחלה
    start_button = tk.Button(root, text="Start!", command=start_game, font=("Arial", 16))
    start_button.pack(pady=30) 
    start_button.config(width=10) 
    
    root.mainloop()
    
# קריאה לפונקציה להצגת חלון הגדרות
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
fast = 22.5 - difficulty
if difficulty == 5:
    fast = 16
    speed = 0.9
speed = 0.55 + difficulty/10
fast_first = fast + 1
fast_second = fast_first +2
fast_third = fast_second + 0.5
fast_four = fast_third + 2
speed_zero = speed - 0.15
speed_first = speed_zero - 0.25
speed_second = speed_first - 0.15
speed_third = speed_second - 0.15




# Set the width and height of the screen
if single_player:
    screen_width = 800
    screen_height = 500
else:
    screen_width = 1600
    screen_height = 500
win = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Football Game')

# Create Footballs
goal,ball,ball2,ball3 = Football(-312, 270),Football(randint(0, 800), 100),Football(randint(0, 800), 100),Football(randint(0, 800), 100)
ball4,ball5,ball6,player = Football(randint(0, 800), 100),Football(randint(0, 800), 100),Football(randint(0, 800), 100),Football(400,300)
if multi_player:
    goal_2,ball7,ball8,ball9 = Football(512, 270),Football(randint(800, 1600), 100),Football(randint(800, 1600), 100),Football(randint(800, 1600), 100)
    ball10,ball11,ball12,player2 = Football(randint(800, 1600), 100),Football(randint(800, 1600), 100),Football(randint(800, 1600), 100),Football(1200,300)

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
if multi_player:
    while ball7.x > 1090 and ball7.x < 1235:
        ball7.x = randint(800,1600)
    while ball8.x > 1090 and ball8.x < 1235:
        ball8.x = randint(800,1600)
    while ball9.x > 1090 and ball9.x < 1235:
        ball9.x = randint(800,1600)
    while ball10.x > 1090 and ball10.x < 1235:
        ball10.x = randint(800,1600)
    while ball11.x > 100 and ball11.x < 1235:
        ball11.x = randint(800,1600)
    while ball12.x > 100 and ball12.x < 1235:
        ball12.x = randint(800,1600)

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
if multi_player:
    if ball7.x > 1150:
        ball_direction7 = "left"
    else:
        ball_direction7 = "right"
    if ball8.x > 1150:
        ball_direction8 = "left"
    else:
        ball_direction8 = "right"
    if ball9.x > 1150:
        ball_direction9 = "left"
    else:
        ball_direction9 = "right"
    if ball10.x > 1150:
        ball_direction10 = "left"
    else:
        ball_direction10 = "right"
    if ball11.x > 1150:
        ball_direction11 = "left"
    else:
        ball_direction11 = "right"
    if ball12.x > 1150:
        ball_direction12 = "left"
    else:
        ball_direction12 = "right"

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
        if multi_player:
            score += 0.5
        else:
            score += 1

        if ballX > 350:
            direction = "left"
        else:
            direction = "right"
        
    if  multi_player and (player2.y > ballY - 51 and player2.y < ballY + 51 and player2.x > ballX - 50.5 and player2.x < ballX + 50.5):
        ballX = randint(800, 1600)
        while ballX > 1090 and ballX < 1235:
            ballX = randint(800, 1600)
        ballY = 35
        score += 0.5

        if ballX > 1150:
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
player2_os = resource_path("images/player2.png")
player_ = pygame.image.load(player_os)

goal_os = resource_path("images/goal.png")
goal = pygame.image.load(goal_os)

ball_os = resource_path("images/ball.png")
ball_ = pygame.image.load(ball_os)
ball_2 = pygame.image.load(ball_os)
ball_3 = pygame.image.load(ball_os)
ball_4 = pygame.image.load(ball_os)
ball_5 = pygame.image.load(ball_os)
ball_6 = pygame.image.load(ball_os)
if multi_player:
    ball2_ = pygame.image.load(ball_os)
    ball2_2 = pygame.image.load(ball_os)
    ball2_3 = pygame.image.load(ball_os)
    ball2_4 = pygame.image.load(ball_os)
    ball2_5 = pygame.image.load(ball_os)
    ball2_6 = pygame.image.load(ball_os)
    goal2 = pygame.image.load(goal_os)
    player_2 = pygame.image.load(player2_os)
    background_2 = pygame.image.load(background_os)




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
    end = font2.render(textToEnd, False, "yellow")
    winner = font2.render(textToWin, False, "yellow")

    # display the score in the top of the window
    # הצג את הניקוד בחלק העליון של החלון
    pygame.display.set_caption("Your Score: "+ str(score))
    # get the keyboard keys list to variable     
    # קבלת את רשימת מקשי המקלדת למשתנה   
    keys= pygame.key.get_pressed()
    # ask if the key is K_RIGHT 
    # בודק האם המקש הוא לחצן ימין
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and multi_player == False: 
        player.x = player.x + fast 
    if multi_player and keys[pygame.K_d]: 
        player.x=player.x+fast
    if multi_player and keys[pygame.K_RIGHT]: 
        player2.x=player2.x+fast
   # ask if the key is K_LEFT
   # בודק האם המקש הוא לחצן שמאל
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and multi_player == False: 
        player.x=player.x-fast
    if multi_player and keys[pygame.K_a]: 
        player.x=player.x-fast
    if multi_player and keys[pygame.K_LEFT]:
        player2.x=player2.x-fast


    if ballMove == True and (ball.y >= 480 or ball2.y >= 480 or ball3.y >= 480 or ball4.y >= 480 or ball5.y >= 480 or ball6.y >= 480):
        if multi_player:
            side1 = True
        textToEnd = "Game Over!!"
        textToWin = "You won!!"
        ballMove = False
        showTextWiner = True
        winner_x = True
        lose_x = False
    if multi_player and ballMove == True and (ball7.y >= 480 or ball8.y >= 480 or ball9.y >= 480 or ball10.y >= 480 or ball11.y >= 480 or ball12.y >= 480):
        winner_x = False
        lose_x = True
        textToEnd = "Game Over!!"
        textToWin = "You won!!"
        side1 = False
        showTextWiner = True
        ballMove = False
    
    if score == 10 and balls >= 2:
        speed = speed_zero
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
    if multi_player:
        ball7.x, ball7.y, ball_direction7 = touch(ball7.x, ball7.y, ball_direction7)
        if score >= 10 and balls >= 2:
            ball8.x, ball8.y, ball_direction8 = touch(ball8.x, ball8.y, ball_direction8)
        if score >= 30 and balls >= 3:
            ball9.x, ball9.y, ball_direction9 = touch(ball9.x, ball9.y, ball_direction9)
        if score >= 60 and balls >= 4:
            ball10.x, ball10.y, ball_direction10 = touch(ball10.x, ball10.y, ball_direction10)
        if score >= 100 and balls >= 5:
            ball11.x, ball11.y, ball_direction11 = touch(ball11.x, ball11.y, ball_direction11)
        if score >= 150 and balls == 6:
            ball12.x, ball12.y, ball_direction12 = touch(ball12.x, ball12.y, ball_direction12)
    # ask if the player at the end of the window 
    # בודק אם השחקן בקצה החלון
    if player.x > 570 : 
        player.x = 570
    if multi_player and player2.x > 1370:
        player2.x = 1360
    # ask if the player at the begining of the window 
    # בודק אם השחקן בתחילת החלון
    if player.x < 140 :
        player.x = 140
    if multi_player and player2.x < 940:
        player2.x = 940

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
    if multi_player:
        win.blit(background_2,(800,-50)) 
        win.blit(player_2,(player2.x,player2.y))
        win.blit(goal,(910, 363))
        if ballMove:
            win.blit(ball2_,(ball7.x, ball7.y))
        if score >= 10 and ballMove and balls >=2:
            win.blit(ball2_2,(ball8.x, ball8.y))
        if score >= 30 and ballMove and balls >=3:
            win.blit(ball2_3,(ball9.x, ball9.y))
        if score >= 60 and ballMove and balls >=4:
            win.blit(ball2_4,(ball10.x, ball10.y))
        if score >= 100 and ballMove and balls >=5:
            win.blit(ball2_5,(ball11.x, ball11.y))
        if score >= 150 and ballMove and balls ==6:
            win.blit(ball2_6,(ball12.x, ball12.y))
        if side1:
            win.blit(winner, (980,270))
            win.blit(end, (180,270))
        else:
            win.blit(winner, (180,270))
            win.blit(end, (980,270))


    win.blit(goal,(110, 363))
    if multi_player == False:
        win.blit(end, (180,270))
    # update the changes
    # מעדכן את השינויים
    pygame.display.update()
# Quit Pygame
pygame.quit()