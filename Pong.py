# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:39:33 2021

@author: Yefry Lopez

You need intall Simplegui

You can see the code in action here:
    https://py3.codeskulptor.org/#user306_sydC1JTW7UoWgaO.py
"""

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
PAD_ACELERATION = 4

score1 = 0
score2 = 0
ball_vel = [0, 0]
direction = RIGHT or LEFT

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if  direction == RIGHT:
        ball_vel[0] =  random.randrange(120, 240)/ 60
        ball_vel[1] =  random.randrange(60, 180) / 60
    else:
        ball_vel[0] = -random.randrange(120, 240) / 60
        ball_vel[1] = -random.randrange(60, 180) / 60
   
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are 
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
     
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]     
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    if ball_pos[0] <= 0 :
        spawn_ball(RIGHT)
    elif ball_pos[0] >= 600 :
        spawn_ball(LEFT)
        
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
        
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
        
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Silver")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Silver")
    # collide and reflection of the ball with top and down of cavas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT-BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
    # determine whether paddle and ball collide    
   
        
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS :
        if (paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += ball_vel[0] * 0.10
            ball_vel[1] += ball_vel[1] * 0.10
        else:
            score2 += 1
            spawn_ball(RIGHT)
                   
    if (ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS):	
        if (paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
           
            ball_vel[0] += ball_vel[0] * 0.10
            ball_vel[1] += ball_vel[1] * 0.10
        else:
            score1 += 1
            spawn_ball(LEFT)
    # draw scores
    canvas.draw_text("Player 1: " + str(score1), [125,50], 28, "White")
    canvas.draw_text("Player 2: " + str(score2), [425,50], 28, "White")   
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= PAD_ACELERATION
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += PAD_ACELERATION
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= PAD_ACELERATION
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += PAD_ACELERATION

def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += PAD_ACELERATION
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= PAD_ACELERATION
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel += PAD_ACELERATION
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel -= PAD_ACELERATION

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('Lime')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game,100)
frame.add_button("Start",new_game,100)

# start frame

frame.start()