#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:27:23 2021

@author: kaspertidner
"""

import random

player1_steps = []

def roll_dice():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    
    return dice1, dice2


def roll(player_position):
    dice1, dice2 = roll_dice()
    walk_length = dice1 + dice2
    player_position = walk(walk_length, player_position)
    player1_steps.append(player_position)
    check_player_position(player_position)
    
    times_double = 0
    
    while dice1 == dice2:
        times_double += 1
        
        if times_double < 3:
            dice1, dice2 = roll_dice()
            walk_length = dice1 + dice2
            player_position = walk(walk_length, player_position)
            player1_steps.append(player_position)
            check_player_position(player_position)
        else:
            player_position = go_to_jail()
            break
   
    return player_position
        

def walk(walk_length, player_position):
    player_position += walk_length
    
    if player_position >= 40:
        player_position -= 40
    
    return player_position


def check_player_position(player_position):
    if player_position == 2:
        player_position = community_chest(player_position)
    elif player_position == 7:
        player_position = chance(player_position)
    elif player_position == 17:
        player_position = community_chest(player_position)
    elif player_position == 22:
        player_position = chance(player_position)
    elif player_position == 30:
        player_position = go_to_jail()
    elif player_position == 33:
        player_position = community_chest(player_position)
    elif player_position == 36:
        player_position = chance(player_position)
        
    return player_position
    

def community_chest(player_position):
    community_player_position = player_position
    card = random.randrange(1,17)
    if card == 1:
        player_position = go_to_jail()
    elif card == 2:
        player_position = 0
    
    if player_position != community_player_position and player_position != 10:
        player1_steps.append(player_position)    
    return player_position


def chance(player_position):
    chance_player_position = player_position
    card = random.randrange(1,17)
    if card == 1:
        player_position = go_to_jail()
    elif card == 2:
        player_position = 0
    elif card == 3:
        player_position -= 3
    elif card == 4:
        player_position = 5
    elif card == 5:
        player_position = 11
    elif card == 6:
        player_position = 24
    elif card == 7:
        player_position = 39
    elif card == 8:
        if player_position == 7:
            player_position = 15
        elif player_position == 22:
            player_position = 25
        elif player_position == 36:
            player_position = 5
    elif card == 9:
        if player_position == 7:
            player_position = 15
        elif player_position == 22:
            player_position = 25
        elif player_position == 36:
            player_position = 5
    
    if player_position != chance_player_position and player_position != 10:
        player1_steps.append(player_position)    
    return player_position


def go_to_jail():
    position = 10
    player1_steps.append(position)
    return position


def show_freq():
    rolls = len(player1_steps)
    
    for i in range(40):
        times_stepped = player1_steps.count(i)
        freq = round(times_stepped/rolls*100, 1)
        print("Ruta: ", str(i), ". Landades på: ", str(freq), "% av alla slag")


def main():
    player1 = 0
    
    for _ in range(10000):
        player1 = 0
        for i in range(50):
            player1 = roll(player1)
    
    show_freq()

main()