import curses
import random
import time


# initialize the curses module
stdscr = curses.initscr()

# clear the screen
stdscr.clear()

# get the screen size
max_y, max_x = stdscr.getmaxyx()



speed = 10
# rpm = random.randint(1000,2000)
fuel = 'low'


for i in range(3):
    # choose a random position for the number
    # print the number at the chosen position
    rpm = random.randint(1000,2000)
    stdscr.addstr(1, 1, str('speed = '+ str(speed)))
    stdscr.addstr(2, 1, str('rpm = '+ str(rpm)))
    stdscr.addstr(3, 1, str('fuel = '+ str(fuel)))
    time.sleep(3)
    stdscr.refresh()

stdscr.getch()

# end the curses module
curses.endwin()