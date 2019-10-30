# Frogger-type game... STARTER CODE BELOW
# Matthew Schaefer (mes2pe) and Christopher Acciai (cga4yc)

# Meeting Required Features
#   User Input
"""
User input will allow the frog to move in every direction. It will be trying to navigate
both a road environment as well as a water area.

SOURCES:
https://www.spriters-resource.com/arcade/frogger/sheet/11067/
http://www.classicgaming.cc/classics/frogger/sounds
"""
#   Graphics/Images
"""
We will be animating the different obstacles as well as the frog character that can be
manipulated.
"""
#   Start Screen
"""
Game Name: Frogger
Student Names: Matthew Schaefer (mes2pe) and Christopher Acciai (cga4yc)
Basic Instructions: "Navigate your way back to the swamp! Use the directional buttons to avoid
the cars on the road and drowning in the water. Get hit or drown and you go back to the start.
You only have three tries, so make them count!" 
"""

# Optional Features
#   Enemies
"""
While they aren't characters, the possibility of getting hit by cars or drowning in the water
act as obstacles for completion which, we believe, fits the requirement for being enemies.
"""
#   Timer
"""
Depending on the route we chose to go, we can have a countdown timer to rush players into
crossing faster (also increasing the difficulty and likelihood of mistakes).
"""
#   Health Meter
"""
We plan on giving players three lives to get across the path of obstacles. Upon losing a life,
players will be sent back to the starting location. If they lose all three lives, they will
lose the game and we will indicate that visually.
"""
#   Music/Sound Effects
"""
This is another option we will be able to pursue, especially if we find a source file of the
original audio.
"""

import pygame
import gamebox

camera = gamebox.Camera(442,500)
background = gamebox.from_image(221,250, 'background.png')
roadlines = gamebox.from_image(221,405, 'road_lines.png')
roadlines2 = gamebox.from_image(221,440, 'road_lines.png')
roadlines3 = gamebox.from_image(221,370, 'road_lines.png')
roadlines4 = gamebox.from_image(221,335, 'road_lines.png')
roadlines5 = gamebox.from_image(221,300, 'road_lines.png')
show_splash = True
ticks = 0


def splash(keys):
    global show_splash
    camera.clear('blue')
    camera.draw(gamebox.from_text(camera.x,camera.y-150,"Frogger", "Arial",40,"green"))
    camera.draw(gamebox.from_text(camera.x, camera.y - 110, "--------------------------------------------------------", "Arial", 20, "green"))
    camera.draw(gamebox.from_text(camera.x,camera.y-80,"Navigate your way back to the swamp!", "Arial", 20, "green"))
    camera.draw(gamebox.from_text(camera.x, camera.y-55,"Use the directional buttons to avoid the cars", "Arial", 20, "green"))
    camera.draw(gamebox.from_text(camera.x, camera.y-30,"on the road and drowning in the water.", "Arial", 20, "green"))
    camera.draw(gamebox.from_text(camera.x, camera.y-5,"Get hit or drown and you go back to the start.", "Arial", 20, "green"))
    camera.draw(gamebox.from_text(camera.x, camera.y+20,"You only have three tries, so make them count!", "Arial", 20, "green"))
    camera.draw(gamebox.from_text(camera.x, camera.y + 150, "(Press space to continue)", "Arial", 20, "green"))
    camera.draw(gamebox.from_text(camera.x, camera.y + 60, "Christopher Acciai (cga4yc) and Matthew Schaefer (mes2pe)", "Arial", 21, "green"))

    if ticks > 120:
        show_splash = False
    if pygame.K_SPACE in keys:
        show_splash = False
    camera.display()

cars = [
    gamebox.from_image(0, 440, 'car.png'),
    gamebox.from_image(-500, 440, 'car.png'),

]
for car in cars:
    car.scale_by(2)
car2 = [
    gamebox.from_image(125, 405, 'car2.png'),
    gamebox.from_image(250, 405, 'car2.png'),
    gamebox.from_image(375, 405, 'car2.png'),
    gamebox.from_image(500, 405, 'car2.png'),
]

for car in car2:
    car.scale_by(2.2)

busses = [
    gamebox.from_image(250, 370, 'bus.png'),
    gamebox.from_image(500, 370, 'bus.png'),
]
for bus in busses:
    bus.scale_by(2.2)

car3 = [
    gamebox.from_image(100, 335, 'car3.png'),
    gamebox.from_image(200, 335, 'car3.png'),
    gamebox.from_image(300, 335, 'car3.png'),
    gamebox.from_image(400, 335, 'car3.png'),
    gamebox.from_image(500, 335, 'car3.png'),
]
for car in car3:
    car.scale_by(2.2)

car4 = [
    gamebox.from_image(166.66, 300, 'car4.png'),
    gamebox.from_image(333.32, 300, 'car4.png'),
    gamebox.from_image(500, 300, 'car4.png'),
]
for car in car4:
    car.scale_by(2.2)

logs = [
    gamebox.from_image(0, 191, 'large_log.png'),
    gamebox.from_image(250, 191, 'large_log.png'),
    gamebox.from_image(-250, 191, 'large_log.png'),
]
for log in logs:
    log.scale_by(1.7)

logs2 = [
    gamebox.from_image(125, 221, 'short_log.png'),
    gamebox.from_image(250, 221, 'short_log.png'),
    gamebox.from_image(375, 221, 'short_log.png'),
    gamebox.from_image(500, 221, 'short_log.png'),
]
for log in logs2:
    log.scale_by(1.7)

logs3 = [
    gamebox.from_image(125, 161, 'short_log.png'),
    gamebox.from_image(250, 161, 'short_log.png'),
    gamebox.from_image(375, 161, 'short_log.png'),
    gamebox.from_image(500, 161, 'short_log.png'),
    gamebox.from_image(500, 161, 'short_log.png'),
    gamebox.from_image(500, 161, 'short_log.png'),
]
for log in logs3:
    log.scale_by(1.7)

logs4 = [
    gamebox.from_image(166.66, 131, 'large_log.png'),
    gamebox.from_image(333.32, 131, 'short_log.png'),
    gamebox.from_image(500, 131, 'large_log.png'),
    gamebox.from_image(666.66, 131, 'short_log.png'),
]
for log in logs4:
    log.scale_by(1.7)

logs5 = [
    gamebox.from_image(250, 101, 'large_log.png'),
    gamebox.from_image(-250, 101, 'large_log.png'),
]
for log in logs5:
    log.scale_by(1.7)

logs6 = [
    gamebox.from_image(166.66, 71, 'large_log.png'),
    gamebox.from_image(333.32, 71, 'short_log.png'),
    gamebox.from_image(500, 71, 'large_log.png'),
    gamebox.from_image(666.66, 71, 'short_log.png'),
]
for log in logs6:
    log.scale_by(1.7)

logs7 = [
    gamebox.from_image(125, 41, 'short_log.png'),
    gamebox.from_image(250, 41, 'short_log.png'),
    gamebox.from_image(375, 41, 'short_log.png'),
    gamebox.from_image(500, 41, 'short_log.png'),
]
for log in logs7:
    log.scale_by(1.7)

run_over_sound = gamebox.load_sound("sound-frogger-squash.wav")
drown_sound = gamebox.load_sound("sound-frogger-plunk.wav")

character = gamebox.from_image(250,490,'frog_still.png')
character.scale_by(2)
character.last_move = 0
character.lives = 3
timer = 1200


def tick(keys):
    global ticks
    global timer
    ticks += 1
    timer -= 1

    if show_splash:
        splash(keys)
        return

    camera.draw(background)
    camera.draw(roadlines)
    camera.draw(roadlines2)
    camera.draw(roadlines3)
    camera.draw(roadlines4)
    camera.draw(roadlines5)

    time = gamebox.from_text(66, 10, "Time Remaining: " + str(timer//30), "Arial", 20, "black")
    camera.draw(time)
    life = gamebox.from_text(0,0, "Lives: "+str(character.lives), "Arial", 20, "black")
    life.top = camera.top
    life.right = camera.right
    lost = gamebox.from_text(221,250, "YOU LOSE!", "Arial", 60, "white")
    win = gamebox.from_text(221, 250, "YOU WIN!", "Arial", 60, "white")

    for car in cars:
        camera.draw(car)
        car.x += 9
        if car.left > camera.right:
            car.x -= 1000
    for car in car2:
        camera.draw(car)
        car.x -= 4
        if car.right < camera.left:
            car.x += 500
    for bus in busses:
        camera.draw(bus)
        bus.x -= 2
        if bus.right < camera.left:
            bus.x += 500
    for car in car3:
        camera.draw(car)
        car.x += 1.5
        if car.left > camera.right:
            car.x -= 500
    for car in car4:
        camera.draw(car)
        car.x += 4
        if car.left > camera.right:
            car.x -= 500
    for log in logs:
        camera.draw(log)
        log.x += 4
        if log.left > camera.right:
            log.x -= 750
    for log in logs2:
        camera.draw(log)
        log.x -= 4
        if log.right < camera.left:
            log.x += 750
    for log in logs3:
        camera.draw(log)
        log.x -= 4
        if log.right < camera.left:
            log.x += 500
    for log in logs4:
        camera.draw(log)
        log.x -= 5
        if log.right < camera.left:
            log.x += 666.66
    for log in logs5:
        camera.draw(log)
        log.x += 3
        if log.left > camera.right:
            log.x -= 1000
    for log in logs6:
        camera.draw(log)
        log.x -= 2
        if log.right < camera.left:
            log.x += 666.66
    for log in logs7:
        camera.draw(log)
        log.x += 4
        if log.left > camera.right:
            log.x -= 750

    if pygame.K_UP in keys and character.last_move < ticks - 4:
        character.y -= 30
        character.last_move = ticks
        character.image = 'frog_still.png'
    if pygame.K_RIGHT in keys and character.last_move < ticks - 4:
        character.x += 30
        character.last_move = ticks
        character.image = 'frog_right_still.png'
    if pygame.K_LEFT in keys and character.last_move < ticks - 4:
        character.x -= 30
        character.last_move = ticks
        character.image = 'frog_left_still.png'
    if pygame.K_DOWN in keys and character.last_move < ticks - 4:
        character.y += 30
        character.last_move = ticks
        character.image = 'frog_back_still.png'

    for car in cars:
        if character.touches(car):
            character.lives -= 1
            if character.lives == 0:
                run_over_sound.play()
                gamebox.pause()
                camera.draw(lost)
            else:
                run_over_sound.play()
                character.x = 250
                character.y = 490
    for car in car2:
        if character.touches(car):
            character.lives -= 1
            if character.lives == 0:
                run_over_sound.play()
                gamebox.pause()
                camera.draw(lost)
            else:
                run_over_sound.play()
                character.x = 250
                character.y = 490
    for bus in busses:
        if character.touches(bus):
            character.lives -= 1
            if character.lives == 0:
                run_over_sound.play()
                gamebox.pause()
                camera.draw(lost)
            else:
                run_over_sound.play()
                character.x = 250
                character.y = 490
    for car in car3:
        if character.touches(car):
            character.lives -= 1
            if character.lives == 0:
                run_over_sound.play()
                gamebox.pause()
                camera.draw(lost)
            else:
                run_over_sound.play()
                character.x = 250
                character.y = 490
    for car in car4:
        if character.touches(car):
            character.lives -= 1
            if character.lives == 0:
                run_over_sound.play()
                gamebox.pause()
                camera.draw(lost)
            else:
                run_over_sound.play()
                character.x = 250
                character.y = 490


    if 30 < character.y < 240:
        safe = False    # Consulted Professor Tychonievich for how I could work with the logs to make the water
        if character.x < 0 or character.x > 442:
            safe = True
        for log in logs2:
            if character.touches(log):
                safe = True
                character.x -= 4
                if character.x < camera.left:
                    character.x += 750
        for log in logs:
            if character.touches(log):
                safe = True
                character.x += 4
                if character.left > camera.right:
                    character.x -= 750
        for log in logs3:
            if character.touches(log):
                safe = True
                character.x -= 4
                if character.right < camera.left:
                    character.x += 500
        for log in logs4:
            if character.touches(log):
                safe = True
                character.x -= 5
                if character.right < camera.left:
                    character.x += 666.66
        for log in logs5:
            if character.touches(log):
                safe = True
                character.x += 3
                if character.left > camera.right:
                    character.x -= 1000
        for log in logs6:
            if character.touches(log):
                safe = True
                character.x -= 2
                if character.right < camera.left:
                    character.x += 666.66
        for log in logs7:
            if character.touches(log):
                safe = True
                character.x += 4
                if character.left > camera.right:
                    character.x -= 750
        if safe == False:
            character.lives -= 1
            if character.lives == 0:
                drown_sound.play()
                gamebox.pause()
                camera.draw(lost)
            else:
                drown_sound.play()
                character.x = 250
                character.y = 490

    if timer == 0 and character.y > 30:
        gamebox.pause()
        camera.draw(lost)

    if character.y <= 30:
        gamebox.pause()
        camera.draw(win)

    camera.draw(character)
    camera.draw(life)
    camera.display()

gamebox.timer_loop(30, tick)
